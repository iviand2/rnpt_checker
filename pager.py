import time
import timeit

import logger
from OzonDriver_inv import Driver, selenium_exceptions
from selenium.webdriver.common.keys import Keys
from timeit import Timer
from logger import logged_func


class SearchPage(Driver):
    @logged_func
    def __init__(self, proxy=''):
        super().__init__(proxy=proxy, wait=20, inv=True)
        self.previously_detected = dict()

    @logged_func
    def search(self, value):
        res = {}
        timer = timeit.Timer()
        start = timer.timer()
        if self.driver.current_url == 'data:,':
            self.driver.get('https://www.nalog.gov.ru/rn77/service/traceability/#tab0')
        try:
            search_input = self.wait_clickable('input[class = "form-control mb-2 traceability_form_search"]')
        except:
            self.driver.get('https://www.nalog.gov.ru/rn77/service/traceability/#tab0')
            search_input = self.wait_clickable('input[class = "form-control mb-2 traceability_form_search"]')
        # search_input = self.driver.find_element(
        #     by='css selector',
        #     value='input[class = "form-control mb-2 traceability_form_search"]'
        # )
        # search_input.clear()
        # if search_input.is_enabled()
        try:
            search_input.send_keys(value)
        except selenium_exceptions.ElementNotInteractableException:
            self.driver.find_element('css selector', 'body').send_keys(Keys.PAGE_UP)
            time.sleep(20)
            search_input.send_keys(value)
        except Exception as ex:
            self.driver.save_screenshot('error.jpg')
            raise ex
        try:
            self.wait_clickable(
                'a#search-button'
            ).click()
        except selenium_exceptions.ElementClickInterceptedException:
            self.driver.save_screenshot('error.png')
            time.sleep(20)
            self.wait_clickable(
                'a#search-button'
            ).click()
        time.sleep(5)
        # self.invisible_wait('a[href="#tab1"]')
        # self.wait_clickable('input[class = "form-control mb-2 traceability_form_search"]')
        search_input.clear()
        try:
            res['tn_ved'] = self.driver.find_element(
                'css selector',
                'td[role="gridcell"] + td'
            ).text
        except (selenium_exceptions.NoSuchElementException, selenium_exceptions.TimeoutException):
            res['tn_ved'] = 'Не найдено'
        self.driver.find_element('css selector', 'body').send_keys(Keys.PAGE_UP)
        print(f'{value} - готово, {res} :: Затрачено времени - {timer.timer() - start}')
        return res

    @logged_func
    def result(self):
        pass




