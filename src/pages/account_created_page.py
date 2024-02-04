from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .common_ops import CommonOps


class AccountCreated(CommonOps):
    ACCOUNT_CREATED_TITLE = (By.CSS_SELECTOR, ".title b")
    CONTINUE_BTN = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def get_account_created_title_text(self):
        return self.find(self.ACCOUNT_CREATED_TITLE).text

    def click_continue_button(self):
        self.find(self.CONTINUE_BTN).click()
