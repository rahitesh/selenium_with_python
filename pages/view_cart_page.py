from selenium.webdriver.common.by import By
from pages.base_page import Common_Methods

class ViewCart_Page:
    
    def __init__(self, driver):
        self.driver= driver
        self.proceed_checkout_btn = (By.XPATH, "//a[text()='Proceed To Checkout']")

        self.common = Common_Methods(driver)

    def is_proceed_to_checkout_visible(self):
        self.common.wait_for_element(self.proceed_checkout_btn)
        return self.driver.find_element(*self.proceed_checkout_btn).is_displayed()
    
    def click_on_procced_to_checkout_button(self):
        self.driver.find_element(*self.proceed_checkout_btn).click()