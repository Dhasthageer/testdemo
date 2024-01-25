from pageobjects.checkoutpage import Checkoutpage
from pageobjects.confirmpage import Confirmpage
from pageobjects.homepage import Homepage
from utilities.baseclass import Baseclass


class Test_Example(Baseclass):

    def test_end_2_end(self):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        homepage.shopitems().click()
        log.info("clicking the shop button in the homepage")
        checkoutpage = Checkoutpage(self.driver)
        checkoutpage.click_blackberry_button()
        log.info("select the required(Nokia Edge) product in the list")
        checkoutpage.checkout_verfication()
        log.info("checkout the required producted selected or not")

        confirmpage = Confirmpage(self.driver)
        confirmpage.entering_country("india")
        log.info("entering country name in the edit box")
        self.verify_link_presence("div[class='suggestions'] ul li a")
        log.info("wait has been implemented until the link presence")
        confirmpage.click_purchase_button()
        message = confirmpage.verfication_on_submission().text
        log.info(message)
        log.info("grasping the text after clicking the purchase button")
        assert "Success" or "success" in message















