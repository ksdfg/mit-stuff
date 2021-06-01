from decouple import config
from selenium.common.exceptions import TimeoutException

from . import run_github_login


def test_correct_email_and_password():
    assert run_github_login(config("ass1_email"), config("ass1_password")) == config("ass1_username")


def test_wrong_email():
    try:
        assert run_github_login("wrong@email.com", config("ass1_password")) != config("ass1_username")
    except TimeoutException:
        pass


def test_wrong_password():
    try:
        assert run_github_login(config("ass1_email"), "wROnGpAsSwOrD") != config("ass1_username")
    except TimeoutException:
        pass


def test_wrong_email_and_password():
    try:
        assert run_github_login("wrong@email.com", "wROnGpAsSwOrD") != config("ass1_username")
    except TimeoutException:
        pass
