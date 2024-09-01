import requests
from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import Select
import json
import os.path

from urllib3 import request

from pages.main_page import MainPage
from pages.Log_in_page import LoginPage
from recources.api.user_api import create_user_api
from pages.creating_an_account_page import CreatingAccountPage

#путь к файлу с тестовыми данными
def load_config(file_path):
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
    with open(config_path) as f:
        target = json.load(f)
    return target

@pytest.fixture()
def browser(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://test.sugaringfactory.com/')
    # Делает скриншоты упавших тестов в момент ошибки
    failed_before = request.session.testsfailed
    yield driver
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        take_screenshot(driver, test_name)
    driver.quit()

@pytest.fixture()
def user_config_data():
    config_data = load_config("recources/variables/user_data.json")
    return config_data["first_name"], config_data["last_name"]


# фикстура создает пользователя и сразу авторизуется под ним
@pytest.fixture()
def create_user_and_login(browser):
    email, password = create_user_api(browser)
    main_page = MainPage(browser)
    main_page.should_be_main_page()
    main_page.open_login()
    main_page.should_be_login_page()
    login_page = LoginPage(browser)
    login_page.login(email, password)

# Путь куда нужно сохранить скриншот
def take_screenshot(browser, test_name):
    screenshot_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "failure_screenshots")
    screenshot_file_path = f"{screenshot_dir}/{test_name}.png"
    browser.save_screenshot(screenshot_file_path)
