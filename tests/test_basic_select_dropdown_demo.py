import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ByLocators:
    FIRST_MULTISELECT_OPTION = By.CSS_SELECTOR, "div.panel-body option[value='California']"
    SECOND_MULTISELECT_OPTION = By.CSS_SELECTOR, "div.panel-body option[value='Ohio']"
    THIRD_MULTISELECT_OPTION = By.CSS_SELECTOR, "div.panel-body option[value='Texas']"
    GET_ALL_SELECTED_BUTTON = By.ID, "printAll"
    OPTIONS_SELECTED = By.CLASS_NAME, "getall-selected"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_with_multiselect(browser):
    # Find 3 options from multiselect
    first_multiselect_option = browser.find_element(*ByLocators.FIRST_MULTISELECT_OPTION)
    browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'start' });", first_multiselect_option)
    first_multiselect_option.click()
    second_multiselect_option = browser.find_element(*ByLocators.SECOND_MULTISELECT_OPTION)
    third_multiselect_option = browser.find_element(*ByLocators.THIRD_MULTISELECT_OPTION)
    # Perform selection of found options
    action_chains = ActionChains(browser)
    action_chains.key_down(Keys.CONTROL)
    action_chains.click(second_multiselect_option)
    action_chains.click(third_multiselect_option)
    action_chains.key_up(Keys.CONTROL)
    action_chains.perform()
    # Verify chosen options are displayed in result line
    get_all_selected_button = browser.find_element(*ByLocators.GET_ALL_SELECTED_BUTTON)
    get_all_selected_button.click()
    options_selected = WebDriverWait(browser, 5).until(ec.presence_of_element_located(ByLocators.OPTIONS_SELECTED))
    actual_options_selected = options_selected.text
    expected_options_selected = "Options selected are : California,Ohio,Texas"
    assert actual_options_selected in expected_options_selected, f"Expected {expected_options_selected} to be presented, but got: {actual_options_selected}"
