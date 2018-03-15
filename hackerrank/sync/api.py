import requests
from collections import namedtuple
from typing import Generator

BASE_URL = "https://www.hackerrank.com/"
LOGIN = f"{BASE_URL}auth/login"
SUBMISSIONS = f"{BASE_URL}rest/contests/master/submissions/"
CHALLENGES = f"{BASE_URL}rest/contests/master/challenges/"
SESSION_COOKIE = "_hrank_session"
CSRF_MARKER = "csrf-token\" content=\""


def get_csrf(page: str) -> str:
    "Find the CSRF token in the login page"
    index = page.find(CSRF_MARKER)
    start = index + len(CSRF_MARKER)
    end = page[start:].find("\"")
    return page[start:start + end]


def create_api():
    "Build a Hackerrank API object"
    session = requests.Session()
    response = session.get(BASE_URL)
    session.headers.update({"X-CSRF-Token": get_csrf(response.text)})
    return HackerRankAPI(session)


def paginate(request, per_page=100):
    """
    Paginate an API call
    
    It should use offset and limit and return {"total": x, "models":[...]}
    """
    offset = 0
    while True:
        res = request({"offset": offset, "limit": per_page})
        total = res["total"]
        models = res["models"]

        yield from models
        if offset + len(models) >= total:
            break
        offset += len(models)

Submission = namedtuple("Submission", [
    "code", "track", "slug", "language", "created_at_epoch"])

Track = namedtuple("Track", ["track_slug", "slug"])

class Challenge:
    def __init__(self, model: dict):
        self.__model = model
    
    def render(self, submission: Submission) -> str:
        lang = submission.language
        head = self.__model.get(f"{lang}_template_head", "")
        tail = self.__model.get(f"{lang}_template_tail", "")
        return "\n".join((head, submission.code, tail))


def create_submission(submission: dict) -> Submission:
    "Creates a Submission object from a dict"
    track = submission["track"]
    return Submission(
        submission["code"],
        Track(track["track_slug"], track["slug"]),
        submission["slug"],
        submission["language"],
        int(submission["created_at_epoch"]))

class HackerRankAPI:
    def __init__(self, session: requests.Session):
        self.__session = session

    def login(self, login: str, password: str) -> None:
        data = {
            "login": login,
            "password": password
        }
        login_res = self.__session.post(LOGIN, data=data).json()
        if "status" not in login_res or not login_res["status"] :
            raise Exception(", ".join(login_res['errors']))

    def submissions(self) -> Generator[Submission, None, None]:
        for s in paginate(lambda p: self.__get(SUBMISSIONS, params=p)):
            yield self.submission(s["id"])

    def submission(self, submission_id: int) -> Submission:
        return create_submission(
            self.__get(f"{SUBMISSIONS}{submission_id}")["model"])
    
    def challenge(self, challenge_slug: str) -> dict:
        return Challenge(self.__get(f"{CHALLENGES}{challenge_slug}")["model"])

    def __get(self, url: str, **kwargs):
        "Wraps a session get request returning json"
        return self.__session.get(url, **kwargs).json()