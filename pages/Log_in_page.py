from pages.base_page import BasePage
from locator.login_in_locator import LoginPageLocator
from time import sleep


class LoginPage(BasePage):

    def open_login(self):
        log_in_button = self.find_element(LoginPageLocator.LOCATOR_LOG_IN_BUTTON)
        log_in_button.click()
    def login(self, email, password):
        email_field = self.find_element(LoginPageLocator.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)
        passwd_field = self.find_element(LoginPageLocator.LOCATOR_PASSWD_FIELD)
        passwd_field.send_keys(password)
        sing_in_button = self.find_element(LoginPageLocator.LOCATOR_SING_IN_BUTTON)
        sleep(5)
        sing_in_button.click()
        sleep(5)

    def should_be_user_page(self):
        self.user_page_text_is_present()

    def user_page_text_is_present(self):
        auth_text = self.find_element(LoginPageLocator.LOCATOR_MY_ACCOUNT_IS_PRESENT).text
        check_text = 'My Account'
        assert auth_text == check_text, f'{auth_text} is not eq {check_text}'

