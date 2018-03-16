"""
Sync HackerRank sumbissions with the filesystem.
"""
import requests
import os
from collections import namedtuple
from typing import Generator
from api import create_api, Submission, Challenge


EXTENSIONS = {
    "ada": "ada",
    "bash": "sh",
    "c": "c",
    "clojure": "clj",
    "cobol": "",
    "coffeescript": "coffee",
    "cpp": "cpp",
    "cpp14": "cpp",
    "csharp": "cs",
    "d": "d",
    "elixir": "exs",
    "erlang": "erl",
    "fortran": "f90",
    "fsharp": "fs",
    "go": "go",
    "groovy": "groovy",
    "haskell": "hs",
    "java": "java",
    "java8": "java",
    "javascript": "js",
    "julia": "jl",
    "kotlin": "kt",
    "lua": "lua",
    "objectivec": "m",
    "ocaml": "ml",
    "pascal": "pas",
    "perl": "pl",
    "php": "php",
    "pypy": "py",
    "pypy3": "py",
    "python": "py",
    "python3": "py",
    "racket": "rkt",
    "ruby": "rb",
    "rust": "rs",
    "sbcl": "sbcl",
    "scala": "scala",
    "swift": "swift",
    "tcl": "tcl",
    "visualbasic": "vb"}


def build_path(submission: Submission) -> (str, str):
    "Builds the final path of the file"
    track = submission.track
    base = os.path.join("..", track.track_slug, track.slug)
    filename = submission.slug + "." + EXTENSIONS.get(submission.language, "unknown")
    full = os.path.join(base, filename)
    return base, full

def should_skip_submission(full: str, submission: Submission) -> bool:
    "If we should overwrite the current file with the Submission"
    if not os.path.isfile(full):
        return False
    current_timestamp = os.stat(full).st_mtime
    submission_timestamp = submission.created_at_epoch
    return current_timestamp >= submission_timestamp


def to_file(submission: Submission, challenge: Challenge) -> None:
    "Dumps a sumbission into a file"
    base, full = build_path(submission)

    # We need the base directory there.
    if not os.path.exists(base):
        os.makedirs(base)
    
    # Check dates
    if should_skip_submission(full, submission):
        print(f"Skipping {full} it is older or the same than curent file")
        return

    print(f"Creating {full}")
    with open(full, 'w') as output:
        output.write(challenge.render(submission.language, submission.code))
    os.utime(full, (0, int(submission.created_at_epoch)))


def cli() -> None:
    "Command line script"
    login = os.environ.get("LOGIN")
    password = os.environ.get("PASSWORD")

    api = create_api()
    api.login(login, password)

    for submission in api.submissions():
        challenge = api.challenge(submission.slug)
        to_file(submission, challenge)


if __name__ == "__main__":
    cli()



