import allure

from src.pages.login_page import LogIn
from src.pages.logged_in_successfully_page import Logout


@allure.feature('Log in')
@allure.story('Successful Log in')
@allure.title('Verify successful Log in')
@allure.description('Verify successful Log in by checking title of loaded page after log in')
@allure.severity('Critical')
def test_log_in_success(driver):
    login_page = LogIn(driver)
    login_page.navigate_to_form()
    login_page.enter_login_username("student")
    login_page.enter_login_password("Password123")
    login_page.click_login_button()

    logged_in_page = Logout(driver)
    success_log_in_text = logged_in_page.successful_log_in()
    with allure.step('Verify page title after log in'):
        assert "Logged In Successfully" in success_log_in_text, "User isn't logged in!"
