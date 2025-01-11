import pytest

from pages.home_page import Home_Page
from pages.signup_page import Signup_Page
from pages.view_cart_page import ViewCart_Page
from pages.checkout_page import Checkout_Page




def test_login_before_checkout(setup):
    driver = setup
    home_page = Home_Page(driver)
    signup_page = Signup_Page(driver)
    view_cart_page = ViewCart_Page(driver)
    checkout_page = Checkout_Page(driver)

    home_page.click_on_signup_Btn()
    signup_page.enter_login_email_address("titu1@gmail.com")
    signup_page.enter_login_password("Bestbuy")
    signup_page.click_on_login_button()
    current_logged_in_user = home_page.get_logged_in_user_name()
    assert current_logged_in_user == "titu"
    home_page.add_first_product_in_cart()
    home_page.click_continue_shopping_btn()
    home_page.click_on_cart_button()
    assert view_cart_page.is_proceed_to_checkout_visible() == True
    view_cart_page.click_on_procced_to_checkout_button()
    name_of_customer = checkout_page.get_customer_name_in_address()
    assert name_of_customer == "Mr. titu tata"
    checkout_page.enter_order_msg("Place Order")
    checkout_page.click_on_place_order_btn()



