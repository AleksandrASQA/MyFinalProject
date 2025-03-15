import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.basket_page import BasketPage
from pages.grill_page import GrillPage
from pages.smartphones_page import SmartphonesPage
from pages.start_page import StartPage


@allure.description("Test buy products")
def test_buy_products():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('log-level=3')             # скрытие ошибок сертификата
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Start test')
    start = StartPage(driver)                       # создаем экземпляр класса StartPage
    start.select_product_from_slider()              # запускаем метод класса StartPage

    grill = GrillPage(driver)                       # создаем экземпляр класса GrillPage
    info_1 = grill.about_grill()                    # запускаем метод класса GrillPage
    driver.back()                                   # возвращаемся на главную страницу

    smart = SmartphonesPage(driver)                 # создаем экземпляр класса SmartphonesPage
    info_2 = smart.find_and_buy_smartphone()        # запускаем метод класса SmartphonesPage

    basket = BasketPage(driver)                     # создаем экземпляр класса BasketPage
    basket.check_basket_page(info_1, info_2)        # запускаем метод класса BasketPage

    print('Finish test')
    driver.close()



