import time
from selenium import webdriver
from pages.basket_page import BasketPage
from pages.grill_page import GrillPage
from pages.smartphones_page import SmartphonesPage
from pages.start_page import StartPage


def test_buy_phone():
    options = webdriver.ChromeOptions()
    options.add_argument('log-level=3')             # скрытие ошибок сертификата
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    print('Start test')
    start = StartPage(driver)                       # создаем экземпляр класса StartPage
    start.select_product_from_slider()              # запускаем метод класса StartPage

    grill = GrillPage(driver)                       # создаем экземпляр класса GrillPage
    info_1 = grill.about_grill()                    # запускаем метод класса GrillPage
    driver.back()                                   # возвращаемся на главную страницу

    smart = SmartphonesPage(driver)                 # создаем экземпляр класса SmartphonesPage
    info_2 = smart.do_smartphones_page()            # запускаем метод класса SmartphonesPage

    basket = BasketPage(driver)                     # создаем экземпляр класса BasketPage
    basket.check_basket_page(info_1, info_2)        # запускаем метод класса BasketPage

    print('Finish test')
    time.sleep(5)




