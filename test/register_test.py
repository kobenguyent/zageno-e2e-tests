from page_objects.register import RegisterPage
from page_objects.floating_cookies import FloatingCookies

class RegisterTests(RegisterPage, FloatingCookies):

    def test_register_new_user(self):
        self.go_to_register_page()
        FloatingCookies.accept_cookies(self)
        self.register()
