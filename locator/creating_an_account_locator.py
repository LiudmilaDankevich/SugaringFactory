from selenium.webdriver.common.by import By


class CreatingAccountPageLocator:
    LOCATOR_CONTINUE_CREATING_BUTTON = (By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div[2]/a')
    LOCATOR_CREATING_ACCOUNT_PAGE_TEXT = (By.XPATH, '//*[@id="content"]/h1')
    LOCATOR_FIRST_NAME = (By.XPATH, '//*[@id="register"]/div[1]/table/tbody/tr[1]/td/div/div/input')
    LOCATOR_LAST_NAME = (By.XPATH, '//*[@id="register"]/div[1]/table/tbody/tr[2]/td/div/div/input')
    LOCATOR_E_MAIL = (By.XPATH, '//*[@id="register"]/div[1]/table/tbody/tr[3]/td/div/div/input')
    LOCATOR_TELEPHONE = (By.XPATH,'//*[@id="register"]/div[1]/table/tbody/tr[4]/td/div/div/input')
    LOCATOR_FAX = (By.XPATH,'// *[ @ id = "register"] / div[1] / table / tbody / tr[5] / td / div / div / input')
    LOCATOR_COMPANY = (By.XPATH,'//*[@id="register"]/div[2]/table/tbody/tr[2]/td/div/div/input')
    LOCATOR_ADDRESS = (By.XPATH,'//*[@id="register"]/div[2]/table/tbody/tr[6]/td/div/div/input')
    LOCATOR_CITY = (By.XPATH,'//*[@id="register"]/div[2]/table/tbody/tr[8]/td/div/div/input')
    LOCATOR_ZIP_CODE = (By.XPATH,'//*[@id="register"]/div[2]/table/tbody/tr[9]/td/div/div/input')
    LOCATOR_COUNTRY = (By.XPATH,'//*[@id="register"]/div[2]/table/tbody/tr[10]/td/div/div/select//div')
    LOCATOR_REGION = (By.XPATH,'//*[@id="register"]/div[2]/table/tbody/tr[11]/td/div/div/select//div')
    LOCATOR_PASSWORD = (By.XPATH,'//*[@id="register"]/div[3]/table/tbody/tr[1]/td/div/div/input')
    LOCATOR_CONFIRM_PASSWORD = (By.XPATH,'//*[@id="register"]/div[3]/table/tbody/tr[2]/td/div/div/input')
    LOCATOR_SUBSCRIBE_YES = (By.XPATH,'//*[@id="register"]/div[4]/table/tbody/tr/td/div/div/label[1]/input')
    LOCATOR_SUBSCRIBE_NO = (By.XPATH,'//*[@id="register"]/div[4]/table/tbody/tr/td/div/div/label[2]/input')
    LOCATOR_CODE_CAPTCHA = (By.XPATH,'//*[@id="register"]/input')
    LOCATOR_CONTINUE_REGISTRATION_BUTTON = (By.XPATH,'//*[@id="register"]/div[5]/div/a/span')
