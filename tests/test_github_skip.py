import pytest

from selene.support.shared import browser
from selene import be, have


def is_mobile(size):
    width, height = size
    return width < height


def test_github_sign_in_desktop(browser_size):
    if is_mobile(browser_size):
        pytest.skip("Desktop test is skipped for mobile screen size")

    browser.open("https://github.com")

    browser.all("a[href='/login']").element_by(have.exact_text("Sign in")).click()

    browser.element("#login_field").should(be.visible)


def test_github_sign_in_mobile(browser_size):
    if not is_mobile(browser_size):
        pytest.skip("Mobile test is skipped for desktop screen size")

    browser.open("https://github.com/login")

    browser.element("#login_field").should(be.visible)