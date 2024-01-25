import time
import pytest
from selenium.webdriver.common.by import By



from pageobjects.homepage import Homepage
from testdata.homepagedata import Homepagedata
from utilities.baseclass import Baseclass


class Testhomepage(Baseclass):

    def test_formsubmission(self, getdata):

        homepage = Homepage(self.driver)
        homepage.getname().send_keys(getdata["firstname"])
        homepage.getmail().send_keys(getdata["email"])
        homepage.getpassword().send_keys("65432")
        homepage.checkme().click()
        self.select_by_text(homepage.select_gender(), getdata["gender"])
        homepage.click_submit().click()
        msg = homepage.grasp_text().text
        print(msg)
        assert "Success" in msg
        time.sleep(2)
        self.driver.refresh()


    @pytest.fixture(params=Homepagedata.test_homepage_data)
    def getdata(self, request):
        return request.param
