from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait




class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = 'https://test.sugaringfactory.com/'

    def open_base_page(self):
        self.driver.get(self.base_page)
    def find_element(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f'Can not find element {locator}')

    def find_elements(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f'Can not find element {locator}')

    def element_is_visible(self, locator, timeout=1):
        return Wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    # def pytest_html_report_title(report):
    #     report.title = "REPORT"
    # def select_by_value(self,"text"):
    #     self.driver.get(self.base_page)





