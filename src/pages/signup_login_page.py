from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .common_ops import CommonOps


class SignupLogin(CommonOps):
    LOGIN_TITLE = (By.CSS_SELECTOR, "div.login-form h2")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[data-qa='login-button']")

    SIGNUP_TITLE = (By.CSS_SELECTOR, "div.signup-form h2")
    SIGNUP_NAME = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BTN = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    SIGNUP_INFO_TITLE = (By.XPATH, "//div[@class='login-form']//h2//b[position()=1]")
    SIGNUP_INFO_TITLE_MR_RADIO_BTN = (By.ID, "id_gender1")
    SIGNUP_INFO_PASSWORD = (By.ID, "password")
    SIGNUP_INFO_DAY_OF_BIRTH = (By.ID, "days")
    SIGNUP_INFO_MONTH_OF_BIRTH = (By.ID, "months")
    SIGNUP_INFO_YEAR_OF_BIRTH = (By.ID, "years")
    SIGNUP_INFO_SIGN_UP_FOR_CHECKBOX = (By.ID, "newsletter")
    SIGNUP_INFO_RECEIVE_CHECKBOX = (By.ID, "optin")
    SIGNUP_INFO_FIRST_NAME = (By.ID, "first_name")
    SIGNUP_INFO_LAST_NAME = (By.ID, "last_name")
    SIGNUP_INFO_COMPANY = (By.ID, "company")
    SIGNUP_INFO_ADDRESS = (By.ID, "address1")
    SIGNUP_INFO_ADDRESS2 = (By.ID, "address2")
    SIGNUP_INFO_COUNTRY = (By.ID, "country")
    SIGNUP_INFO_STATE = (By.ID, "state")
    SIGNUP_INFO_CITY = (By.ID, "city")
    SIGNUP_INFO_ZIPCODE = (By.ID, "zipcode")
    SIGNUP_INFO_MOBILE_NUMBER = (By.ID, "mobile_number")
    SIGNUP_INFO_CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, "button[data-qa='create-account']")

    def get_login_title_text(self):
        return self.find(self.LOGIN_TITLE).text

    def log_in_user(self, email, password):
        self.find(self.LOGIN_EMAIL).send_keys(email)
        self.wait_for(self.LOGIN_PASSWORD).send_keys(password)
        self.find(self.LOGIN_BTN).click()

    def get_signup_title_text(self):
        return self.find(self.SIGNUP_TITLE).text

    def sign_up_user(self, name, email):
        self.wait_for(self.SIGNUP_NAME).send_keys(name)
        self.find(self.SIGNUP_EMAIL).send_keys(email)
        self.find(self.SIGNUP_BTN).click()

    def get_signup_info_title_text(self):
        return self.find(self.SIGNUP_INFO_TITLE).text

    def fill_new_user_info(self, password, day, month, year, first_name, last_name, company, address, address2, country,
                           state, city, zipcode, mobile_number):
        self.find(self.SIGNUP_INFO_TITLE_MR_RADIO_BTN).click()
        self.scroll_to_element(self.SIGNUP_INFO_PASSWORD)
        self.find(self.SIGNUP_INFO_PASSWORD).send_keys(password)

        day_dropdown = Select(self.find(self.SIGNUP_INFO_DAY_OF_BIRTH))
        month_dropdown = Select(self.find(self.SIGNUP_INFO_MONTH_OF_BIRTH))
        year_dropdown = Select(self.find(self.SIGNUP_INFO_YEAR_OF_BIRTH))
        day_dropdown.select_by_visible_text(str(day))
        month_dropdown.select_by_visible_text(month)
        year_dropdown.select_by_visible_text(str(year))

        self.scroll_to_element(self.SIGNUP_INFO_FIRST_NAME)

        self.find(self.SIGNUP_INFO_SIGN_UP_FOR_CHECKBOX).click()
        self.find(self.SIGNUP_INFO_RECEIVE_CHECKBOX).click()

        self.find(self.SIGNUP_INFO_FIRST_NAME).send_keys(first_name)
        self.find(self.SIGNUP_INFO_LAST_NAME).send_keys(last_name)
        self.find(self.SIGNUP_INFO_COMPANY).send_keys(company)
        self.find(self.SIGNUP_INFO_ADDRESS).send_keys(address)
        self.find(self.SIGNUP_INFO_ADDRESS2).send_keys(address2)

        country_dropdown = Select(self.find(self.SIGNUP_INFO_COUNTRY))
        country_dropdown.select_by_visible_text(country)

        self.scroll_to_element(self.SIGNUP_INFO_STATE)
        self.find(self.SIGNUP_INFO_STATE).send_keys(state)
        self.find(self.SIGNUP_INFO_CITY).send_keys(city)
        self.find(self.SIGNUP_INFO_ZIPCODE).send_keys(zipcode)
        self.find(self.SIGNUP_INFO_MOBILE_NUMBER).send_keys(mobile_number)

        self.find(self.SIGNUP_INFO_CREATE_ACCOUNT_BTN).click()
