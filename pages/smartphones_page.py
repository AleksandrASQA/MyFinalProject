import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class SmartphonesPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalogue = '//a[@href="/catalogue/"]'                                      # локатор кнопки "Каталог"
    link_smartphones = '//a[@href="/catalogue/smartfony-c13/"]'                 # локатор ссылки на "Смартфоны"
    in_detail = '//a[@class="ic__hasSet  ic__hasSet__goodsListingType_4 "]'     # локатор кнопки "подробно"
    diagonal = '//input[@id="diagonal2"]'                                       # локатор поля ввода значения диагонали
    brand = '//a[@title="INOI"]'                                                # локатор выделяемой кнопки бренда INOI
    show_products = '//a[@title="Показать товары по выбранным условиям"]'       # локатор кнопки "Показать"
    code_product = '//div[@class="indexGoods__item__storeCode"]'                # локатор кода продукта
    name_product = '//a[contains(text(), "INOI Note 13s 4/128GB Фиолетовый")]'  # локатор имени продукта
    price_product = '//span[@class="price js__actualPrice"]'                    # локатор цены продукта
    button_buy_product = '//a[@data-handler="buy"]'                             # локатор кнопки "Купить"
    place_an_order = '//a[@id="js__popup_addedToCart__cartLinkID"]'             # локатор кнопки "Оформить заказ"

    # Getters
    def get_catalogue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalogue)))

    def get_link_smartphones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_smartphones)))

    def get_in_detail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.in_detail)))

    def get_diagonal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.diagonal)))

    def get_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand)))

    def get_show_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_products)))

    def get_code_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.code_product)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_button_buy_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_buy_product)))

    def get_place_an_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.place_an_order)))

    # Actions
    def click_catalogue(self):
        self.get_catalogue().click()
        print('Нажимаем на кнопку "Каталог"')

    def click_get_link_smartphones(self):
        self.get_link_smartphones().click()
        print('Нажимаем на ссылку "Смартфоны"')

    def click_in_detail(self):
        self.get_in_detail().click()
        time.sleep(2)
        print('Меняем вид отображения товаров на "подробно"')

    def input_diagonal(self):
        self.get_diagonal().click()
        self.get_diagonal().clear()
        self.get_diagonal().send_keys('6.5')
        time.sleep(3)
        self.get_show_products().click()
        time.sleep(2)
        print('Задаём максимальное значение диагонали 6.5 и показываем результат')

    def click_brand(self):
        self.get_brand().click()
        print('Выбираем бренд "INOI"')

    def info_product(self):
        code = self.get_code_product().text         # присваиваем переменной текстовое значение локатора кода товара
        name = self.get_name_product().text         # присваиваем переменной текстовое значение локатора названия товара
        price = self.get_price_product().text       # присваиваем переменной текстовое значение локатора цены товара
        return code, name, price                    # возвращаем текстовые значеия кода, названия и цены товара

    def click_button_buy_product(self):
        self.get_button_buy_product().click()
        print('Нажимаем кнопку "Купить"')

    def click_place_an_order(self):
        self.get_place_an_order().click()
        print('Нажимаем кнопку "Оформить заказ"')

    # Methods
    def find_and_buy_smartphone(self):
        with allure.step("Find and buy smartphone"):
            Logger.add_start_step(method='find_and_buy_smartphone')         # начало логгирования
            self.get_current_url()                              # отображаем url открытой страницы
            self.assert_url('https://www.onlinetrade.ru/')      # сверяем url с изначальным адресом
            self.click_catalogue()                              # нажимаем на кнопку "Каталог"
            self.click_get_link_smartphones()                   # кликаем по ссылке 'Смартфоны'
            self.click_in_detail()                              # меняем вид отображение товаров на "подробно"
            self.input_diagonal()                               # кликаем в поле максимального значения диагонали, очищаем и вводим значение 6.5
            self.click_brand()                                  # выбираем бренд "INOI"
            info = self.info_product()                          # присваиваем переменной список значений: код, имя и цену товара
            self.click_button_buy_product()                     # кликаем по кнопке "Купить"
            self.click_place_an_order()                         # нажимаем "Оформить заказ"
            self.driver.refresh()                               # обновляем страницу, т.к. не авторизованы
            Logger.add_end_step(url=self.driver.current_url, method='find_and_buy_smartphone')  # конец логгирования
            return info                                         # возвращаем код, имя и цену товара


