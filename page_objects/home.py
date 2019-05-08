from seleniumbase import BaseCase

class HomePage(BaseCase):
    add_to_cart_button = 'button[id="js-add-to-cart"]'

    def go_to_home_page(self):
        self.open("https://internet:oureurekatime16@staging.zageno.com/")

    def add_to_cart(self):
        self.click(self.add_to_cart_button)
