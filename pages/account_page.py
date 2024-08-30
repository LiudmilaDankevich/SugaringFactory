from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.Log_in_page import LoginPage
from pages.creating_an_account_page import CreatingAccountPage
from locator.main_page_locator import MainPageLocator
from locator.login_in_locator import LoginPageLocator
from locator.creating_an_account_locator import CreatingAccountPageLocator

class AccountPage(BasePage):
    def should_be_account_page(self):
        self.account_page_text_is_present()

    def account_page_text_is_present(self):
        auth_text = self.find_element(LoginPageLocator.LOCATOR_MY_ACCOUNT_IS_PRESENT).text
        check_text = 'My Account'
        assert auth_text == check_text, f'{auth_text} is not eq {check_text}'