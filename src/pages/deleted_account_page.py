from selenium.webdriver.common.by import By

from .common_ops import CommonOps


class DeletedAccount(CommonOps):
    DELETED_ACCOUNT_TITLE = (By.CSS_SELECTOR, "h2.title b")
    CONTINUE_BTN = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def get_deleted_account_title_text(self):
        return self.find(self.DELETED_ACCOUNT_TITLE).text

    def click_continue_button(self):
        self.find(self.CONTINUE_BTN).click()
