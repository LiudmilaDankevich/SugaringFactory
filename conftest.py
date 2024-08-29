from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import Select
import json
import os.path
from pages.main_page import MainPage
from pages.Log_in_page import LoginPage
from pages.creating_an_account_page import CreatingAccountPage


def load_config(file_path):
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
    with open(config_path) as f:
        target = json.load(f)
    return target

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get('https://test.sugaringfactory.com/')
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture()
def user_config_data():
    config_data = load_config("recources/variables/user_data.json")
    return config_data["first_name"], config_data["last_name"]

@pytest.fixture()
def create_user_and_login(browser):
    email, password = create_user_api()
    main_page = MainPage(browser)
    main_page.should_be_main_page()
    main_page.open_login()
    main_page.should_be_login_page()
    login_page = LoginPage(browser)
    login_page.open_login()
    login_page.login(email, password)
