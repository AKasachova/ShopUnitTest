from src.pages.home_page import Home
from src.pages.account_created_page import AccountCreated
import time


class TestLoginUserWithCorrectCreds:

    def test_signup_login_page_visible(self, web_browser):
        home_page = Home(web_browser)
        assert "Automation" in home_page.home_title_text(), "Home page is not displayed!"

        signup_login_page = home_page.signup_login_page()
        assert "Login to your account" in signup_login_page.get_login_title_text(), "'Login' page is not displayed!"

    def test_logged_in_username_visible_deletion_of_the_account(self, web_browser):
        # creating of the new account
        signup_login_page = Home(web_browser).signup_login_page()
        signup_login_page.sign_up_user("Aliona2", "alionakasachova+52@gmail.com")

        signup_login_page.fill_new_user_info('Aliona2!', 1, "January", 2000, 'Aliona2', 'Kasachova',
                                             'Coherent Solutions', 'Test', 'Test2', 'Canada',
                                             'Test3', 'Test4', 12345, 123456789)

        AccountCreated(web_browser).click_continue_button()
        # time to remove pop-ups and ads manually
        time.sleep(10)

        signup_login_page = Home(web_browser).click_logout_link()
        # log in with the new account
        signup_login_page.log_in_user("alionakasachova+52@gmail.com", 'Aliona2!')

        assert "Logged in as" in Home(web_browser).logged_in_text() and "Aliona2" in Home(web_browser).username_text(), \
            "The new account wasn't logged in!"

        deleted_account_page = Home(web_browser).deleted_account_page()
        # it is used method lower() cause the test is failing in Firefox
        assert "account deleted!" in deleted_account_page.get_deleted_account_title_text().lower(), "The account wasn't deleted!"
