from src.pages.home_page import Home
from pytest_check import check
import time


class TestAllProductsSearch:
    def test_products_page_visible(self, web_browser):
        home_page = Home(web_browser)
        assert "Automation" in home_page.home_title_text(), "'Home' page is not displayed!"

        products_page = home_page.get_products_page()
        # time to remove pop-ups and ads manually
        time.sleep(10)
        assert "ALL PRODUCTS" in products_page.get_products_title_text(), " 'Products' page is not displayed!"

    def test_products_search_performed_successfully(self, web_browser):
        products_page = Home(web_browser).get_products_page()
        products_page.enter_search_criteria_and_perform_search('TOPS')
        assert "SEARCHED PRODUCTS" in products_page.get_products_title_text(), " The title for search results wasn't changed after filtering!"

    def test_all_searched_products(self, web_browser):
        products_page = Home(web_browser).get_products_page()
        products_page.enter_search_criteria_and_perform_search('Jeans')
        # time to remove pop-ups and ads manually
        time.sleep(10)
        products_text = products_page.get_searched_product_items()
        for product_text in products_text:
            with check:
                assert 'Jeans' in product_text, f"The product {product_text} doesn't match the search criteria!"
