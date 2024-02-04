import pytest
from src.pages.home_page import Home
from pytest_check import check
import time


@pytest.mark.usefixtures("driver")
class TestAllProductsSearch:
    def test_home_page_visible(self, driver):
        home_page = Home(driver)
        assert "Automation" in home_page.home_title_text(), "'Home' page is not displayed!"

    def test_products_page_visible(self, driver):
        products_page = Home(driver).get_products_page()
        # time to remove pop-ups and ads manually
        time.sleep(10)
        assert "ALL PRODUCTS" in products_page.get_products_title_text(), " 'Products' page is not displayed!"

    def test_products_search_performed_successfully(self, driver):
        products_page = Home(driver).get_products_page()
        products_page.enter_search_criteria_and_perform_search('TOPS')
        assert "SEARCHED PRODUCTS" in products_page.get_products_title_text(), " The title for search results wasn't changed after filtering!"

    def test_all_searched_products(self, driver):
        products_page = Home(driver).get_products_page()

        products_page.enter_search_criteria_and_perform_search('Jeans')
        # time to remove pop-ups and ads manually
        time.sleep(10)
        products_text = products_page.get_searched_product_items()
        for product_text in products_text:
            with check:
                assert 'Jeans' in product_text, f"The product {product_text} doesn't match the search criteria!"
