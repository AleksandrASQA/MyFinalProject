import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class GrillPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://www.onlinetrade.ru/catalogue/aerogrili-c1145/kitfort/aerogril_kitfort_kt_2263-4591425.html'  # страница гриля

    # Locators
    code = '//div[@class="catalog__displayedItem__storeCode "]' # локатор кода товара
    name = '//h1[@itemprop="name"]'                             # локатор названия товара
    price = '//span[@itemprop="price"]'                         # локатор цены товара
    buy_button = '//a[@href="/basket.html?add=3289080"]'        # локатор кнопки "Купить"
    continue_shopping = '//a[@title="Продолжить покупки"]'      # локатор кнопки "Продолжить покупки"

    # Getters
    def get_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.code)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_continue_shopping(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_shopping)))


    # Actions
    def info_product(self):
        code = self.get_code().text                 # присваиваем переменной текстовое значение локатора кода товара
        name = self.get_name().text                 # присваиваем переменной текстовое значение локатора названия товара
        price = self.get_price().text               # присваиваем переменной текстовое значение локатора цены товара
        return code, name, price                    # возвращаем текстовые значеия кода, названия и цены товара

    def click_buy_button(self):
        self.get_buy_button().click()
        time.sleep(2)
        print('Нажимаем кнопку "Купить"')

    def click_continue_shopping(self):
        self.get_continue_shopping().click()
        time.sleep(2)
        print('Кликаем "Продолжить покупки"')


    # Methods
    def about_grill(self):
        with allure.step("About grill"):
            Logger.add_start_step(method='about_grill')         # начало логгирования
            self.get_current_url()                              # отображаем url открытой страницы
            info = self.info_product()                          # сохраняем в переменную список значений: код, название и цену товара
            self.click_buy_button()                             # кликаем на кнопку "Купить"
            self.click_continue_shopping()                      # нажимаем на кнопку "Продолжить покупки"
            Logger.add_end_step(url=self.driver.current_url, method='about_grill')  # конец логгирования
            return info                                         # возвращаем код, имя и цену товара

