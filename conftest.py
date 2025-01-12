import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        print("Invalid browser Name")

    driver.get("http://automationexercise.com")
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()