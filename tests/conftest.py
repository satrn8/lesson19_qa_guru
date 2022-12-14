import os
import pytest
from dotenv import load_dotenv
from appium import webdriver
from datetime import date
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def mobile_android():
    USER = os.getenv('LOGIN')
    KEY = os.getenv('KEY')
    APPIUM_BROWSERSTACK = os.getenv('APPIUM_BROWSERSTACK')

    desired_cap = {
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        "deviceName": "Google Pixel 3",
        "platformVersion": "9.0",
        "platformName": "android",
        "project": "Python project",
        "build": "browserstack-build-" + str(date.today())
    }
    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{USER}:{KEY}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_cap
    )
    browser.config.timeout = 4
    yield mobile_android
    browser.quit()