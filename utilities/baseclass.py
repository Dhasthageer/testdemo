import inspect

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import logging
import inspect

@pytest.mark.usefixtures("setup")
class Baseclass:

    def getlogger(self):

        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("loger.log")
        formatter = logging.Formatter("%(asctime)s : %(name)s  : %(levelname)s  %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger



    def verify_link_presence(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, locator))).click()


    def select_by_text(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

