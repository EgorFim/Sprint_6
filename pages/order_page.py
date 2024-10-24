import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import name,street,surname,tel_number
from data import name_2,street_2,surname_2,tel_number_2

class OrderPage(BasePage):

    @allure.step('Заполняем поля оформления')
    def make_order(self):
        self.click_to_element(OrderPageLocators.POLE_NAME)
        self.add_text_to_element(OrderPageLocators.POLE_NAME, name)
        self.click_to_element(OrderPageLocators.POLE_SURNAME)
        self.add_text_to_element(OrderPageLocators.POLE_SURNAME, surname)
        self.click_to_element(OrderPageLocators.POLE_ADRESS)
        self.add_text_to_element(OrderPageLocators.POLE_ADRESS, street)
        self.click_to_element(OrderPageLocators.OPEN_SPISOK_METRO)
        self.click_to_element(OrderPageLocators.STATION_1)
        self.click_to_element(OrderPageLocators.POLE_TEL)
        self.add_text_to_element(OrderPageLocators.POLE_TEL, tel_number)
        self.click_to_element(OrderPageLocators.ORDER_KNOPKA_DALEE)
        self.find_element_with_wait(OrderPageLocators.VTORAYA_STRANICA_ORDER)
        self.click_to_element(OrderPageLocators.KOGDA_PRIVEZTI_OKNO)
        self.click_to_element(OrderPageLocators.OKNO_DATY)
        self.click_to_element(OrderPageLocators.OKNO_SROK_ARENDY)
        self.click_to_element(OrderPageLocators.KOLICHESTVO_SUTOK)
        self.click_to_element(OrderPageLocators.KNOPKA_ZAKAZAT_FINAL)

    @allure.step('Заполняем поля оформления')
    def make_order_2(self):
        self.click_to_element(OrderPageLocators.POLE_NAME)
        self.add_text_to_element(OrderPageLocators.POLE_NAME, name_2)
        self.click_to_element(OrderPageLocators.POLE_SURNAME)
        self.add_text_to_element(OrderPageLocators.POLE_SURNAME, surname_2)
        self.click_to_element(OrderPageLocators.POLE_ADRESS)
        self.add_text_to_element(OrderPageLocators.POLE_ADRESS, street_2)
        self.click_to_element(OrderPageLocators.OPEN_SPISOK_METRO)
        self.click_to_element(OrderPageLocators.STATION_2)
        self.click_to_element(OrderPageLocators.POLE_TEL)
        self.add_text_to_element(OrderPageLocators.POLE_TEL, tel_number_2)
        self.click_to_element(OrderPageLocators.ORDER_KNOPKA_DALEE)
        self.find_element_with_wait(OrderPageLocators.VTORAYA_STRANICA_ORDER)
        self.click_to_element(OrderPageLocators.KOGDA_PRIVEZTI_OKNO)
        self.click_to_element(OrderPageLocators.OKNO_DATY)
        self.click_to_element(OrderPageLocators.OKNO_SROK_ARENDY)
        self.click_to_element(OrderPageLocators.KOLICHESTVO_SUTOK)
        self.click_to_element(OrderPageLocators.KNOPKA_ZAKAZAT_FINAL)

    @allure.step('Проверяем появления окна о создании заказа')
    def check_create_order(self):
        return self.find_element_with_wait(OrderPageLocators.PROVERKA_ZAKAZ_OFORMLEN)








