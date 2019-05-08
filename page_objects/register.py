from seleniumbase import BaseCase
from faker import Faker

class RegisterPage(BaseCase):
    first_name_field = '#id_first_name'
    last_name_field = '#id_last_name'
    email_field = '#id_email'
    password_field = '#id_password1'
    repeat_password_field = '#id_password2'
    accept_privacy_checkbox = 'div[class="privacy-checkbox"] div'
    signup_button = 'input[type="submit"]'
    thank_you_popup = 'div[class="sweet-alert showSweetAlert visible"]'

    def go_to_register_page(self):
        self.open('https://internet:oureurekatime16@staging.zageno.com/signup/?next=%2F')

    def register(self):
        fake = Faker()
        full_name = fake.name().split(' ')
        default_password = '12345678'
        self.update_text(self.first_name_field, full_name[0])
        self.update_text(self.last_name_field, full_name[1])
        self.update_text(self.email_field, fake.email())
        self.update_text(self.password_field, default_password)
        self.update_text(self.repeat_password_field, default_password)
        self.click(self.accept_privacy_checkbox)
        self.click(self.signup_button)
        self.assert_element(self.thank_you_popup)