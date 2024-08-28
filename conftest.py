from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import Select
import json
import os.path

def load_config(file_path):
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),file_path)
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
    config_data = load_config("resources/variables/user_data.json")
    return config_data["first_name"], config_data["last_name"]