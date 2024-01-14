from .pages.formLogin import LogIn
from .pages.logout import Logout


def test_log_in_success(driver):
    form = LogIn(driver)
    form.make_screenshot_of_page('./tests/screenshots/test_login.png')
    form.navigate_to_form()
    form.enter_login_username("student")
    form.enter_login_password("Password123")
    form.click_login_button()

    logout_page = Logout(driver)
    success_log_in_text = logout_page.successful_log_in()
    assert "Logged In Successfully" in success_log_in_text, "User isn't logged in!"
