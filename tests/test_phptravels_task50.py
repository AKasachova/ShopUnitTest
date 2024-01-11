import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://phptravels.com/demo/")
    driver.maximize_window()
    yield driver
    driver.quit()


# def login_test_data():
#     test_data = []
#     with open('login_test_data.csv', newline='') as testfile:
#         reader = csv.DictReader(testfile)
#         for row in reader:
#             test_data.append((row['username'], row['password']))
#     return test_data


# @pytest.mark.parametrize("username, password", login_test_data())
@pytest.mark.parametrize("username, password", [('alionakosachova@gmail.com', 'Aliona1!'), ('kosachova17021991@mail.ru','Aliona2!')])
def test_login(browser, username, password):
    default_timeout = WebDriverWait(browser, 5)
    # Current tab
    main_tab = browser.current_window_handle
    login_button = default_timeout.until(ec.element_to_be_clickable((By.CLASS_NAME, 'btn-outline-dark')))
    login_button.click()
    # Wait for the new tab to be visible
    default_timeout.until(lambda driver: len(driver.window_handles) > 1)
    all_tabs = browser.window_handles
    # Switch to the new tab
    new_tab = [tab for tab in all_tabs if tab != main_tab][0]
    browser.switch_to.window(new_tab)
    # Wait for the login form to be visible
    default_timeout.until(ec.presence_of_element_located((By.CLASS_NAME, "login-form")))
    # Add login data
    email_input = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")
    # Skip captcha element (on a real project feature captcha ("I'm not a robot") must be off/automation is not possible)
    login_button_2 = default_timeout.until(ec.element_to_be_clickable((By.ID, "login")))
    actions = ActionChains(browser)
    actions.move_to_element(login_button_2)
    actions.perform()
    # Adding existing user correct data
    email_input.send_keys(username)
    password_input.send_keys(password)
    # Set captcha verification manually.This waiter pauses the execution of the script (introduces explicit waits), but do it unlike implicit and explicit waits provided by Selenium WebDriver(does not dynamically wait for the conditions to be met).
    time.sleep(30)
    login_button_2.click()
    # Verify username on a page after logging into the account
    browser.maximize_window()
    # Explicit wait for the username to appear after login with custom polling frequency
    actual_username = WebDriverWait(browser, 20, poll_frequency=5).until(ec.presence_of_element_located((By.CSS_SELECTOR, "a.btn-active-client span"))).text
    assert "Test" in actual_username, f"Unexpected username is presented in the 'Logged in as', got username: {actual_username}"
