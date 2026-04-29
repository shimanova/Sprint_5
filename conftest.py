import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.education-services.ru/")
    driver.wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit()