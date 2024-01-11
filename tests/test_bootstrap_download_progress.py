import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html")
    yield driver
    driver.quit()


def test_bootstrap_download_progress_refresh(browser):
    download_button = browser.find_element(By.ID, "cricle-btn")
    actions = ActionChains(browser)
    actions.move_to_element(download_button)
    actions.perform()
    download_button.click()
    progress_bar = int(browser.find_element(By.CLASS_NAME, "percenttext").text.strip('%'))
    while progress_bar < 50:
        progress_bar = int(browser.find_element(By.CLASS_NAME, "percenttext").text.strip('%'))
    browser.refresh()
    assert progress_bar >= 50, f"Browser was refreshed earlier,  progress bar value: {progress_bar}"
