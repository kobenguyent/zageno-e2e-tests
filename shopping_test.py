from page_objects.login import LoginPage
from page_objects.floating_cookies import FloatingCookies
from page_objects.header import Header
from page_objects.home import HomePage
from page_objects.cart import CartPage
from page_objects.catalog import CatalogPage
from page_objects.product_details import ProductDetailsPage

class ShoppingTests(LoginPage, FloatingCookies, Header, HomePage, CartPage, CatalogPage, ProductDetailsPage):

    def test_add_a_product_on_home_page(self):
        self.go_to_home_page()
        FloatingCookies.accept_cookies(self)
        self.login()
        Header.is_logged_in(self)
        HomePage.add_to_cart(self)
        CartPage.is_product_added_to_cart(self)

    def test_search_and_add_a_product_to_cart(self):
        self.go_to_login_page()
        FloatingCookies.accept_cookies(self)
        self.login()
        Header.search(self)
        CatalogPage.select_a_product(self)
        ProductDetailsPage.add_to_cart(self)
        CartPage.is_product_added_to_cart(self)
