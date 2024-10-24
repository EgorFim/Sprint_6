import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from selenium import webdriver
from data import test_url



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(test_url)
    yield driver
    driver.quit()

@pytest.fixture
def driver_2():
    driver = webdriver.Firefox()
    driver.get(test_url)
    yield driver
    driver.quit()