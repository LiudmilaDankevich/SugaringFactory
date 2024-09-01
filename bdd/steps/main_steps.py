from pytest_bdd import given, when, then
from pages.main_page import MainPage

@given('open main page')
def open(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    pass