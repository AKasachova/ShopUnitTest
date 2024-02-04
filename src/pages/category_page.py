from selenium.webdriver.common.by import By

from .common_ops import CommonOps


class Category(CommonOps):
    CATEGORY_TITLE = (By.CSS_SELECTOR, "div.features_items h2.title")
    CATEGORY_MEN = (By.CSS_SELECTOR, "a[href='#Men']")
    SUBCATEGORY_JEANS = (By.CSS_SELECTOR, "a[href='/category_products/6']")

    def get_category_title_text(self):
        return self.wait_for(self.CATEGORY_TITLE).text

    def click_category_men(self):
        self.find(self.CATEGORY_MEN).click()

    def click_subcategory_jeans(self):
        self.wait_for(self.SUBCATEGORY_JEANS).click()
