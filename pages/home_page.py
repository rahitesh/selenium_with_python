from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Common_Methods

class Home_Page():
    def __init__(self, driver):
        self.driver = driver
        self.signup_btn = (By.CSS_SELECTOR, ".fa.fa-lock")
        self.logged_in_user = (By.XPATH, "//a[contains(text(), 'Logged in as')]/b")
        self.first_product = (By.XPATH, "//img[@src = '/get_product_picture/1']")
        self.continue_shopping_btn = (By.XPATH,  "//button[text()='Continue Shopping']")
        self.cart_link = (By.XPATH, "//a[text()=' Cart']")

        self.action = ActionChains(self.driver)
        self.common = Common_Methods(self.driver)

    def click_on_signup_Btn(self):
        self.common.wait_for_clickable(self.signup_btn)
        self.driver.find_element(*self.signup_btn).click()
    
    def get_logged_in_user_name(self):
        self.common.wait_for_element(self.logged_in_user)
        return self.driver.find_element(*self.logged_in_user).text
    
    def add_first_product_in_cart(self):
        self.common.wait_for_element(self.first_product)
        first_product_element = self.driver.find_element(*self.first_product)
        self.action.move_to_element(first_product_element).perform()
        self.driver.find_element(By.XPATH, "//img[@src = '/get_product_picture/1']/parent::div/following-sibling::div[@class='product-overlay']/div/a").click()

    def click_continue_shopping_btn(self):
        self.common.wait_for_clickable(self.continue_shopping_btn)
        self.driver.find_element(*self.continue_shopping_btn).click()  

    def click_on_cart_button(self):
        self.common.wait_for_element(self.cart_link)
        self.driver.find_element(*self.cart_link).click() 

