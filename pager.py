import logger
from OzonDriver_inv import Driver, selenium_exceptions
from timeit import Timer
from logger import logged_func


class SearchPage(Driver):
    @logged_func
    def __init__(self, proxy=''):
        super().__init__(proxy=proxy)
        self.previously_detected = dict()

    @logged_func
    def search(self):
        pass

    @logged_func
    def result(self):
        pass




