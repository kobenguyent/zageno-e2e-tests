from seleniumbase import BaseCase

class CatalogPage(BaseCase):
    view_and_buy = 'a div[class="btn btn--slim product-item__cta-buy"]'

    def select_a_product(self):
        self.click(self.view_and_buy)
