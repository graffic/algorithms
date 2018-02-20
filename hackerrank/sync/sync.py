"""
Sync HackerRank sumbissions with the filesystem.
"""
import requests
import os

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


class HackerRankAPI:
    def __init__(self, session):
        self.__session = session

    def login(self, login, password):
        data = {
            "login": login,
            "password": password
        }
        login_res = self.__session.post(LOGIN, data=data).json()
        if "status" not in login_res or not login_res["status"] :
            raise Exception(", ".join(login_res['errors']))

       
    def submissions(self):
        current = {"offset": 0, "limit": 3}
        while True:
            res = self.__session.get(SUBMISSIONS, params=current).json()
            yield from res['models']
            if current["offset"] + len(res["models"]) >= res["total"]:
                break
            current["offset"] += len(res["models"])

    def submission(self, submission_id):
        return self.__session.get(f"{SUBMISSIONS}{submission_id}").json()["model"]


def to_file(submission):
    base = os.path.join("..", submission["track"]["slug"])
    filename = submission["slug"] + EXTENSIONS.get(submission["language"], "unknown")
    full = os.path.join(base, filename)
    if not os.path.exists(base):
        os.makedirs(base)
    print(f"Creating {full}")
    with open(full, 'w') as output:
        output.write(submission["code"])


def cli():
    login = os.environ.get("LOGIN")
    password = os.environ.get("PASSWORD")

    api = create_api()
    api.login(login, password)

    for submission in api.submissions():
        to_file(api.submission(submission["id"]))
    
if __name__ == "__main__":
    cli()



