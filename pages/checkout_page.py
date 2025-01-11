from selenium.webdriver.common.by import By
from pages.base_page import Common_Methods

class Checkout_Page:

    def __init__(self, driver):
        self.driver = driver
        self.customer_name_in_address = (By.XPATH, "//ul[@id='address_delivery']/li[@class='address_firstname address_lastname']")
        self.ordr_msg = (By.XPATH, "//div[@id='ordermsg']//textarea[@name='message']")
        self.place_order_btn = (By.XPATH, "//a[text()='Place Order']")

        self.common = Common_Methods(self.driver)
    
    def get_customer_name_in_address(self):
        self.common.wait_for_element(self.customer_name_in_address)
        return self.driver.find_element(*self.customer_name_in_address).text

    def enter_order_msg(self, msg):
        self.driver.find_element(*self.ordr_msg).send_keys(msg)
    
    def click_on_place_order_btn(self):
        self.common.wait_for_clickable(self.place_order_btn)
        self.driver.find_element(*self.place_order_btn).click()