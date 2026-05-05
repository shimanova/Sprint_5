from selenium.webdriver.support import expected_conditions as EC
from locators.locators import AuthLocators
from utils.helpers import generate_unique_email

class TestBlock1Registration:
    
    def test_successful_registration(self, driver):
        driver.wait.until(EC.element_to_be_clickable(AuthLocators.LOGIN_REG_BUTTON)).click()
        driver.wait.until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        
        email = generate_unique_email()
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys("000000")
        driver.find_element(*AuthLocators.CONFIRM_PASSWORD_FIELD).send_keys("000000")
        
        driver.wait.until(EC.element_to_be_clickable(AuthLocators.CREATE_BUTTON)).click()
        
        driver.wait.until(EC.visibility_of_element_located(AuthLocators.USER_AVATAR))
        user_name = driver.find_element(*AuthLocators.USER_AVATAR).text
        
        assert "User" in user_name