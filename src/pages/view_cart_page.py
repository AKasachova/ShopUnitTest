from selenium.webdriver.common.by import By
from .common_ops import CommonOps


class ViewCart(CommonOps):
    FIRST_PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    SECOND_PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "a[href='/product_details/2']")
    FIRST_PRODUCT_PRICE = (By.CSS_SELECTOR, "tr[id='product-1'] td.cart_price p")
    SECOND_PRODUCT_PRICE = (By.CSS_SELECTOR, "tr[id='product-2'] td.cart_price p")
    FIRST_PRODUCT_QUANTITY = (By.CSS_SELECTOR, "tr[id='product-1'] td.cart_quantity button")
    SECOND_PRODUCT_QUANTITY = (By.CSS_SELECTOR, "tr[id='product-2'] td.cart_quantity button")
    FIRST_PRODUCT_TOTAL_PRICE = (By.CSS_SELECTOR, "tr[id='product-1'] td.cart_total p")
    SECOND_PRODUCT_TOTAL_PRICE = (By.CSS_SELECTOR, "tr[id='product-2'] td.cart_total p")

    def get_first_product_description_text(self):
        return self.wait_for(self.FIRST_PRODUCT_DESCRIPTION).text

    def get_second_product_description_text(self):
        self.scroll_to_element(self.SECOND_PRODUCT_DESCRIPTION)
        return self.wait_for(self.SECOND_PRODUCT_DESCRIPTION).text

    def get_first_product_price_text(self):
        return self.wait_for(self.FIRST_PRODUCT_PRICE).text

    def get_second_product_price_text(self):
        return self.wait_for(self.SECOND_PRODUCT_PRICE).text

    def get_first_product_quantity_text(self):
        return self.wait_for(self.FIRST_PRODUCT_QUANTITY).text

    def get_second_product_quantity_text(self):
        return self.wait_for(self.SECOND_PRODUCT_QUANTITY).text

    def get_first_product_total_price_text(self):
        return self.wait_for(self.FIRST_PRODUCT_TOTAL_PRICE).text

    def get_second_product_total_price_text(self):
        return self.wait_for(self.SECOND_PRODUCT_TOTAL_PRICE).text
