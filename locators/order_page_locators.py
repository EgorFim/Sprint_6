from selenium.webdriver.common.by import By


class OrderPageLocators:

    POLE_NAME = By.XPATH, './/*[@placeholder="* Имя"]'
    #поле "Имя" в окне заказа
    POLE_SURNAME = By.XPATH, './/*[@placeholder="* Фамилия"]'
    #поле "Фамилия" в окне заказа
    POLE_ADRESS = By.XPATH, './/*[@placeholder="* Адрес: куда привезти заказ"]'
    #поле "Адрес" в окне заказа
    POLE_TEL = By.XPATH, './/*[@placeholder="* Телефон: на него позвонит курьер"]'
    #поле "Телефон" в окне заказа
    STATION_1 = By.XPATH, './/*[@value="1"]'
    #первая станция в списке метро
    STATION_2 = By.XPATH, './/*[@value="2"]'
    #вторая станция в списке метро
    OPEN_SPISOK_METRO = By.XPATH, './/*[@placeholder="* Станция метро"]'
    #поле выбора станции метро
    ORDER_KNOPKA_DALEE = By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    #кнопка далее, переход на второе окно заказа
    OZHIDANIE_OKNA_ZAKAZA = By.XPATH, './/*[text()="Для кого самокат"]'
    #ожидание первого окна заказа
    VTORAYA_STRANICA_ORDER = By.XPATH, './/*[text()="Про аренду"]'
    #ожидание второго окна заказа
    KOGDA_PRIVEZTI_OKNO = By.XPATH, './/*[@placeholder="* Когда привезти самокат"]'
    #окно когда привезти самокат
    OKNO_DATY = By.XPATH, 'html/body/div/div/div/div/div/div/div/div/div/div/div/div/div[@tabindex="0"]'
    #выпадающий календарь
    OKNO_SROK_ARENDY = By.XPATH, './/*[@class="Dropdown-placeholder"]'
    #поле срок аренды
    KOLICHESTVO_SUTOK = By.XPATH, './/*[text()="сутки"]'
    #выпадающий список аренды
    KNOPKA_ZAKAZAT_FINAL = By.XPATH, 'html/body/div/div/div/div/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    #кнопка заказать во втором окне
    OFORMIT_FINAL_DA = By.XPATH, './/*[text()="Да"]'
    #кнопка да в всплывающем окне
    PROVERKA_ZAKAZ_OFORMLEN = By.XPATH, './/*[@class="Order_ModalHeader__3FDaJ"]'
    #всплывающее окно об оформлении заказа

