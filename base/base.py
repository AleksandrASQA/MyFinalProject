import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод проверки url"""

        get_url = self.driver.current_url
        print("Текущий url: " + get_url)

    def assert_word(self, word, result):
        """Проверка значения текста"""

        value_word = word.text
        print('Заголовок страницы: ', value_word)
        assert value_word == result
        print("Текстовое значение заголовка верно")

    def get_screenshot(self):
        """Снятие скриншота"""

        now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
        name_screenshot = "screenshot " + now_date + ".png"
        print('Screenshot: ', self.driver.save_screenshot(f"screen/{name_screenshot}"))

    def assert_url(self, result):
        """Проверка значения url"""

        get_url = self.driver.current_url
        assert get_url == result
        print("Значение url совпадает")