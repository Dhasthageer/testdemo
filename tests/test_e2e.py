import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utilities.BaseClass import BaseClass

class Testone(BaseClass):

    def test_e2e(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, "Shop").click()
        products = self.driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")
        for product in products:
            product_name = product.find_element(By.CSS_SELECTOR, "div div h4 a").text
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "//button[text()='Add ']").click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()

        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
        self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='India']")))
        self.driver.find_element(By.XPATH, "//a[text()='India']").click()
        self.driver.find_element(By.CSS_SELECTOR, "div label[for*='checkbox2']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()
        message = self.driver.find_element(By.XPATH, "//strong").text
        assert "Success" in message















