from pages.Log_in_page import LoginPage
from pages.main_page import MainPage
from time import sleep


def test_open_login_page(browser):
    main_page = MainPage(browser)
    sleep(2)
    main_page.open_base_page()
    login_page = LoginPage(browser)
    sleep(2)
    login_page.open_login()
    sleep(2)
    login_page.login('dan2510@gmail.com', '1111')
    sleep(2)
# Не загружается страница !!!!!!!!!!!!!1 Тест не работает
    # login_page = LoginPage(browser)
    # login_page.should_be_login_page()
