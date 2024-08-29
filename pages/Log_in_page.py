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

