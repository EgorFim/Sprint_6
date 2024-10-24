import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Тест на появление окна о создании заказа')
    @allure.description('Создаем заказ и проверяем наличие окна')
    def test_appearence_window_of_successful_create_order(self,driver_2):
        main_page = MainPage(driver_2)
        order_page = OrderPage(driver_2)
        main_page.button_zakazat_in_header_click()
        order_page.make_order()
        assert order_page.check_create_order()

    @allure.title('Тест на появление окна о создании заказа')
    @allure.description('Создаем заказ и проверяем наличие окна')
    def test_appearance_window_of_successful_create_order_2(self,driver_2):
        main_page = MainPage(driver_2)
        order_page = OrderPage(driver_2)
        main_page.button_zakazat_in_middle_click()
        order_page.make_order_2()
        assert order_page.check_create_order()
        