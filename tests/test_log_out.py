from .pages.formLogin import LogIn
from .pages.logout import Logout


def test_log_in_success(driver):
    form = LogIn(driver)
    form.navigate_to_form()
    form.enter_login_username("student")
    form.enter_login_password("Password123")
    form.click_login_button()

    logout_page = Logout(driver)
    logout_page.click_log_out_button()

    login_page_title = form.check_title_text()
    assert "Test login" in login_page_title, "User isn't logged out!"
