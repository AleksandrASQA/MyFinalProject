import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class BasketPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    basket = '//h1[contains(text(), "Корзина")]'            # локатор заголовка "Корзина"
    code1 = '(//span[@class="descriptionLine__item"])[1]'   # локатор кода первого товара
    code2 = '(//span[@class="descriptionLine__item"])[2]'   # локатор кода второго товара
    name1 = '(//a[@class="semibold"])[1]'                   # локатор названия первого товара
    name2 = '(//a[@class="semibold"])[2]'                   # локатор названия второго товара
    price1 = '(//b[@class="nowrap"])[1]'                    # локатор цены первого товара
    price2 = '(//b[@class="nowrap"])[2]'                    # локатор цены второго товара
    total_price = '//b[@class="size18 medium"]'             # локатор итоговой цены
    # Getters
    def get_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket)))

    def get_code1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.code1)))

    def get_code2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.code2)))

    def get_name1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name1)))

    def get_name2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name2)))

    def get_price1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price1)))

    def get_price2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price2)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    # Actions
    def check_first_product(self, info):
        value_code1 = self.get_code1().text                             # получаем значение кода первого товара
        value_name1 = self.get_name1().text                             # получаем значение названия первого товара
        value_price1 = self.get_price1().text                           # получаем значение цены первого товара
        assert value_code1 == info[0]                                   # сравниваем значение кода первого товара
        print(value_code1)
        print('Код первого товара совпадает')
        assert value_name1 == info[1]                                   # сравниваем значение имени первого товара
        print('Название первого товара: ', value_name1)
        print('Имя первого товара совпадает')
        assert value_price1.replace(' ₽', '') == info[2]    # сравниваем значение цены первого товара
        print('Цена первого товара: ', value_price1)
        print('Цена первого товара совпадает')

    def check_second_product(self, info):
        value_code2 = self.get_code2().text                             # получаем значение кода второго товара
        value_name2 = self.get_name2().text                             # получаем значение названия второго товара
        value_price2 = self.get_price2().text                           # получаем значение цены второго товара
        assert value_code2 == info[0]                                   # сравниваем значение кода второго товара
        print(value_code2)
        print('Код второго товара совпадает')
        assert value_name2 == 'Смартфон ' + info[1]                     # сравниваем значение имени второго товара
        print('Название второго товара: ', value_name2)
        print('Имя второго товара совпадает')
        assert value_price2 == info[2]                                  # сравниваем значение цены второго товара
        print('Цена второго товара: ', value_price2)
        print('Цена второго товара совпадает')

    def check_total_price(self, price1, price2):
        result = int(price1.replace(' ', '')) + int(price2.replace(' ₽', '').replace(' ', ''))   # строчные значения цен форматируем и преобразуем в числовой тип
        value_total_price = self.get_total_price().text                                          # получаем строчное значение локатора итоговой суммы
        print('Итоговая цена: ', value_total_price)
        assert result == int(value_total_price.replace(' ₽', '').replace(' ', ''))  # сравниваем значения, предварительно отформатировав строковое значение и преобразовав его в числовой тип
        print('Итоговая цена совпадает')

    # Methods
    def check_basket_page(self, info1, info2):
        with allure.step("Check basket page"):
            Logger.add_start_step(method='check_basket_page')           # начало логгирования
            self.get_current_url()                                      # отображаем url открытой страницы
            self.assert_word(self.get_basket(), 'Корзина')        # сравниваем значение локатора заголовка со строкой "Корзина"
            self.check_first_product(info1)                             # проводим проверку значений первого товара
            self.check_second_product(info2)                            # проводим проверку значений второго товара
            self.check_total_price(info1[2], info2[2])                  # сравниваем итоговую цену с суммой цен двух товаров
            self.get_screenshot()                                       # делаем скриншот и сохраняем его в папку screen
            Logger.add_end_step(url=self.driver.current_url, method='check_basket_page')    # конец логгирования

