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
    LOCATOR_COUNTRY = (By.CSS_SELECTOR,'[name="country_id"]')
    LOCATOR_COUNTRY_NAME = (By.CSS_SELECTOR,' [name="country_id"] :nth-child(3)')
    LOCATOR_REGION = (By.CSS_SELECTOR,' [name="zone_id"] ')
    # LOCATOR_REGION_CHOICE = (By.XPATH,'//*[@id="register"]/div[2]/table/tbody/tr[11]/td/div/div/select/option[13]')
    LOCATOR_PASSWORD = (By.CSS_SELECTOR,'.q1[name="password"]')
    LOCATOR_CONFIRM_PASSWORD = (By.CSS_SELECTOR,'.q1[name="confirm"]')
    LOCATOR_SUBSCRIBE_YES = (By.CSS_SELECTOR,'#register > div:nth-child(8) > table '
                                             '> tbody > tr > td > div > div > '
                                             'label:nth-child(1) > input[type=radio]')
    # LOCATOR_SUBSCRIBE_YES = (By.CSS_SELECTOR, '[class="radio inline"][class="radio inline"]>[value*="1"]')
    LOCATOR_SUBSCRIBE_NO = (By.CSS_SELECTOR,'[class="radio inline"]>[value*="0"]')
    LOCATOR_CODE_CAPTCHA = (By.XPATH,'[name=captcha]')
    LOCATOR_CAPTCHA_IMAGE = (By.CSS_SELECTOR, '[src="index.php?route=account/register/captcha"] ')
    LOCATOR_CONTINUE_REGISTRATION_BUTTON = (By.CSS_SELECTOR,'[onclick*="submit();"]')
