from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from .common_ops import CommonOps


class Products(CommonOps):
    PRODUCTS_TITLE = (By.CSS_SELECTOR, "div.features_items h2.title")
    SEARCH_FIELD = (By.ID, "search_product")
    SEARCH_BTN = (By.ID, "submit_search")
    PRODUCTS_ITEMS = (By.CSS_SELECTOR, "div.features_items  div.productinfo  p")

    FIRST_PRODUCT_ADD_TO_CART = (By.CSS_SELECTOR, " div.productinfo a[data-product-id='1']")
    FIRST_PRODUCT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div.overlay-content a[data-product-id='1']")
    MAST_HARBOUR_TITLE = (By.CSS_SELECTOR, "a[href='/brand_products/Mast & Harbour']")
    SECOND_PRODUCT_ADD_TO_CART = (By.CSS_SELECTOR, " div.productinfo a[data-product-id='2']")
    SECOND_PRODUCT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div.overlay-content a[data-product-id='2']")

    CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR, "div.modal-content button.btn-success.close-modal")
    VIEW_CART_LINK = (By.CSS_SELECTOR, "p.text-center a[href='/view_cart']")
    # AD_CLOSE_BUTTON = (By.CSS_SELECTOR, "div[id = 'ad_position_box'] div[id = 'dismiss-button']]")

    def get_products_title_text(self):
        return self.wait_for(self.PRODUCTS_TITLE).text

    def enter_search_criteria_and_perform_search(self, search_criteria):
        self.find(self.SEARCH_FIELD).send_keys(search_criteria)
        self.find(self.SEARCH_BTN).click()

    def get_searched_product_items(self):
        searched_products = self.find_elements(self.PRODUCTS_ITEMS)
        searched_products_text = []
        for product in searched_products:
            product_text = product.text
            searched_products_text.append(product_text)
        return searched_products_text

    def find_first_product_and_add_to_cart(self):
        add_to_cart_button = self.find(self.FIRST_PRODUCT_ADD_TO_CART)
        action_chains = ActionChains(self.driver)
        self.scroll_to_element(self.MAST_HARBOUR_TITLE)
        action_chains.move_to_element(add_to_cart_button).perform()
        self.wait_for(self.FIRST_PRODUCT_ADD_TO_CART_BTN).click()

    def click_continue_shopping_button(self):
        self.wait_for(self.CONTINUE_SHOPPING_BTN).click()

    def find_second_product_and_add_to_cart(self):
        add_to_cart_button = self.find(self.SECOND_PRODUCT_ADD_TO_CART)
        action_chains = ActionChains(self.driver)
        self.scroll_to_element(self.MAST_HARBOUR_TITLE)
        action_chains.move_to_element(add_to_cart_button).perform()
        self.wait_for(self.SECOND_PRODUCT_ADD_TO_CART_BTN).click()

    def click_view_cart_link(self):
        self.wait_for(self.VIEW_CART_LINK).click()

    # def visibility_of_ad(self):
    #     self.wait_for(self.AD_CLOSE_BUTTON)
    #
    # def click_close_ad_button(self):
    #     self.find(self.AD_CLOSE_BUTTON).click()
