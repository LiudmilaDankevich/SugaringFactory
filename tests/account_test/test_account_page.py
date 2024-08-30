from pages.Log_in_page import LoginPage
from pages.account_page import AccountPage


class TestAccountPage:
    def test_open_account_page(self, browser, create_user_and_login):
        account_page = AccountPage(browser)
        account_page.should_be_account_page()
