from seleniumbase import BaseCase

class LoginPage(BaseCase):
    user_name_field = '#id_username'
    password_field = '#id_password'
    login_button = 'form[method="post"] input[type="submit"]'

    def go_to_login_page(self):
        self.open("https://internet:oureurekatime16@staging.zageno.com/accounts/login/?next=%2F")

    def login(self):
        self.update_text(self.user_name_field, 'peter.nguyentr@gmail.com')
        self.update_text(self.password_field, '12345678')
        self.click(self.login_button)
