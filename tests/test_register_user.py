import pytest
from src.pages.home_page import Home
from src.pages.account_created_page import AccountCreated
import time



@pytest.mark.usefixtures("driver")
class TestRegisterUser:
    def test_home_page_visible(self, driver):
        home_page = Home(driver)
        assert "Automation" in home_page.home_title_text(), "Home page is not displayed!"

    def test_signup_login_page_visible(self, driver):
        signup_login_page = Home(driver).signup_login_page()
        assert "New User Signup!" in signup_login_page.get_signup_title_text(), " 'Login' page is not displayed!"

    def test_account_info_form_title_visible(self, driver):
        signup_login_page = Home(driver).signup_login_page()
        signup_login_page.enter_signup_name("Aliona1")
        signup_login_page.enter_signup_email("alionakasachova+40@gmail.com")
        signup_login_page.click_signup_button()
        assert "ENTER ACCOUNT INFORMATION" in signup_login_page.get_signup_info_title_text(), " 'Signup' page is not displayed!"

    def test_account_successfully_created_and_logged_in(self, driver):
        signup_login_page = Home(driver).signup_login_page()
        signup_login_page.enter_signup_name("Aliona2")
        signup_login_page.enter_signup_email("alionakasachova+41@gmail.com")
        signup_login_page.click_signup_button()

        signup_login_page.fill_account_info('Aliona1!', 1, "January", 2000)
        signup_login_page.select_signup_info_sign_up_for_checkbox()
        signup_login_page.select_signup_info_receive_checkbox()
        signup_login_page.fill_address_info('Aliona2', 'Kasachova', 'Coherent Solutions', 'Test', 'Test2', 'Canada',
                                            'Test3', 'Test4', 12345, 123456789)

        signup_login_page.click_create_account_button()
        assert "ACCOUNT CREATED!" in AccountCreated(
            driver).get_account_created_title_text(), " The new account wasn't created!"

        account_created_page = AccountCreated(driver)
        account_created_page.click_continue_button()
        # time to remove pop-ups and ads manually
        time.sleep(10)
        home_page = Home(driver)
        assert "Logged in as" in home_page.logged_in_text() and "Aliona" in home_page.username_text(), \
            "The new account wasn't logged in"



@pytest.mark.usefixtures("driver")
class TestDeleteAccount:
    def test_account_successfully_deleted_after_creation(self, driver):
        signup_login_page = Home(driver).signup_login_page()
        signup_login_page.enter_signup_name("Aliona5")
        signup_login_page.enter_signup_email("alionakasachova+42@gmail.com")
        signup_login_page.click_signup_button()

        signup_login_page.fill_account_info('Aliona1!', 1, "January", 2000)
        signup_login_page.select_signup_info_sign_up_for_checkbox()
        signup_login_page.select_signup_info_receive_checkbox()
        signup_login_page.fill_address_info('Aliona5', 'Kasachova', 'Coherent Solutions', 'Test', 'Test2', 'Canada',
                                            'Test3', 'Test4', 12345, 123456789)

        signup_login_page.click_create_account_button()
        account_created_page = AccountCreated(driver)
        account_created_page.click_continue_button()
        # time to remove pop-ups and ads manually
        time.sleep(10)
        deleted_account_page = Home(driver).deleted_account_page()
        assert "ACCOUNT DELETED!" in deleted_account_page.get_deleted_account_title_text(), "The account wasn't deleted!"
