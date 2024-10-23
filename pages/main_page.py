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
    def knopka_zakazat_header_click(self):
         return self.click_to_element(MainPageLocators.KNOPKA_ZAKAZAT_HEADER)

    @allure.step('Нажимаем кнопку "Заказать" в середине страницы')
    def knopka_zakazat_middle_click(self):
        self.scroll_to_element(MainPageLocators.KNOPKA_ZAKAZAT_MIDDLE)
        return self.click_to_element(MainPageLocators.KNOPKA_ZAKAZAT_MIDDLE)

    @allure.step('Нажимаем кнопку "Самокат" в хедере')
    def samokat_header_button_click(self):
        self.click_to_element(MainPageLocators.KNOPKA_SAMOKAT)

    @allure.step('Нажимаем кнопку "Яндекс" в хедере')
    def knopka_yandex_click(self):
        self.click_to_element(MainPageLocators.KNOPKA_YANDEX)

    @allure.step('Проверяем переход на страницу Дзен')
    def perehod_na_stranicu_dzen(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.find_element_with_wait(MainPageLocators.YANDEX_DZEN_PROVERKA)




