from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import Select



@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()