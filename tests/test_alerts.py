import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://demo.seleniumeasy.com/javascript-alert-box-demo.html")
    yield driver
    driver.quit()


def test_java_script_alert_box_text(browser):
    click_me_button = By.XPATH, "//button[@OnClick='myAlertFunction()']"
    browser.find_element(*click_me_button).click()
    # Verify text in opened alert
    WebDriverWait(browser, 5).until(ec.alert_is_present())
    java_script_alert_box = browser.switch_to.alert
    actual_java_script_alert_box_text = java_script_alert_box.text
    assert actual_java_script_alert_box_text in 'I am an alert box!', f"Unexpected text in the alert, got: {actual_java_script_alert_box_text}"


def test_java_script_confirm_box_accept(browser):
    click_me_button = browser.find_element(By.XPATH, "//button[@OnClick='myConfirmFunction()']")
    actions = ActionChains(browser)
    actions.move_to_element(click_me_button)
    actions.perform()
    click_me_button.click()
    # Verify text in confirm box after confirmation
    WebDriverWait(browser, 5).until(ec.alert_is_present())
    java_script_confirm_box = browser.switch_to.alert
    java_script_confirm_box.accept()
    actual_accepted_text = browser.find_element(By.ID, "confirm-demo").text
    assert actual_accepted_text in "You pressed OK!", f"Unexpected text after confirmation, got: {actual_accepted_text}"


def test_java_script_confirm_box_cancel(browser):
    click_me_button = browser.find_element(By.XPATH, "//button[@OnClick='myConfirmFunction()']")
    actions = ActionChains(browser)
    actions.move_to_element(click_me_button)
    actions.perform()
    click_me_button.click()
    # Verify text after cancellation in confirm box
    WebDriverWait(browser, 5).until(ec.alert_is_present())
    java_script_confirm_box = browser.switch_to.alert
    java_script_confirm_box.dismiss()
    actual_accepted_text = browser.find_element(By.ID, "confirm-demo").text
    assert actual_accepted_text in "You pressed Cancel!", f"Unexpected text after canceling in confirm box, got: {actual_accepted_text}"
