from selenium.webdriver.common.by import By
from pages.base_page import Common_Methods

class Payment_Page:

    def __init__(self, driver):
        self.driver = driver
        self.name_of_card_holder_textbox = (By.NAME, "name_on_card")
        self.card_number_textbox = (By.NAME, "card_number")
        self.cvc_textbox = (By.NAME, "cvc")
        self.expiry_month_textbox = (By.NAME, "expiry_month")
        self.expiry_year_textbox = (By.NAME, "expiry_year")
        self.place_confirm_order_btn = (By.ID, "submit")
        self.payment_confirmation_msg = (By.XPATH, "//*[text()='Congratulations! Your order has been confirmed!']")
        self.continue_btn = (By.XPATH, "//a[@data-qa='continue-button']")

        self.common = Common_Methods(self.driver)
    
    def enter_card_holder_name(self, name):
        self.common.wait_for_element(self.name_of_card_holder_textbox)
        self.driver.find_element(*self.name_of_card_holder_textbox).send_keys(name)
    
    def enter_card_number(self, card_number):
        self.driver.find_element(*self.card_number_textbox).send_keys(card_number)
    
    def enter_cvc_number(self, cvc_num):
        self.driver.find_element(*self.cvc_textbox).send_keys(cvc_num)

    def enter_expiry_month(self, xmonth):
        self.driver.find_element(*self.expiry_month_textbox).send_keys(xmonth)
    
    def enter_expiry_year(self, xyears):
        self.driver.find_element(*self.expiry_year_textbox).send_keys(xyears)
    
    def click_on_place_confirm_order_button(self):
        self.driver.find_element(*self.place_confirm_order_btn).click()
    
    def get_payment_confirmation_msg(self):
        self.common.wait_for_element(self.payment_confirmation_msg)
        return self.driver.find_element(*self.payment_confirmation_msg).text

    def click_on_continue_button(self):
        self.driver.find_element(*self.continue_btn).click()
    
