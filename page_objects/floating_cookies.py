from seleniumbase import BaseCase

class FloatingCookies(BaseCase):
    accept_cookies_button = 'input[value="Agree and Proceed"]'

    def accept_cookies(self):
        self.click(self.accept_cookies_button)
