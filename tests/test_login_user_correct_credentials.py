import pytest
from src.pages.home_page import Home
import time



@pytest.mark.usefixtures("driver")
class TestLoginUserWithCorrectCreds:
    def test_home_page_visible(self, driver):
        home_page = Home(driver)
        assert "Automation" in home_page.home_title_text(), "Home page is not displayed!"

    def test_signup_login_page_visible(self, driver):
        signup_login_page = Home(driver).signup_login_page()
        assert "Login to your account" in signup_login_page.get_login_title_text(), " 'Login' page is not displayed!"

    def test_logged_in_username_visible(self, driver):
        signup_login_page = Home(driver).signup_login_page()
        signup_login_page.enter_login_email("alionakasachova@gmail.com")
        signup_login_page.enter_login_password("Aliona1!")
        signup_login_page.click_login_button()
        home_page = Home(driver)
        assert "Logged in as" in home_page.logged_in_text() and "Aliona" in home_page.username_text(), \
            "The new account wasn't logged in"



@pytest.mark.usefixtures("driver")
class TestAccountDeletedAfterLogin:

    def test_account_deleted(self, driver):
        signup_login_page = Home(driver).signup_login_page()
        signup_login_page.enter_login_email("alionakasachova@gmail.com")
        signup_login_page.enter_login_password("Aliona1!")
        signup_login_page.click_login_button()
        # time to remove pop-ups and ads manually
        time.sleep(10)
        deleted_account_page = Home(driver).deleted_account_page()
        assert "ACCOUNT DELETED!" in deleted_account_page.get_deleted_account_title_text(), "The account wasn't deleted!"
