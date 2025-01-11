from selenium.webdriver.common.by import By
from pages.base_page import Common_Methods

class Signup_Page()    :

    def __init__(self, driver):
        self.driver = driver
        self.signup_name_textbox = (By.NAME, "Name")
        self.login_email_textbox = (By.XPATH, "//input[@data-qa='login-email']")
        self.login_password_textbox = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_btn = (By.XPATH, "//button[@data-qa='login-button']")
        self.common = Common_Methods(self.driver)

    def enter_login_email_address(self, email_addr):
        self.common.wait_for_element(self.login_email_textbox)
        self.driver.find_element(*self.login_email_textbox).send_keys(email_addr)

    def enter_login_password(self, password):
        self.common.wait_for_element(self.login_password_textbox)
        self.driver.find_element(*self.login_password_textbox).send_keys(password)
    
    def click_on_login_button(self):
        self.common.wait_for_clickable(self.login_btn)
        self.driver.find_element(*self.login_btn).click()