from selenium.webdriver.common.by import By
from src.pages.signup_login_page import SignupLogin
from src.pages.deleted_account_page import DeletedAccount
from src.pages.products_page import Products
from src.pages.view_cart_page import ViewCart

from .common_ops import CommonOps


class Home(CommonOps):
    HOME_TITLE = (By.CSS_SELECTOR, "div.carousel-inner span")
    HOME_TITLE_TEXT = 'Automation'
    NAVBAR_HOME_ACTIVE = (By.LINK_TEXT, "/")
    NAVBAR_SIGNUP_LOGIN = (By.CSS_SELECTOR, "a[href='/login']")
    NAVBAR_PRODUCTS = (By.CSS_SELECTOR, "a[href='/products']")
    NAVBAR_CART = (By.CSS_SELECTOR, "a[href='/view_cart']")

    LOGGED_IN = (By.CSS_SELECTOR, "div.shop-menu li:last-child a")
    USERNAME = (By.CSS_SELECTOR, "div.shop-menu li:last-child b")
    DELETE_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/delete_account']")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")

    CATEGORY_TITLE = (By.XPATH, "//div[@id='accordian']/preceding-sibling::h2")
    CATEGORY_WOMEN = (By.CSS_SELECTOR, "a[href='#Women']")
    CATEGORY_KIDS = (By.CSS_SELECTOR, "a[href='#Kids']")
    CATEGORY_DRESS = (By.CSS_SELECTOR, "a[href='/category_products/1']")

    def home_title_text(self):
        return self.wait_for(self.HOME_TITLE).text

    def signup_login_page(self):
        self.find(self.NAVBAR_SIGNUP_LOGIN).click()
        return SignupLogin(self.driver)

    def logged_in_text(self):
        return self.wait_for(self.LOGGED_IN).text

    def username_text(self):
        return self.wait_for(self.USERNAME).text

    def click_logout_link(self):
        self.wait_for(self.LOGOUT_LINK).click()
        return SignupLogin(self.driver)

    def deleted_account_page(self):
        self.find(self.DELETE_ACCOUNT_LINK).click()
        return DeletedAccount(self.driver)

    def get_products_page(self):
        self.find(self.NAVBAR_PRODUCTS).click()
        return Products(self.driver)

    def get_view_cart_page(self):
        self.find(self.NAVBAR_CART).click()
        return ViewCart(self.driver)

    def get_category_title_text(self):
        return self.wait_for(self.CATEGORY_TITLE).text

    def get_category_women_title_text(self):
        return self.wait_for(self.CATEGORY_WOMEN).text

    def scroll_to_kids_title_text(self):
        self.scroll_to_element(self.CATEGORY_KIDS)

    def click_category_women(self):
        self.wait_for(self.CATEGORY_WOMEN).click()

    def click_category_dress(self):
        self.wait_for(self.CATEGORY_DRESS).click()
