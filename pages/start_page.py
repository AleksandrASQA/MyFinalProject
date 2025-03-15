import time
import allure
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
    accept_cookie = '//a[contains(text(), "Принять")]'              # локатор кнопки "Принять" во всплывающем окне
    personal_account = '//span[@class="ic__set ic__set__member"]'   # локатор личного кабинета
    email = '//input[@id="ajax_login_popup_email"]'                 # локатор поля почты
    password = '//input[@id="ajax_login_popup_pass"]'               # локатор поля пароля
    button_enter = '//input[@name="submit"]'                        # локатор кнопки "Вход"
    first_slider_slide = '//span[@aria-label="Go to slide 1"]'      # локатор 1 слайда в первом слайдере
    grill = '//a[contains(text(), "Аэрогриль Kitfort КТ-2263")]'    # локатор ссылки на товар

    # Getters
    def get_accept_cookie(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_cookie)))

    def get_personal_account(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_account)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_enter)))

    def get_first_slider_slide(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_slider_slide)))

    def get_grill(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.grill)))

    # Actions
    def click_accept_cookie(self):
        self.get_accept_cookie().click()
        print('Нажимаем на кнопку "Принять куки"')

    def enter_in_personal_account(self):
        self.get_personal_account().click()             # открываем окно входа в личный кабинет
        self.get_email().send_keys('bayers00@mail.ru')  # вводим почту
        self.get_password().send_keys('Ar6nTA3Em3a')    # вводим пароль
        self.get_button_enter().click()                 # кликаем на кнопку "Вход"
        print('Нажимаем на кнопку "Вход"')

    def find_grill(self):
        for i in range(2, 26):
            try:
                self.get_first_slider_slide().click()
                time.sleep(2)
                print('Ищем в первом слайде товар "Гриль"')
                self.get_grill().click()
                time.sleep(2)
                print('Открываем страницу товара "Гриль"')
                break
            except:
                first_slider_slide = f'//span[@aria-label="Go to slide {i}"]'


    # Methods
    def select_product_from_slider(self):
        with allure.step("Select product from slider"):
            Logger.add_start_step(method='select_product_from_slider')  # начало логгирования
            self.driver.get(self.url)                                 # открываем наш url
            self.driver.maximize_window()                             # раскрываем страницу на весь экран
            self.get_current_url()                                    # отображаем текущий url адрес
            self.click_accept_cookie()                                # принимаем куки
            self.enter_in_personal_account()                          # авторизуемся на сайте
            self.find_grill()                                         # ищем слайд с аэрогрилем и открываем его страницу
            Logger.add_end_step(url=self.driver.current_url, method='select_product_from_slider')  # конец логгирования
