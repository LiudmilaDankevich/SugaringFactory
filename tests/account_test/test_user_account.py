from pages.creating_an_account_page import CreatingAccountPage
from pages.main_page import MainPage
from pages.Log_in_page import LoginPage





def test_account_is_display(browser, create_user_and_login):
    # main_page = MainPage(browser)
    # login_page = LoginPage(browser)
    # login_page.open_login()
    # login_page.login(email= email, password= password)
    account_page = CreatingAccountPage(browser)
    account_page.open_creating_account_page()
