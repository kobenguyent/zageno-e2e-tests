from seleniumbase import BaseCase

class ProductDetailsPage(BaseCase):
    add_to_cart_button = '#js-add-to-cart'

    def add_to_cart(self):
        self.click(self.add_to_cart_button)
