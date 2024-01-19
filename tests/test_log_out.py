import pytest

from src.pages.login_page import LogIn
from src.pages.logged_in_successfully_page import Logout


@pytest.fixture
def logged_in_user(driver):
    login_page = LogIn(driver)
    login_page.navigate_to_form()
    login_page.enter_login_username("student")
    login_page.enter_login_password("Password123")
    login_page.click_login_button()
    return login_page


def test_log_out_success(driver, logged_in_user):
    logged_in_page = Logout(driver)
    logged_in_page.click_log_out_button()

    logged_out_page_title = logged_in_user.get_title_text()
    assert "Test login" in logged_out_page_title, "User isn't logged out!"
