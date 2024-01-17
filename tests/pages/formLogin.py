from selenium.webdriver.common.by import By

from .common import CommonOps


class LogIn(CommonOps):

    PAGE_TITLE = (By.CSS_SELECTOR, "#login h2")
    FORM_USERNAME = (By.ID, "username")
    FORM_PASSWORD = (By.ID, "password")
    FORM_SUBMIT_BTN = (By.ID, "submit")

    def navigate_to_form(self):
        self.scroll_to_element(self.FORM_USERNAME)

    def enter_login_username(self, username):
        self.wait_for(self.FORM_USERNAME).send_keys(username)

    def enter_login_password(self, password):
        self.find(self.FORM_PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find(self.FORM_SUBMIT_BTN).click()

    def check_title_text(self):
        return self.find(self.PAGE_TITLE).text
