import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="class", params=["chrome", "firefox"])
def browser(request):
    return request.param


@pytest.fixture(scope="class")
def driver(browser):
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
    driver.implicitly_wait(5)
    driver.get("https://www.automationexercise.com/")
    return driver
    # driver.quit()
