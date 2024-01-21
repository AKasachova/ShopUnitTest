from selenium.webdriver.common.by import By

from .common_ops import CommonOps
import allure


class Logout(CommonOps):
    SUCCESS_LOGIN_TITLE = (By.CLASS_NAME, "post-title")
    LOG_OUT_BTN = (By.CLASS_NAME, "wp-block-button__link")

    @allure.step('Get Logged in successfully page title')
    def successful_log_in(self):
        return self.wait_for(self.SUCCESS_LOGIN_TITLE).text

    @allure.step('Get Logged in successfully page title')
    def click_log_out_button(self):
        self.find(self.LOG_OUT_BTN).click()
