from page_objects.floating_cookies import FloatingCookies
from page_objects.header import Header
from page_objects.cart import CartPage
from page_objects.catalog import CatalogPage
from page_objects.product_details import ProductDetailsPage
from page_objects.register import RegisterPage

class ShoppingTests(RegisterPage, FloatingCookies, Header, CartPage, CatalogPage, ProductDetailsPage):

    def test_search_and_add_a_product_to_cart(self):
        self.go_to_register_page()
        FloatingCookies.accept_cookies(self)
        self.register()
        Header.search(self)
        CatalogPage.select_a_product(self)
        ProductDetailsPage.add_to_cart(self)
        CartPage.is_product_added_to_cart(self)
