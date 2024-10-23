import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    TEST_URL = 'https://qa-scooter.praktikum-services.ru/'
    driver.get(TEST_URL)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ZAGRUZKA_GLAVNOI))
    yield driver
    driver.quit()

@pytest.fixture
def driver_2():
    driver = webdriver.Firefox()
    TEST_URL = 'https://qa-scooter.praktikum-services.ru/'
    driver.get(TEST_URL)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ZAGRUZKA_GLAVNOI))
    yield driver
    driver.quit()