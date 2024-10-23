import allure

from pages.main_page import MainPage
import pytest
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators

class TestHeaderLogo:
    @allure.title('Тест на проверку корректной работы кнопки "Самокат" в лого')
    @allure.description('Проверяем после клика на кнопку "Самокат" переход на главную страницу')
    def test_samokat_button(self,driver_2):
        main_page = MainPage(driver_2)
        main_page.knopka_zakazat_header_click()
        main_page.samokat_header_button_click()
        assert main_page.find_element_with_wait(MainPageLocators.ZAGRUZKA_GLAVNOI)
    @allure.title('Тест на проверку корректной работы кнопки "Яндекс" в лого')
    @allure.description('Проверяем после клика открытие в новой странице сайт Дзена')
    def test_dzen_button(self,driver_2):
        main_page = MainPage(driver_2)
        main_page.knopka_yandex_click()
        assert main_page.perehod_na_stranicu_dzen()



