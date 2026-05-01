import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import AuthLocators, AdLocators

class TestBlock7CreateAdAuthorized:
    
    def test_create_ad_authorized(self, driver):
        # 1. Авторизация
        driver.wait.until(EC.element_to_be_clickable(AuthLocators.LOGIN_REG_BUTTON)).click()
        driver.wait.until(EC.presence_of_element_located(AuthLocators.EMAIL_FIELD))
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys("test_user_1777652630767@test.ru")
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys("000000")
        driver.wait.until(EC.element_to_be_clickable(AuthLocators.LOGIN_BUTTON)).click()
        driver.wait.until(EC.visibility_of_element_located(AuthLocators.USER_AVATAR))
        
        # 2. Нажать «Разместить объявление»
        driver.wait.until(EC.element_to_be_clickable(AdLocators.ADD_AD_BUTTON)).click()
        
        # 3. Заполнить форму
        title = f"Ноутбук {int(time.time() * 1000)}"
        driver.find_element(*AdLocators.TITLE_FIELD).send_keys(title)
        driver.find_element(*AdLocators.DESCRIPTION_FIELD).send_keys("Отличное состояние")
        driver.find_element(*AdLocators.PRICE_FIELD).send_keys("25000")
        
        driver.find_element(*AdLocators.CONDITION_NEW).click()
        driver.find_element(*AdLocators.PUBLISH_BUTTON).click()
        
        # 4. Подождать, пока страница обновится, и НАЙТИ АВАТАР ЗАНОВО
        time.sleep(2)
        driver.wait.until(EC.visibility_of_element_located(AuthLocators.USER_AVATAR)).click()
        
        # 5. Проверить, что объявление появилось
        created_title = driver.wait.until(
            EC.visibility_of_element_located((By.XPATH, f"//div[contains(@class, 'card')]//h2[text()='{title}']"))
        )
        
        assert created_title.is_displayed()