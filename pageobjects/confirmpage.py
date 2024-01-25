import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Confirmpage:

    def __init__(self, driver):
        self.driver = driver

    def entering_country(self, text):
        return self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys(text)
    def click_purchase_button(self):
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']/a").click()
        self.driver.find_element(By.XPATH, "//button[text()='Close']").click()
        time.sleep(3)
        return self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

    def verfication_on_submission(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[class~='alert']")



