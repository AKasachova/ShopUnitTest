import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
import platform
from datetime import datetime


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def web_browser(request):
    run_in_selenoid = os.getenv("RUN_IN_SELENOID")
    browser = os.getenv("BROWSER")
    if run_in_selenoid == 'True':
        b = remote_driver(browser)
    else:
        b = local_driver(browser)

    b.implicitly_wait(5)
    b.get("https://www.automationexercise.com/")
    b.maximize_window()

    yield b

    if request.node and hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            browser_info = f"Browser: {b.capabilities['browserName']} Version: {b.capabilities['browserVersion']}"

            b.execute_script("document.body.bgColor = 'white';")

            allure.attach(b.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(f"Test execution timestamp: {current_datetime}",
                          name="Timestamp",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(browser_info,
                          name="Browser Info",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"Platform: {platform.system()} {platform.version()}", name="Platform Info",
                          attachment_type=allure.attachment_type.TEXT)
        except:
            print('The report''s attachment can''t be generated!')


def local_driver(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        print('Set needed browser: Chrome/Firefox!')
    return driver


def remote_driver(browser):
    moon_options = {
        "enableVNC": True,
        "enableVideo": False
    }
    if browser == "chrome":
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_capability("browserName", "firefox")
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    options.set_capability("browserVersion", "120.0")
    options.set_capability("moon:options", moon_options)

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options)
    return driver
