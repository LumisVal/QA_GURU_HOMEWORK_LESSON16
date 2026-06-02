import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser


@pytest.fixture
def desktop_browser():
    options = Options()
    driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.timeout = 6
    driver.set_window_size(1920, 1080)

    yield browser

    browser.quit()


@pytest.fixture
def mobile_browser():
    options = Options()
    options.add_experimental_option(
        "mobileEmulation",
        {
            "deviceName": "iPhone X"
        }
    )

    driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.timeout = 6

    yield browser

    browser.quit()


@pytest.fixture(params=[
    (1920, 1080),
    (1366, 768),
    (390, 844),
])
def browser_size(request):
    width, height = request.param

    options = Options()
    driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.timeout = 6
    driver.set_window_size(width, height)

    yield width, height

    browser.quit()


@pytest.fixture
def window_size(request):
    width, height = request.param

    options = Options()
    driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.timeout = 6
    driver.set_window_size(width, height)

    yield width, height

    browser.quit()