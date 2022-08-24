from pages.main_page import MainPage
from time import sleep


def test_click_sing_in_button(browser):
    main_page = MainPage(browser)
    sleep(2)
    main_page.open_base_page()
    sleep(2)
    # main_page.should_be_main_page()


