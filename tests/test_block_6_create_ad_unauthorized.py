from selenium.webdriver.support import expected_conditions as EC
from locators.locators import AdLocators

class TestBlock6CreateAdUnauthorized:
    
    def test_create_ad_unauthorized(self, driver):
        driver.wait.until(EC.element_to_be_clickable(AdLocators.ADD_AD_BUTTON)).click()
        
        modal_title = driver.wait.until(EC.visibility_of_element_located(AdLocators.MODAL_TITLE))
        
        assert "авторизуйтесь" in modal_title.text.lower()