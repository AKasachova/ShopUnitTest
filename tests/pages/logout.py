from selenium.webdriver.common.by import By

from .common import CommonOps


class Logout(CommonOps):

    SUCCESS_LOGIN_TITLE = (By.CLASS_NAME, "post-title")
    LOG_OUT_BTN = (By.CLASS_NAME, "wp-block-button__link")

    def successful_log_in(self):
        return self.wait_for(self.SUCCESS_LOGIN_TITLE).text

    def click_log_out_button(self):
        self.find(self.LOG_OUT_BTN).click()
