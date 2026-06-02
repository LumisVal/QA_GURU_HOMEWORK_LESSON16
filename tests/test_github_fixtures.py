from selene.support.shared import browser
from selene import be


def test_github_sign_in_desktop_with_fixture(desktop_browser):
    browser.open("https://github.com/login")

    browser.element("#login_field").should(be.visible)


def test_github_sign_in_mobile_with_fixture(mobile_browser):
    browser.open("https://github.com/login")

    browser.element("#login_field").should(be.visible)