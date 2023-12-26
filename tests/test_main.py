import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class ByLocators:
    TAG_NAME = By.TAG_NAME, "tag name from the project to find element by"
    ID = By.ID, "Id from the project to find element by"
    XPATH = By.XPATH, "Xpath from the project to find element by"
    CSS_SELECTOR = By.CSS_SELECTOR, "CSS selector from the project to find element by"
    NAME = By.NAME, "Element name from the project to find element by"
    CLASS_NAME = By.CLASS_NAME, "Class name from the project to find element by"
    LINK_TEXT = By.LINK_TEXT, 'Link search, to search hyperlinks  for the text displayed on this hyperlink'
    PARTIAL_LINK_TEXT = By.PARTIAL_LINK_TEXT, 'Link search, to search hyperlinks  for the text displayed on this hyperlink'


class TestLoginWithCorrectCreds(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get('https://phptravels.com/demo/')
        self.driver.maximize_window()
        # Current tab
        main_tab = self.driver.current_window_handle
        login_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, 'btn-outline-dark')))
        if login_button.is_displayed():
            login_button.click()
        else:
            print("Element is not visible.")
        # Wait for the new tab to be visible
        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
        all_tabs = self.driver.window_handles
        # Switch to the new tab
        new_tab = [tab for tab in all_tabs if tab != main_tab][0]
        self.driver.switch_to.window(new_tab)
        # Wait for the login form to be visible
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "login-form")))
        self.driver.maximize_window()
        # Add login data
        email_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        # recaptcha_checkbox functionality must be disabled
        login_button_2 = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.ID, "login")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_button_2)

        email_input.send_keys("alionakosachova@gmail.com")
        password_input.send_keys("Aliona1!")
        #On real project feature  capcha ("I'm not a robot") must be off/automatization is not possible
        time.sleep(30)
        login_button_2.click()

        current_url = self.driver.current_url
        self.driver.maximize_window()
        link_element = self.driver.find_element(By.CSS_SELECTOR, "a.btn-active-client")
        username = link_element.find_element(By.TAG_NAME, "span").text

        self.assertIn("Test", username, f"Expected 'Test' to be present in the Logged in as, but got: {username}")

    # if __name__ == '__main__':
    #     unittest.main()

