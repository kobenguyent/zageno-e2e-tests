from page_objects.login import LoginPage
from page_objects.floating_cookies import FloatingCookies
from page_objects.header import Header
from pytest_testrail.plugin import pytestrail

class LoginTests(LoginPage, FloatingCookies, Header):

    @pytestrail.case('C1')
    def test_login_with_valid_credentials(self):
        self.go_to_login_page()
        FloatingCookies.accept_cookies(self)
        self.login()
        Header.is_logged_in(self)
