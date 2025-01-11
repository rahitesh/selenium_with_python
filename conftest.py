import pytest

from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("http://automationexercise.com")
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()