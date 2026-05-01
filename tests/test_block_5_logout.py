from selenium.webdriver.support import expected_conditions as EC
from locators.locators import AuthLocators

class TestBlock5Logout:
    
    def test_successful_logout(self, driver):
        driver.wait.until(EC.element_to_be_clickable(AuthLocators.LOGIN_REG_BUTTON)).click()
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys("test_user_1777652630767@test.ru")
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys("000000")
        driver.wait.until(EC.element_to_be_clickable(AuthLocators.LOGIN_BUTTON)).click()
        driver.wait.until(EC.visibility_of_element_located(AuthLocators.USER_AVATAR))
        
        driver.find_element(*AuthLocators.LOGOUT_BUTTON).click()
        
        driver.wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_REG_BUTTON))
        login_button = driver.find_element(*AuthLocators.LOGIN_REG_BUTTON)
        
        assert login_button.is_displayed()