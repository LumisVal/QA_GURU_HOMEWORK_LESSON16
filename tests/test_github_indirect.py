import pytest

from selene.support.shared import browser
from selene import be, have


@pytest.mark.parametrize(
    "window_size",
    [
        (1920, 1080),
        (1366, 768),
    ],
    indirect=True,
)
def test_github_sign_in_desktop_indirect(window_size):
    browser.open("https://github.com")

    browser.all("a[href='/login']").element_by(have.exact_text("Sign in")).click()

    browser.element("#login_field").should(be.visible)


@pytest.mark.parametrize(
    "window_size",
    [
        (390, 844),
    ],
    indirect=True,
)
def test_github_sign_in_mobile_indirect(window_size):
    browser.open("https://github.com/login")

    browser.element("#login_field").should(be.visible)