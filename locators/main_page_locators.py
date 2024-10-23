from selenium.webdriver.common.by import By


class MainPageLocators:
    KNOPKA_ZAKAZAT_HEADER = By.XPATH, './/*[@class="Button_Button__ra12g"]'
    #кнопка заказать в хедере
    KNOPKA_ZAKAZAT_MIDDLE = By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    #кнопка заказать в середине страницы
    ZAGRUZKA_GLAVNOI = By.XPATH, './/*[@class="Home_Header__iJKdX"]'
    #загрузка главной страницы
    QUESTION_LOC = By.XPATH, './/*[@id="accordion__heading-{}"]'
    #локатор вопросов
    ANSWER_LOC = By.XPATH, './/*[@id="accordion__panel-{}"]'
    #локатор ответов
    SCROLL_QUESTION_LOCATOR = By.XPATH, './/*[@id="accordion__heading-7"]'
    #скролл до последнего вопроса
    OKNO_ZAKAZA = By.XPATH, './/*[text()="Для кого самокат"]'
    #ожидание окна заказа
    KNOPKA_SAMOKAT = By.XPATH, './/*[@class="Header_LogoScooter__3lsAR"]'
    #кнопка самокат в хедере
    KNOPKA_YANDEX = By.XPATH, './/*[@class="Header_LogoYandex__3TSOI"]'
    #кнопка яндекс в хедере
    YANDEX_DZEN_PROVERKA = By.XPATH, './/*[@class="dzen-layout--navigation-tab__tabWrapper-3L"]'
    # проверка открытия страницы Дзена