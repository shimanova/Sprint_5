from selenium.webdriver.common.by import By

class AuthLocators:
    LOGIN_REG_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    CREATE_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@name='submitPassword']")
    
    USER_AVATAR = (By.XPATH, "//h3[@class='profileText name']")
    ERROR_MESSAGE = (By.XPATH, "//span[@class='input_span__yWPqB']")

class AdLocators:
    ADD_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'modal')]//h1")
    NEXT_ARROW = (By.XPATH, "//button[contains(@class, 'arrowButton--right')]")
    
    TITLE_FIELD = (By.XPATH, "//input[@name='name']")
    DESCRIPTION_FIELD = (By.XPATH, "//textarea[@name='description']")
    PRICE_FIELD = (By.XPATH, "//input[@name='price']")
    
    CONDITION_NEW = (By.XPATH, "//label[contains(text(), 'Новый')]")