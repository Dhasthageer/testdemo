from selenium.webdriver.common.by import By



class Homepage:

    def __init__(self, driver):
        self.driver = driver

    def shopitems(self):
        return self.driver.find_element(By.LINK_TEXT, "Shop")

    def getname(self):
        return self.driver.find_element(By.NAME, "name")
    def getmail(self):
        return self.driver.find_element(By.NAME, "email")
    def getpassword(self):
        return self.driver.find_element(By.ID, "exampleInputPassword1")
    def checkme(self):
        return self.driver.find_element(By.ID, "exampleCheck1")
    def select_gender(self):
        return self.driver.find_element(By.ID, "exampleFormControlSelect1")
    def click_submit(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[value='Submit']")

    def grasp_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[class$='dismissible']")



















