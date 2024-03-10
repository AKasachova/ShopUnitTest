from src.pages.home_page import Home
from src.pages.account_created_page import AccountCreated
import time


class TestRegisterUser:
    def test_home_page_visible(self, web_browser):
        home_page = Home(web_browser)
        assert "Automation" in home_page.home_title_text(), "Home page is not displayed!"

    def test_signup_login_page_visible(self, web_browser):
        signup_login_page = Home(web_browser).signup_login_page()
        assert "New User Signup!" in signup_login_page.get_signup_title_text(), " 'Login' page is not displayed!"

    def test_account_info_form_title_visible(self, web_browser):
        signup_login_page = Home(web_browser).signup_login_page()
        signup_login_page.sign_up_user("Aliona", "alionakasachova+61@gmail.com")
        assert "ENTER ACCOUNT INFORMATION" in signup_login_page.get_signup_info_title_text(), " 'Signup' page is not displayed!"

    def test_account_successfully_created_and_deleted_after_log_in(self, web_browser):
        signup_login_page = Home(web_browser).signup_login_page()
        signup_login_page.sign_up_user("Aliona", "alionakasachova+61@gmail.com")

        signup_login_page.fill_new_user_info('Aliona1!', 1, "January", 2000, 'Aliona', 'Kasachova', 'Coherent Solutions', 'Test', 'Test2', 'Canada',
                                            'Test3', 'Test4', 12345, 123456789)

        account_created_page = AccountCreated(web_browser)
        assert "ACCOUNT CREATED!" in account_created_page.get_account_created_title_text(), " The new account wasn't created!"

        account_created_page.click_continue_button()
        # time to remove pop-ups and ads manually
        time.sleep(10)
        assert "Logged in as" in Home(web_browser).logged_in_text() and "Aliona" in Home(web_browser).username_text(), \
            "The new account wasn't logged in!"

        deleted_account_page = Home(web_browser).deleted_account_page()
        assert "ACCOUNT DELETED!" in deleted_account_page.get_deleted_account_title_text(), "The account wasn't deleted!"
