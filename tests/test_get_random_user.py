import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://demo.seleniumeasy.com/dynamic-data-loading-demo.html")
    yield driver
    driver.quit()


def test_wait_for_random_user_creation(browser):
    get_new_user_button = browser.find_element(By.ID, "save")
    browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'start' });", get_new_user_button)
    get_new_user_button.click()
    # Wait for loading random user data
    loading_user_data = WebDriverWait(browser, 7).until_not(lambda d: 'loading...' in d.find_element(By.ID, "loading").text)
    presence_user_img = WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.XPATH, "//div[@id='loading']//img")))
    loading_user_text = WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.XPATH, "//div[@id='loading']"))).text
    assert "First Name :" and "Last Name :" in loading_user_text, f"Random user's data wasn't loaded"
