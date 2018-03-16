"""
api module tests
"""
from api import (
    get_csrf,
    create_api,
    paginate,
    Submission,
    Track,
    Challenge,
    HackerRankAPI)
import requests
import responses
import pytest

TEST_PAGE = """
<!-- CSRF Token -->
<meta name="csrf-param" content="authenticity_token">
<meta name="csrf-token" content="spam">
<!-- Typography -->
"""
TEST_SUBMISSION = {
    "code": "code",
    "track": {
        "track_slug": "track_slug",
        "slug": "slug"
    },
    "slug": "slug",
    "language": "language",
    "created_at_epoch": "12345"
}



pluck = lambda d, *args: (d[arg] for arg in args)

def test_get_csrf():
    assert "spam" == get_csrf(TEST_PAGE)

def test_paginate():
    def fake_action(params):
        offset, limit = pluck(params, 'offset', 'limit')
        if offset == 0 and limit == 42:
            return {"total": 5, "models": ["spam"] * 3}
        if offset == 3 and limit == 42:
            return {"total": 5, "models": ["eggs"] * 2}
        raise Exception()
    
    assert list(paginate(fake_action, 42)) == ["spam", "spam", "spam", "eggs", "eggs"]

@pytest.mark.parametrize("model,expected", [
    ({}, "42"),
    ({"c_template_head": "spam"},"spam\n42"),
    ({"c_template_tail": "eggs"},"42\neggs"),
    ({"c_template_head": "spam", "c_template_tail": "eggs"}, "spam\n42\neggs"),
])
def test_challenge_render(model, expected):
    sut = Challenge(model)
    submission = Submission("42", None, None, "c", None)
    assert expected == sut.render("c", "42")

@responses.activate
def test_create_api_right_token_in_headers():
    responses.add(
        responses.GET,
        "https://www.hackerrank.com/",
        body=TEST_PAGE)
    
    api = create_api()
    
    responses.add(
        responses.POST,
        'https://www.hackerrank.com/auth/login',
        json={"status": True});
    api.login("42", "42")
    assert responses.calls[1].request.headers["X-CSRF-Token"] == "spam"

@responses.activate
def test_API_login_ok():
    responses.add(
        responses.POST,
        'https://www.hackerrank.com/auth/login',
        json={"status": True});
    session = requests.Session()
    api = HackerRankAPI(session)
    api.login("spam", "bacon")

    response = responses.calls[0]
    assert response.request.body == "login=spam&password=bacon"

@responses.activate
def test_API_login_error():
    responses.add(
        responses.POST,
        'https://www.hackerrank.com/auth/login',
        json={"status": False, "errors": ["spam", "eggs"]});
    session = requests.Session()
    api = HackerRankAPI(session)

    with pytest.raises(Exception):
        api.login("spam", "bacon")

@responses.activate
def test_API_submissions():
    responses.add(
        responses.GET,
        'https://www.hackerrank.com/rest/contests/master/submissions/',
        json={"models": [{"id": 42}], "total": 1})
    responses.add(
        responses.GET,
        'https://www.hackerrank.com/rest/contests/master/submissions/42',
        json={"model": TEST_SUBMISSION})
    session = requests.Session()
    api = HackerRankAPI(session)
    result = list(api.submissions())[0]
    expected = Submission(
        "code", Track("track_slug", "slug"), "slug", "language", 12345)
    assert result == expected

@responses.activate
def test_API_challenge():
    responses.add(
        responses.GET,
        'https://www.hackerrank.com/rest/contests/master/challenges/spam',
        json={"model": {"c_template_head": "42"}}
    )
    session = requests.Session()
    api = HackerRankAPI(session)
    challenge = api.challenge("spam")
    assert challenge.render("c", "code") == "42\ncode"