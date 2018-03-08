"""
Sync HackerRank sumbissions with the filesystem.
"""
import requests
import os
from collections import namedtuple
from typing import Generator

BASE_URL = "https://www.hackerrank.com/"
LOGIN = f"{BASE_URL}auth/login"
SUBMISSIONS = f"{BASE_URL}rest/contests/master/submissions/"
SESSION_COOKIE = "_hrank_session"
CSRF_MARKER = "csrf-token\" content=\""
EXTENSIONS = {"python3": ".py", "elixir": ".exs"}


def get_csrf(page):
    index = page.find(CSRF_MARKER)
    start = index + len(CSRF_MARKER)
    end = page[start:].find("\"")
    return page[start:start + end]


def create_api():
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
    def __init__(self, session: str):
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

    def submission(self, submission_id) -> Submission:
        return create_submission(
            self.__get(f"{SUBMISSIONS}{submission_id}")["model"])
    
    def __get(self, url, **kwargs):
        "Wraps a session get request returning json"
        return self.__session.get(url, **kwargs).json()

def build_path(submission: Submission):
    "Builds the final path of the file"
    track = submission.track
    base = os.path.join("..", track.track_slug, track.slug)
    filename = submission.slug + EXTENSIONS.get(submission.language, "unknown")
    full = os.path.join(base, filename)
    return base, full

def is_newer(full, submission):
    "Is the submission older than the current"
    if not os.path.isfile(full):
        return False
    current_timestamp = os.stat(full).st_mtime
    submission_timestamp = submission.created_at_epoch
    return current_timestamp < submission_timestamp


def to_file(submission):
    "Dumps a sumbission into a file"
    base, full = build_path(submission)

    # We need the base directory there.
    if not os.path.exists(base):
        os.makedirs(base)
    
    # Check dates
    if not is_newer(full, submission):
        print(f"Skipping {full} it is older or the same than curent file")
        return

    print(f"Creating {full}")
    with open(full, 'w') as output:
        output.write(submission.code)
    os.utime(full, (0, int(submission.created_at_epoch)))


def cli():
    "Command line script"
    login = os.environ.get("LOGIN")
    password = os.environ.get("PASSWORD")

    api = create_api()
    api.login(login, password)

    for submission in api.submissions():
        to_file(submission)


if __name__ == "__main__":
    cli()



