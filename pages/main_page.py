from pages.base_page import BasePage
from locator.main_page_locator import MainPageLocator



class MainPage(BasePage):
    def should_be_main_page(self):
        self.main_page_text_is_present()

# def find_job_form_is_present(self):
#     self.find_element(MainPageLocator.LOCATOR_FIND_JOB_FORM)
#
    def main_page_text_is_present(self):
        auth_text = self.find_element(MainPageLocator.LOCATOR_MAIN_PAGE_TEXT).text
        check_text = 'Learn Why'
        assert auth_text == check_text, f'{auth_text} is not eq {check_text}'
#
#
    def click_sing_in_button(self):
        sing_in_button = self.find_element(
            MainPageLocator.LOCATOR_SING_IN_BUTTON
        )
        sing_in_button.click()

    # def confirm_alert(self):
    #     confirm = self.find_element(MainPageLocator.LOCATOR_CONFIRM_ALERT)
    #     #confirm.accept()
    #     confirm.dismiss()
    # def click_registration_applicant_button(self):
    #     registration_applicant_button = self.find_element(
    #         MainPageLocator.LOCATOR_REGISTRATION_APPLICANT_BUTTON
    #     )
    #     registration_applicant_button.click()
