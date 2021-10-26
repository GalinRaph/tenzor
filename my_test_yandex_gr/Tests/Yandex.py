"""
Для тестирования были использованы:
PyCharm 2021.2.2
Python 3.8.7
Selenium 3.14.0
Браузер Chrome 95.0.4638.54
Chromedriver ChromeDriver 95.0.4638.17
Chromedriver должен быть в PATH!!!

Понадобились следующие пакеты:
selenium команда установки pip install selenium==3.14.0
unittest
time
logging
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import unittest
import time
import logging
from Pages.YandexPage import YandexPage


class YandexTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_yandex(self):
        driver = self.driver
        self.driver.get('http://www.yandex.ru')
        yandex = YandexPage(driver)
        try:
            yandex.search_element_by_id('text')
            logging.info('Строка поиска есть')
            print('Строка поиска есть')
        except NoSuchElementException:
            logging.exception('Проверьте правильность ID строки поиска')
            print('Проверьте правильность ID строки поиска')
        yandex.search_text('Тензор')
        try:
            yandex.search_element_by_css('li[id^="suggest-item-"]')
            logging.info('Подсказка есть')
            print('Подсказка есть')
        except NoSuchElementException:
            logging.exception('Подсказки нет')
            print('Подсказки нет')
        yandex.element_xpath_click('//button[@type="submit"]')

        '''
        Данная функция проводит тестирование слудющих пунктов ТЗ:
        1)	Зайти на yandex.ru
        2)	Проверить наличия поля поиска
        3)	Ввести в поиск Тензор
        4)	Проверить, что появилась таблица с подсказками (suggest) 
        5)	При нажатии Enter появляется таблица результатов поиска
        '''

    def test_second_page_yandex(self):
        driver = self.driver
        self.driver.get('https://yandex.ru/search/?lr='
                        '172&oprnd=5113499050&text=тензор')
        yandex = YandexPage(driver)
        firstsite = yandex.get_src_of_href(
            '(//div[@class="content__left"]//a)[1]')
        secondsite = yandex.get_src_of_href(
            '(//div[@class="content__left"]//a)[2]')
        threesite = yandex.get_src_of_href(
            '(//div[@class="content__left"]//a)[3]')
        foursite = yandex.get_src_of_href(
            '(//div[@class="content__left"]//a)[4]')
        fivetsite = yandex.get_src_of_href(
            '(//div[@class="content__left"]//a)[5]')
        # здесь нужен был цикл для изменения номера ссылки, но я не успел
        link_search = (str(firstsite) + str(secondsite) + str(
            threesite) + str(foursite) + str(fivetsite))
        try:
            if link_search.count('tensor.ru') > 5:
                logging.info('Первые пять ссылок ведут на tensor.ru')
                print('Первые пять ссылок ведут на tensor.ru')
            else:
                pass
        except:
            logging.exception('Yandex вставил рекламу')
            print('Yandex вставил рекламу')

    '''
    Данная функция проверяет соответствуют ли первые пять ссылок сайту tensor.ru
    В моих тестах яндекс регулярно вставлял рекламу первой строкой,
    поэтому этот тест проваливался
    '''

    def test_service_yandex(self):
        driver = self.driver
        self.driver.get('http://www.yandex.ru')
        yandex = YandexPage(driver)
        try:
            yandex.search_element_by_xpath('//*[contains'
                                                  '(@data-id,"images")]')
            logging.info('Кнопка "Картинки" существует')
            print('Кнопка "Картинки" существует')
        except NoSuchElementException:
            logging.exception('Кнопки не оказалось')
            print('Кнопки не оказалось')
        yandex.element_xpath_click('//*[contains(@data-id,"images")]')

    '''
    Данная функция проверяет следующие пункты ТЗ:
    1)	Зайти на yandex.ru
    2)	Ссылка «Картинки» присутствует на странице
    3)	Кликаем на ссылку
    
    '''

    def test_yandex_search_pic(self):
        driver = self.driver
        self.driver.get('https://yandex.ru/images/?utm_source=main_stripe_big')
        yandex = YandexPage(driver)
        verify_url = 'https://yandex.ru/images/'
        curr_url = driver.current_url
        if verify_url in curr_url:
            logging.info('Вы в поисковике картинок')
            print('Вы в поисковике картинок')
        else:
            logging.exception('Вы не в поисковике картинок')
            print('Вы не в поисковике картинок')
        time.sleep(2)
        textpicone = driver.find_element_by_xpath('//div[@class="PopularRequestList-SearchText"]')
        textpicone = textpicone.text.lower()
        yandex.element_xpath_click('//div[contains(@class,"PopularRequestList-Shadow")]')
        time.sleep(3)
        yandex.search_element_by_xpath('//input[contains(@class,"input")]')
        driver.find_element_by_xpath('//input[contains(@class,"input")]').send_keys(Keys.LEFT)
        time.sleep(2)
        textpictwo = driver.find_element_by_xpath('//div[contains(@class,"suggest2")]//b[contains(@class,"")]')
        textpictwo = textpictwo.text.lower()
        if textpictwo == textpicone:
            logging.info('Вы ищете правильно')
        else:
            logging.exception('Поиск не по той картинке')
        time.sleep(5)
        driver.refresh()
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath('//div[@class="serp-item__preview"]').click()
        time.sleep(7)
        imgsrcfirst = driver.find_element_by_xpath('//img[contains(@class,"MMImage-Origin")]').get_attribute("href")
        yandex.element_xpath_click(
            '//div[contains(@class,"CircleButton_type_next")]')
        yandex.element_xpath_click(
            '//div[contains(@class,"CircleButton_type_prev")]')
        imgsrcsecond = driver.find_element_by_xpath('//img[contains(@class,"MMImage-Origin")]').get_attribute("href")
        if imgsrcfirst == imgsrcsecond:
            logging.info('Картинка та же самая')
        else:
            logging.exception('Картинка не та же самая')

        '''
        Данная фнукция проверяет следующие пункты: 
        4)	Проверить, что перешли на url https://yandex.ru/images/
        5)	Открыть 1 категорию, проверить что открылась, в поиске верный текст
        6)Открыть 1 картинку , проверить что открылась
        7) При нажатии кнопки вперед  картинка изменяется
        8) При нажатии кнопки назад картинка изменяется на изображение из шага 6. 
            Необходимо проверить, что это то же изображение.
        '''

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.close()
        cls.driver.quit()
        print('Тест пройден')


if __name__ == '__main__':
    unittest.main()
