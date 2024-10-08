from pages.main_page import MainPage
from time import sleep
from pages.creating_an_account_page import CreatingAccountPage
from pages.Log_in_page import LoginPage
from locator.creating_an_account_locator import CreatingAccountPageLocator

class TestCreatingAccount:

    def test_creating_an_account(self,browser, user_config_data):
        # main_page = MainPage(browser)
        # main_page.open_base_page()
        first_name, last_name = user_config_data
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        login_page.open_login()
        account_page = CreatingAccountPage(browser)
        account_page.open_creating_account_page()
        account_page.creating_account_1(first_name,last_name)
        account_page.creating_account_2('Dankevich7923@gmail.com',
                                   '+375297774477', '+375297734472', 'RVT',
                                     'Zudro 5-47', 'Minsk', '10001')
        sleep(5)
        account_page.creating_account_3('12345', '12345')
        account_page.newsletter_subscribe()






        # login_page = LoginPage(browser)
        # login_page.click_registration_applicant_button()
        # sleep(2)
        # registration_applicant_form = RegistrationApplicatorForm(browser)
        # registration_applicant_form.registration_of_the_applicant(
        #     'Anna', 'Born', 'Born@gmail.com', '1111'
        # )