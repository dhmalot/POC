import pytest
import time

from Testing_POC.webpages.HomePage import HomePage
from Testing_POC.webpages.HomeLiving import HomeLiving
from Testing_POC.webpages.FloorLamp import FloorLamp
from Testing_POC.webpages.ProductDetails import ProductDetails


@pytest.mark.usefixtures("setup")
class TestSample:
    def test_check_browser_functionality(self):
        home_page = HomePage(self.driver)
        time.sleep(5)
        home_page.get_section_list() # for getting all the product category sections on home page
        home_page.click_home_and_living()
        home_living = HomeLiving(self.driver)
        # time.sleep(5)
        home_living.click_floor_and_lamps()
        floor_lamps = FloorLamp(self.driver)
        # time.sleep(5)
        parent_window = self.driver.title
        floor_lamps.select_and_click_product()

        product_page = ProductDetails(self.driver)
        time.sleep(5)

        product_page.get_discount_percentage()
        new_window = self.driver.title

        if parent_window != new_window:
            print("Product was opened in new window.")
        else:
            print("Testcase failed")

        product_page.click_wishlist()

        current_url = self.driver.current_url
        assert "login" in current_url


        # signin_ele = self.driver.find_element(*HomePage.signin_xpath)
        # print(signin_ele.get_attribute("textContent"))
