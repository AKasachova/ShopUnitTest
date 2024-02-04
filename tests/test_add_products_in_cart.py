import pytest
from src.pages.home_page import Home
from src.pages.products_page import Products
from src.pages.view_cart_page import ViewCart
import time



@pytest.mark.usefixtures("driver")
class TestAddProductsInCart:
    def test_home_page_visible(self, driver):
        home_page = Home(driver)
        assert "Automation" in home_page.home_title_text(), "'Home' page is not displayed!"

    def test_category_page_is_displayed(self, driver):
        Home(driver).get_products_page()
        # time to remove pop-ups and ads manually
        time.sleep(5)
        Products(driver).find_first_product_and_add_to_cart()
        Products(driver).click_continue_shopping_button()
        Products(driver).find_second_product_and_add_to_cart()
        Products(driver).click_view_cart_link()
        cart_page = ViewCart(driver)
        assert "Blue Top" in cart_page.get_first_product_description_text() and "Men Tshirt" in cart_page.get_second_product_description_text(), \
            "Added product(s) is(are) not displayed in the Cart!"
        assert "Rs. 500" in cart_page.get_first_product_price_text(), "The first product hasn't appropriate price!"
        assert "Rs. 400" in cart_page.get_second_product_price_text(), "The second product hasn't appropriate price!"
        assert "1" in cart_page.get_first_product_quantity_text(), "The first product hasn't appropriate quantity!"
        assert "1" in cart_page.get_second_product_quantity_text(), "The second product hasn't appropriate quantity!"
        assert "Rs. 500" in cart_page.get_first_product_total_price_text(), "The first product hasn't appropriate total price!"
        assert "Rs. 400" in cart_page.get_second_product_total_price_text(), "The second product hasn't appropriate total price!"
