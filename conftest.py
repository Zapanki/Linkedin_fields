import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import allure
from allure_commons.types import AttachmentType


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    yield browser
    browser.implicitly_wait(20)
    allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    browser.quit()

@pytest.fixture()
def browser_firefox():
    services = FirefoxService(GeckoDriverManager().install())
    browser_firefox = webdriver.Firefox(service=services)
    browser_firefox.maximize_window()
    yield browser_firefox
    browser_firefox.implicitly_wait(20)
    allure.attach(browser_firefox.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    browser_firefox.quit()