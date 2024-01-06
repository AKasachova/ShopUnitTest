from selenium import webdriver
from selenium.webdriver.common.by import By


def bootstrap_download_progress_refresh(browser):
    download_button = browser.find_element(By.ID, "cricle-btn")
    browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'start' });", download_button)
    download_button.click()
    progress_bar = int(browser.find_element(By.CLASS_NAME, "percenttext").text.strip('%'))
    while progress_bar < 50:
        progress_bar = int(browser.find_element(By.CLASS_NAME, "percenttext").text.strip('%'))
    browser.refresh()
    return print(f"Progress bar value: {progress_bar}")


# Example usage:
browser_1 = webdriver.Chrome()
browser_1.get("https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html")
refresh_1 = bootstrap_download_progress_refresh(browser_1)
browser_1.quit()
