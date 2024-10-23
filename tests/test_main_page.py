import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import ANSWER_1,ANSWER_2,ANSWER_3,ANSWER_4,ANSWER_5,ANSWER_6,ANSWER_7,ANSWER_8
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:
    @pytest.mark.parametrize(
        'num,result',
        [
            (0,ANSWER_1),
            (1,ANSWER_2),
            (2,ANSWER_3),
            (3,ANSWER_4),
            (4,ANSWER_5),
            (5,ANSWER_6),
            (6,ANSWER_7),
            (7,ANSWER_8)
        ]
    )
    @allure.title('Тест на соответствие вопросов и ответов на странице')
    @allure.description('Кликаем по очереди на вопросы и смотрим соответствуют ли ответы')
    def test_question_and_answers(self,driver_2,num,result):
        main_page = MainPage(driver_2)
        assert main_page.get_answer_text(num) == result


    @allure.title('Тест кнопки заказать в хэдэре страницы')
    @allure.description('Кликаем по кнопке и ждем что откроется окно заказа')
    def test_knopka_zakazat_header(self, driver):
        main_page = MainPage(driver)
        main_page.knopka_zakazat_header_click()
        assert main_page.find_element_with_wait(MainPageLocators.OKNO_ZAKAZA)

    @allure.title('Тест кнопки заказать в середине страницы')
    @allure.description('Кликаем по кнопке и ждем что откроется окно заказа')
    def test_knopka_zakazat_middle(self, driver):
        main_page = MainPage(driver)
        main_page.knopka_zakazat_middle_click()
        assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.OKNO_ZAKAZA))
