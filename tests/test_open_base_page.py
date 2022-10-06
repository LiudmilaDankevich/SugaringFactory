from pages.main_page import MainPage
from pages.Log_in_page import LoginPage
from time import sleep


def test_open_main_page(browser):
    main_page = MainPage(browser)
    sleep(2)
    main_page.open_base_page()
    sleep(2)
    main_page.should_be_main_page()


# def test_click_sing_in_button(browser):
#     login_page = LoginPage(browser)
#     sleep(2)
#     login_page.login()


# def test_buy_ducks_in_the_store(browser):
#     main_page = MainPage(browser)
#     main_page.open_base_page()
#     login_page = LoginPage(browser)
#     login_page.login('dan2510@gmail.com', '1111')
    # duck = RubberDuckPage(browser)
    # duck.choose_duck()
    # duck.change_the_number_of_duck('3')
    # duck.click_add_to_cart()
    # duck.click_cart()
    # sleep(1)
    # cart_page = CartPage(browser)
    # cart_page.should_be_quantity_duck()
    # # cart_page.should_be_cost_duck()
    # cart_page.click_confirm_order()
    # # База данных не проходит в дженкинсе, тест падает
    # # connect = DataBase()
    # # connect.check_order_by_id()

