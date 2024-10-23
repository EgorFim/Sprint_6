import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Тест на появление окна о создании заказа')
    @allure.description('Создаем заказ и проверяем наличие окна')
    def test_okno_uspeshnogo_sozdaniya_zakaza(self,driver_2):
        main_page = MainPage(driver_2)
        order_page = OrderPage(driver_2)
        main_page.knopka_zakazat_header_click()
        order_page.make_order()
        assert order_page.proverka_sozdaniya_zakaza()

    @allure.title('Тест на появление окна о создании заказа')
    @allure.description('Создаем заказ и проверяем наличие окна')
    def test_okno_uspeshnogo_sozdaniya_zakaza_2(self,driver_2):
        main_page = MainPage(driver_2)
        order_page = OrderPage(driver_2)
        main_page.knopka_zakazat_middle_click()
        order_page.make_order()
        assert order_page.proverka_sozdaniya_zakaza()
        