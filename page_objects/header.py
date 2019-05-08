from seleniumbase import BaseCase

class Header(BaseCase):
    my_account_icon = '#my-account'
    logout_link = 'a[href="/accounts/logout/"]'
    search_field = 'input[name="search"]'
    search_button = 'button[type="submit"]'

    def is_logged_in(self):
        self.click(self.my_account_icon)
        self.assert_element(self.logout_link)
        self.assert_text('Logout', self.logout_link)

    def search(self, search_string = 'kit'):
        self.update_text(self.search_field, search_string)
        self.click(self.search_button)