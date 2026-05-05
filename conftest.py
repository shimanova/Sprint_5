import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from config import BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit()