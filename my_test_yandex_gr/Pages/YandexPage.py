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

from selenium.webdriver.common.keys import Keys


class YandexPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_line_id = 'text'

    def search_text(self, company_name):
        self.driver.find_element_by_id(self.search_line_id).clear()
        self.driver.find_element_by_id(self.search_line_id).send_keys(company_name)

    def search_element_by_id(self, element_id):
        self.driver.find_element_by_xpath(element_id)

    def search_element_by_xpath(self, element_xpath):
        self.driver.find_element_by_xpath(element_xpath)

    def search_element_by_css(self, element_css):
        self.driver.find_elements_by_css_selector(element_css)

    def element_xpath_click(self, element_xpath):
        self.driver.find_element_by_xpath(element_xpath).click()

    def send_my_keys(self, element_xpath):
        self.driver.find_element_by_xpath(element_xpath).send_keys(Keys.LEFT)

    def get_src_of_pic(self, element_xpath):
        self.driver.find_element_by_xpath(element_xpath).get_attribute("src")

    def get_src_of_href(self, element_xpath):
        self.driver.find_element_by_xpath(element_xpath).get_attribute("href")
