import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Получаем текст ответа')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(
            MainPageLocators.QUESTION_LOC, num)
        locator_a_formatted = self.format_locators(
            MainPageLocators.ANSWER_LOC, num)
        self.scroll_to_element(MainPageLocators.SCROLL_QUESTION_LOCATOR)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Нажимаем кнопку "Заказать" в хедере')
    def button_zakazat_in_header_click(self):
         return self.click_to_element(MainPageLocators.KNOPKA_ZAKAZAT_HEADER)

    @allure.step('Нажимаем кнопку "Заказать" в середине страницы')
    def button_zakazat_in_middle_click(self):
        self.scroll_to_element(MainPageLocators.KNOPKA_ZAKAZAT_MIDDLE)
        return self.click_to_element(MainPageLocators.KNOPKA_ZAKAZAT_MIDDLE)

    @allure.step('Нажимаем кнопку "Самокат" в хедере')
    def samokat_header_button_click(self):
        self.click_to_element(MainPageLocators.KNOPKA_SAMOKAT)

    @allure.step('Нажимаем кнопку "Яндекс" в хедере')
    def button_yandex_in_header_click(self):
        self.click_to_element(MainPageLocators.KNOPKA_YANDEX)

    @allure.step('Проверяем переход на страницу Дзен')
    def switch_to_dzen_page(self):
        self.switch_to_window()
        return self.find_element_with_wait(MainPageLocators.YANDEX_DZEN_PROVERKA)

    @allure.step('Проверяем загрузку главной страницы')
    def load_main_page(self):
        return self.find_element_with_wait(MainPageLocators.ZAGRUZKA_GLAVNOI)

    @allure.step('Проверяем переход к странице заказа')
    def switch_to_order_page(self):
        return self.find_element_with_wait(MainPageLocators.OKNO_ZAKAZA)




