from seleniumbase import BaseCase

class CartPage(BaseCase):
    cart_form = 'form[id="js-form"] div'

    def is_product_added_to_cart(self):
        self.assert_element(self.cart_form)
