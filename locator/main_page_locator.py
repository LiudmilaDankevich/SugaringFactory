from selenium.webdriver.common.by import By

class MainPageLocator:
    # LOCATOR_SING_IN_BUTTON = (By.LINK_TEXT, 'Вход и регистрация')
    LOCATOR_FIND_JOB_FORM = (
        By.NAME, "search[query]")
    LOCATOR_MAIN_PAGE_TEXT = (By.LINK_TEXT, 'Learn Why')
    LOCATOR_LOG_IN_BUTTON = (By.CSS_SELECTOR, '#header > div:nth-child(1) > div.top-menu-desktop > a.menu-item._login')
    LOCATOR_LOG_IN_TEXT = (By.CSS_SELECTOR, '#content > h1')


    # LOCATOR_REGISTRATION_APPLICANT_BUTTON
    # LOCATOR_CONFIRM_ALERT = (By.XPATH, '/html/body/script[1]')
    # logo > a > img