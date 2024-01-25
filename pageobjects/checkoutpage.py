import time

from selenium.webdriver.common.by import By


class Checkoutpage:

    def __init__(self, driver):
        self.driver = driver


    def find_products(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")


    def click_blackberry_button(self):
        products = self.find_products()
        time.sleep(3)
        for product in products:
            product_name = product.find_element(By.CSS_SELECTOR, "div h4").text

            if product_name == "Nokia Edge":
                product.find_element(By.CSS_SELECTOR, " button").click()
                break

    def checkout_verfication(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[class~='btn']").click()

        return self.driver.find_element(By.XPATH, "//tr[3]/td[5]/button[@type = 'button']").click()


