from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def wait_for_random_user_creation(browser):
    get_new_user_button = browser.find_element(By.ID, "save")
    browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'start' });", get_new_user_button)
    get_new_user_button.click()
    # Wait for loading random user data
    loading_user_data = WebDriverWait(browser, 7).until_not(lambda d: 'loading...' in d.find_element(By.ID, "loading").text)
    # presence_user_img = WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.XPATH, "//div[@id='loading']//img")))
    loading_user_text = WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.XPATH, "//div[@id='loading']"))).text
    return print(f"{loading_user_text}")


# Example usage:
browser_1 = webdriver.Chrome()
browser_1.get("https://demo.seleniumeasy.com/dynamic-data-loading-demo.html")
random_user_creation = wait_for_random_user_creation(browser_1)
browser_1.quit()
