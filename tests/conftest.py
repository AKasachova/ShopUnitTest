import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    moon_options = {
         "enableVNC": True,
         "enableVideo": False
     }

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "119.0")
    options.set_capability("moon:options", moon_options)

    driver = webdriver.Remote(
         command_executor="http://localhost:4444/wd/hub",
         options=options)
    driver.implicitly_wait(5)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    return driver
    # driver.quit()
