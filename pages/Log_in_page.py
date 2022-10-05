from pages.base_page import BasePage
from locator.login_in_locator import LoginPageLocator


class LoginPage(BasePage):
    def open_login(self):
        log_in_button = self.find_element(LoginPageLocator.LOCATOR_LOG_IN_BUTTON)
        log_in_button.click()
    def login(self, email, passwd):
        email_field = self.find_element(LoginPageLocator.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)
        passwd_field = self.find_element(LoginPageLocator.LOCATOR_PASSWD_FIELD)
        passwd_field.send_keys(passwd)
        sing_in_button = self.find_element(LoginPageLocator.LOCATOR_SING_IN_BUTTON)
        sing_in_button.click()

