import pytest
from src.pages.home_page import Home
from src.pages.category_page import Category
import time


@pytest.mark.usefixtures("driver")
class TestViewCategoryProducts:
    def test_categories_are_visible(self, driver):
        home_page = Home(driver)
        assert 'CATEGORY' in home_page.get_category_title_text() and 'WOMEN' in home_page.get_category_women_title_text(), \
            "Categories title or options are not visible!"

    def test_category_page_is_displayed(self, driver):
        home_page = Home(driver)
        home_page.scroll_to_kids_title_text()
        home_page.click_category_women()
        home_page.click_category_dress()
        category_page = Category(driver)
        # time to remove pop-ups and ads manually
        time.sleep(10)
        assert 'WOMEN - DRESS PRODUCTS' in category_page.get_category_title_text(), "Category page (Women category, dress subcategory) is not visible!"

        category_page.click_category_men()
        category_page.click_subcategory_jeans()
        # time to remove pop-ups and ads manually
        time.sleep(10)
        assert 'MEN - JEANS PRODUCTS' in category_page.get_category_title_text(), "Category page (Men category, jeans subcategory) is not visible!"