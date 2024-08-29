from pages.Log_in_page import LoginPage
from pages.main_page import MainPage
from time import sleep


def test_open_login_page(browser):
    main_page = MainPage(browser)
    main_page.should_be_main_page()
    main_page.open_login()
    main_page.should_be_login_page()

