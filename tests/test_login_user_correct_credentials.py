import pytest
from src.pages.home_page import Home
import time


@pytest.mark.usefixtures("web_browser")
class TestLoginUserWithCorrectCreds:
    def test_home_page_visible(self, web_browser, browser):
        home_page = Home(web_browser)
        assert "Automation" in home_page.home_title_text(), "Home page is not displayed!"

    def test_signup_login_page_visible(self, web_browser, browser):
        signup_login_page = Home(web_browser).signup_login_page()
        assert "Login to your account" in signup_login_page.get_login_title_text(), "'Login' page is not displayed!"

    def test_logged_in_username_visible(self, web_browser, browser):
        signup_login_page = Home(web_browser).signup_login_page()
        signup_login_page.enter_login_email("alionakasachova@gmail.com")
        signup_login_page.enter_login_password("Aliona1!")
        signup_login_page.click_login_button()
        assert "Logged in as" in Home(web_browser).logged_in_text() and "Aliona" in Home(web_browser).username_text(), \
            "The new account wasn't logged in!"


@pytest.mark.usefixtures("web_browser")
class TestAccountDeletedAfterLogin:

    def test_account_deleted(self, web_browser, browser):
        signup_login_page = Home(web_browser).signup_login_page()
        signup_login_page.enter_login_email("alionakasachova@gmail.com")
        signup_login_page.enter_login_password("Aliona1!")
        signup_login_page.click_login_button()
        # time to remove pop-ups and ads manually
        time.sleep(10)
        deleted_account_page = Home(web_browser).deleted_account_page()
        # it is used method lower() cause the test is failing in Firefox
        assert "account deleted!" in deleted_account_page.get_deleted_account_title_text().lower(), "The account wasn't deleted!"
