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

    def enter_login_email(self, email):
        self.find(self.LOGIN_EMAIL).send_keys(email)

    def enter_login_password(self, password):
        self.wait_for(self.LOGIN_PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find(self.LOGIN_BTN).click()

    def get_signup_title_text(self):
        return self.find(self.SIGNUP_TITLE).text

    def enter_signup_name(self, name):
        self.wait_for(self.SIGNUP_NAME).send_keys(name)

    def enter_signup_email(self, email):
        self.find(self.SIGNUP_EMAIL).send_keys(email)

    def click_signup_button(self):
        self.find(self.SIGNUP_BTN).click()

    def get_signup_info_title_text(self):
        return self.find(self.SIGNUP_INFO_TITLE).text

    def choose_info_title_mr_radio_button(self):
        self.find(self.SIGNUP_INFO_TITLE_MR_RADIO_BTN).click()

    def scroll_to_info_password(self):
        self.scroll_to_element(self.SIGNUP_INFO_PASSWORD)

    def scroll_to_info_first_name(self):
        self.scroll_to_element(self.SIGNUP_INFO_FIRST_NAME)

    def select_date_of_birth_dropdown_values(self, day, month, year):
        day_dropdown = Select(self.find(self.SIGNUP_INFO_DAY_OF_BIRTH))
        month_dropdown = Select(self.find(self.SIGNUP_INFO_MONTH_OF_BIRTH))
        year_dropdown = Select(self.find(self.SIGNUP_INFO_YEAR_OF_BIRTH))
        day_dropdown.select_by_visible_text(str(day))
        month_dropdown.select_by_visible_text(month)
        year_dropdown.select_by_visible_text(str(year))

    def select_signup_info_sign_up_for_checkbox(self):
        self.find(self.SIGNUP_INFO_SIGN_UP_FOR_CHECKBOX).click()

    def select_signup_info_receive_checkbox(self):
        self.find(self.SIGNUP_INFO_RECEIVE_CHECKBOX).click()

    def enter_info_signup_password(self, password):
        self.find(self.SIGNUP_INFO_PASSWORD).send_keys(password)

    def enter_info_first_name(self, first_name):
        self.find(self.SIGNUP_INFO_FIRST_NAME).send_keys(first_name)

    def enter_info_last_name(self, last_name):
        self.find(self.SIGNUP_INFO_LAST_NAME).send_keys(last_name)

    def enter_info_company(self, company):
        self.find(self.SIGNUP_INFO_COMPANY).send_keys(company)

    def enter_info_address(self, address):
        self.find(self.SIGNUP_INFO_ADDRESS).send_keys(address)

    def enter_info_address2(self, address2):
        self.find(self.SIGNUP_INFO_ADDRESS2).send_keys(address2)

    def select_country_dropdown_values(self, country):
        country_dropdown = Select(self.find(self.SIGNUP_INFO_COUNTRY))
        country_dropdown.select_by_visible_text(country)

    def scroll_to_info_state(self):
        self.scroll_to_element(self.SIGNUP_INFO_STATE)

    def enter_info_state(self, state):
        self.find(self.SIGNUP_INFO_STATE).send_keys(state)

    def enter_info_city(self, city):
        self.find(self.SIGNUP_INFO_CITY).send_keys(city)

    def enter_info_zipcode(self, zipcode):
        self.find(self.SIGNUP_INFO_ZIPCODE).send_keys(zipcode)

    def enter_info_mobile_number(self, mobile_number):
        self.find(self.SIGNUP_INFO_MOBILE_NUMBER).send_keys(mobile_number)

    def fill_account_info(self, password, day, month, year):
        self.choose_info_title_mr_radio_button()
        self.scroll_to_info_password()
        self.enter_info_signup_password(password)
        self.select_date_of_birth_dropdown_values(day, month, year)

    def fill_address_info(self, first_name, last_name, company, address, address2, country, state, city, zipcode,
                          mobile_number):
        self.scroll_to_info_first_name()
        self.enter_info_first_name(first_name)
        self.enter_info_last_name(last_name)
        self.enter_info_company(company)
        self.enter_info_address(address)
        self.enter_info_address2(address2)
        self.select_country_dropdown_values(country)
        self.scroll_to_info_state()
        self.enter_info_state(state)
        self.enter_info_city(city)
        self.enter_info_zipcode(zipcode)
        self.enter_info_mobile_number(mobile_number)

    def click_create_account_button(self):
        self.find(self.SIGNUP_INFO_CREATE_ACCOUNT_BTN).click()

    def get_login_title_text(self):
        return self.find(self.LOGIN_TITLE).text
