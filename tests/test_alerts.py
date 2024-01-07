import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://demo.seleniumeasy.com/javascript-alert-box-demo.html")
    yield driver
    driver.quit()


def test_java_script_alert_box_text(browser):
    click_me_button = browser.find_element(By.CSS_SELECTOR, "div.col-md-6.text-left div.panel.panel-primary:first-of-type button")
    click_me_button.click()
    # Verify text in opened alert
    WebDriverWait(browser, 5).until(ec.alert_is_present())
    java_script_alert_box = browser.switch_to.alert
    actual_java_script_alert_box_text = java_script_alert_box.text
    expected_java_script_alert_box_text = 'I am an alert box!'
    assert actual_java_script_alert_box_text in expected_java_script_alert_box_text, f"Expected {expected_java_script_alert_box_text} to be presented, but got: {actual_java_script_alert_box_text}"
    java_script_alert_box.accept()


def test_java_script_confirm_box_accept(browser):
    click_me_button = browser.find_element(By.CSS_SELECTOR, "div.col-md-6.text-left div.panel.panel-primary:nth-of-type(2) button")
    browser.execute_script("arguments[0].scrollIntoView(true);", click_me_button)
    click_me_button.click()
    # Verify text after confirmation in confirm box
    WebDriverWait(browser, 5).until(ec.alert_is_present())
    java_script_confirm_box = browser.switch_to.alert
    java_script_confirm_box.accept()
    actual_accepted_text = browser.find_element(By.ID, "confirm-demo").text
    expected_accepted_text = "You pressed OK!"
    assert actual_accepted_text in expected_accepted_text, f"Expected {expected_accepted_text} to be presented, but got: {actual_accepted_text}"


def test_java_script_confirm_box_cancel(browser):
    click_me_button = browser.find_element(By.CSS_SELECTOR, "div.col-md-6.text-left div.panel.panel-primary:nth-of-type(2) button")
    browser.execute_script("arguments[0].scrollIntoView(true);", click_me_button)
    click_me_button.click()
    # Verify text after cancellation in confirm box
    WebDriverWait(browser, 5).until(ec.alert_is_present())
    java_script_confirm_box = browser.switch_to.alert
    java_script_confirm_box.dismiss()
    actual_accepted_text = browser.find_element(By.ID, "confirm-demo").text
    expected_accepted_text = "You pressed Cancel!"
    assert actual_accepted_text in expected_accepted_text, f"Expected {expected_accepted_text} to be presented, but got: {actual_accepted_text}"
