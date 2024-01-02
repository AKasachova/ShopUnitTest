import unittest
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


class TestLoginWithCorrectCreds(unittest.TestCase):
    BASE_URL = 'https://phptravels.com/demo/'

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Current tab
        main_tab = self.driver.current_window_handle
        login_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CLASS_NAME, 'btn-outline-dark')))
        login_button.click()
        # Wait for the new tab to be visible
        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
        all_tabs = self.driver.window_handles
        # Switch to the new tab
        new_tab = [tab for tab in all_tabs if tab != main_tab][0]
        self.driver.switch_to.window(new_tab)
        # Wait for the login form to be visible
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "login-form")))
        # Add login data
        email_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        # Skip captcha element(on real project feature  captcha ("I'm not a robot") must be off/automation is not possible)
        login_button_2 = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.ID, "login")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_button_2)
        # Adding existing user correct data
        email_input.send_keys("alionakosachova@gmail.com")
        password_input.send_keys("Aliona1!")
        # Set captcha verification manually
        time.sleep(30)
        login_button_2.click()
        # Verify username on a page after log into the account
        self.driver.maximize_window()
        link_element = self.driver.find_element(By.CSS_SELECTOR, "a.btn-active-client")
        username = link_element.find_element(By.TAG_NAME, "span").text
        self.assertIn("Test", username, f"Expected 'Test' to be present in the 'Logged in as', but got: {username}")
    # This allows you to run tests if the file is run directly, but not if the file is imported into another script.
    # if __name__ == '__main__':
    #     unittest.main()
