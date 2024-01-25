import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "",
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": False
    #     }
    # }
    # driver = webdriver.Remote(
    #     command_executor="http://localhost:4444/wd/hub",
    #     options=capabilities)


    # moon_options = {
    #     "enableVNC": True,
    #     "enableVideo": True
    # }
    #
    # options = Options()
    # options.set_capability("browserName", "chrome")
    # options.set_capability("moon:options", moon_options)
    #
    # driver = webdriver.Remote(
    #     command_executor="http://localhost:4444/wd/hub",
    #     options=options)
    driver.implicitly_wait(5)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    yield driver
    driver.quit()
