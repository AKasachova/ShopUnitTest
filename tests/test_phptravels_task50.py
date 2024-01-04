import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class ByLocators:
    FIRST_NAME_INPUT = By.TAG_NAME, "input[name='first_name']"
    LOGIN_BUTTON = By.ID, "login"
    SUBMIT_BUTTON = By.XPATH, "//button[@id='demo']"
    LAST_NAME_INPUT = By.CSS_SELECTOR, "input[name='last_name']"
    BUSINESS_NAME_INPUT = By.NAME, "business_name"
    NAVBAR_TOGGLER_BUTTON = By.CLASS_NAME, "navbar-toggler"
    LOGO_LINK = By.LINK_TEXT, "https://phptravels.com/"
    LINKEDIN_LINK = By.PARTIAL_LINK_TEXT, "company"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.get("https://phptravels.com/demo/")
    driver.maximize_window()
    yield driver
    driver.quit()


def login_test_data():
    test_data = []
    with open('login_test_data.csv', newline='') as testfile:
        reader = csv.DictReader(testfile)
        for row in reader:
            test_data.append((row['username'], row['password']))
    return test_data
# [("alionakosachova@gmail.com", "Aliona1!"), ("kosachova17021991@mail.ru", "Aliona2!")]

@pytest.mark.parametrize("username, password", login_test_data())
def test_login(browser, username, password):
    # Current tab
    main_tab = browser.current_window_handle
    login_button = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, 'btn-outline-dark')))
    login_button.click()
    # Wait for the new tab to be visible
    WebDriverWait(browser, 10).until(lambda driver: len(driver.window_handles) > 1)
    all_tabs = browser.window_handles
    # Switch to the new tab
    new_tab = [tab for tab in all_tabs if tab != main_tab][0]
    browser.switch_to.window(new_tab)
    # Wait for the login form to be visible
    WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "login-form")))
    # Add login data
    email_input = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")
    # Skip captcha element (on a real project feature captcha ("I'm not a robot") must be off/automation is not possible)
    login_button_2 = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.ID, "login")))
    browser.execute_script("arguments[0].scrollIntoView(true);", login_button_2)
    # Adding existing user correct data
    email_input.send_keys(username)
    password_input.send_keys(password)
    # Set captcha verification manually
    time.sleep(30)
    login_button_2.click()
    # Verify username on a page after logging into the account
    browser.maximize_window()
    link_element = browser.find_element(By.CSS_SELECTOR, "a.btn-active-client")
    actual_username = link_element.find_element(By.TAG_NAME, "span").text
    expected_username = "Test"
    assert expected_username in actual_username, f"Expected '{expected_username}' to be present in the 'Logged in as', but got: {actual_username}"
