from selenium.webdriver.support import expected_conditions as EC
from locators.locators import AuthLocators

class TestBlock4Login:
    
    def test_successful_login(self, driver):
        driver.wait.until(EC.element_to_be_clickable(AuthLocators.LOGIN_REG_BUTTON)).click()
        driver.wait.until(EC.presence_of_element_located(AuthLocators.EMAIL_FIELD))
        
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys("test_user_1777652630767@test.ru")
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys("000000")
        driver.wait.until(EC.element_to_be_clickable(AuthLocators.LOGIN_BUTTON)).click()
        
        driver.wait.until(EC.visibility_of_element_located(AuthLocators.USER_AVATAR))
        user_name = driver.find_element(*AuthLocators.USER_AVATAR).text
        
        assert "User" in user_name