import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    yield driver
    driver.quit()

