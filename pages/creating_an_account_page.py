from pages.base_page import BasePage
from locator.creating_an_account_locator import CreatingAccountPageLocator
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options



class CreatingAccountPage(BasePage):
    def open_creating_account_page(self):
        continue_creating_button = self.find_element(CreatingAccountPageLocator.
                                                     LOCATOR_CONTINUE_CREATING_BUTTON)
        continue_creating_button.click()
        auth_text = self.find_element(CreatingAccountPageLocator.
                                      LOCATOR_CREATING_ACCOUNT_PAGE_TEXT).text
        check_text = 'Register Account'
        assert auth_text == check_text, f'{auth_text} is not eq {check_text}'


    def creating_account_1(self, first_name, last_name):

        first_name_field = self.find_element(CreatingAccountPageLocator.LOCATOR_FIRST_NAME)
        first_name_field.send_keys(first_name)
        last_name_field = self.find_element(CreatingAccountPageLocator.LOCATOR_LAST_NAME)
        last_name_field.send_keys(last_name)



    def creating_account_2(self,email, telephone, fax, company, address,
                               city, zip_code):
        email_field = self.find_element(CreatingAccountPageLocator.LOCATOR_E_MAIL)
        email_field.send_keys(email)
        telephone_field = self.find_element(CreatingAccountPageLocator.LOCATOR_TELEPHONE)
        telephone_field.send_keys(telephone)
        fax_field = self.find_element(CreatingAccountPageLocator.LOCATOR_FAX)
        fax_field.send_keys(fax)
        company_field = self.find_element(CreatingAccountPageLocator.LOCATOR_COMPANY)
        company_field.send_keys(company)
        address_field = self.find_element(CreatingAccountPageLocator.LOCATOR_ADDRESS)
        address_field.send_keys(address)
        city_field = self.find_element(CreatingAccountPageLocator.LOCATOR_CITY)
        city_field.send_keys(city)
        zip_code_field = self.find_element(CreatingAccountPageLocator.LOCATOR_ZIP_CODE)
        zip_code_field.send_keys(zip_code)
        sleep(2)
        country_field = self.find_element(CreatingAccountPageLocator.LOCATOR_COUNTRY)
        country_field.click()
        sleep(5)
        # region_field = self.find_element(CreatingAccountPageLocator.LOCATOR_REGION)
        # region_field.click()
        # country_field_florida = self.find_element(CreatingAccountPageLocator.LOCATOR_REGION_CHOICE)
        # country_field_florida.click()
        # select = self.find_element_by_tag_name("country_id")
        # select.select_by_value("FLORIDA") # ищем элемент с текстом "FLORIDA"
        # select.click()


    def creating_account_3(self, password, confirm_password):
        password_field = self.find_element(CreatingAccountPageLocator.LOCATOR_PASSWORD)
        password_field.send_keys(password)
        confirm_password_field = self.find_element(CreatingAccountPageLocator.LOCATOR_CONFIRM_PASSWORD)
        confirm_password_field.send_keys(confirm_password)


        # sing_in_button = self.find_element(LoginPageLocator.LOCATOR_SING_IN_BUTTON)
        # sing_in_button.click()
#
#
# class LoginPage(BasePage):
#
#     def should_be_login_page(self):
#         self.login_form_is_present()
#         self.auth_text_is_present()
#
#     def login_form_is_present(self):
#         self.find_element(LoginPageLocator.LOCATOR_LOGIN_FORM)
#
#     def auth_text_is_present(self):
#         auth_text = self.find_element(LoginPageLocator.LOCATOR_AUTH_TEXT).text
#         check_text = 'Вход'
#         assert auth_text == check_text, f'{auth_text} is not eq {check_text}'
#
#     def login(self, email, passwd):
#         email_field = self.find_element(LoginPageLocator.LOCATOR_EMAIL_FIELD)
#         email_field.send_keys(email)
#         sleep(2)
#         passwd_field = self.find_element(LoginPageLocator.LOCATOR_PASSWD_FIELD)
#         passwd_field.send_keys(passwd)
#         sleep(2)
#         # remember_me = self.find_element(LoginPageLocator.LOCATOR_REMEMBER_ME)
#         # remember_me.click()
#         sing_in_button = self.find_element(LoginPageLocator.LOCATOR_SING_IN_BUTTON)
#         sing_in_button.click()
#
#     def click_registration_applicant_button(self):
#         registration_applicant_button = self.find_element(
#             LoginPageLocator.LOCATOR_REGISTRATION_APPLICANT_BUTTON
#         )
#         registration_applicant_button.click()