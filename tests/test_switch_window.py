from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_window_switching():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")

    # Store the original window handle
    original_window = driver.current_window_handle

    # Open a new tab (replace with your application's logic)
    driver.execute_script("window.open('https://www.google.com', '_blank');")

    # Wait for the new window to open (explicit wait)
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # Switch to the new window using a more reliable method (finding by title)
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Perform actions in the new window
    print("Title of new window:", driver.title)
    assert "Google" in driver.title
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q"))) #Explicit wait for search box
    search_box.send_keys("Selenium 4 Python")
    search_box.submit()

    # Close the new window
    driver.close()

    # Switch back to the original window
    driver.switch_to.window(original_window)
    print("Title of original window:", driver.title)
    assert "Example Domain" in driver.title

    driver.quit()