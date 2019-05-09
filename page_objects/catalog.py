from seleniumbase import BaseCase

class CatalogPage(BaseCase):
    view_and_buy_button = 'div[class="product-item__info-cta"] a div[class="btn btn--slim product-item__cta-buy"]'

    def select_a_product(self):
        self.find_element(self.view_and_buy_button, timeout=6).click()
