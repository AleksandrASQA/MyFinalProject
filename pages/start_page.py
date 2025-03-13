import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class StartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://www.onlinetrade.ru/'  # url тестируемого сайта

    # Locators
    accept_cookie = '//a[contains(text(), "Принять")]'                                              # локатор кнопки "Принять" во всплывающем окне
    first_slider_slide6 = '//span[@aria-label="Go to slide 6"]'                                     # локатор 5 слайда в первом слайдере
    grill = '//a[@href="/catalogue/aerogrili-c1145/kitfort/aerogril_kitfort_kt_2263-4591425.html"]' # локатор ссылки на товар

    # Getters
    def get_accept_cookie(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_cookie)))

    def get_first_slider_slide6(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_slider_slide6)))

    def get_grill(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.grill)))


    # Actions
    def click_accept_cookie(self):
        self.get_accept_cookie().click()
        print("Нажимаем на кнопку 'Принять куки'")

    def open_grill(self):
        self.get_first_slider_slide6().click()
        time.sleep(2)
        print("В первом слайдере выбираем 6 слайд")
        self.get_grill().click()
        time.sleep(2)
        print('Открываем страницу товара "Гриль"')


    # Methods
    def select_product_from_slider(self):
        Logger.add_start_step(method='select_product_from_slider')          # начало логгирования
        self.driver.get(self.url)                                           # открываем наш url
        self.driver.maximize_window()                                       # раскрываем страницу на весь экран
        url = self.get_current_url()                                        # отображаем текущий url адрес и присваиваем переменной
        self.click_accept_cookie()                                          # принимаем куки
        self.open_grill()                                                   # открываем страницу гриля из 6 слайда в первом слайдере
        Logger.add_end_step(url=url, method='select_product_from_slider')   # конец логгирования


