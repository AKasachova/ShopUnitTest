import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import random


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
    multi_select_element = browser.find_element(By.ID, 'multi-select')
    actions = ActionChains(browser)
    actions.move_to_element(multi_select_element)
    actions.perform()
    select = Select(multi_select_element)
    all_options = select.options
    random.shuffle(all_options)
    # select 3 first options from randomly shuffled  all options (list of options)
    selected_options = all_options[:3]
    for option in selected_options:
        option.click()

    for option in selected_options:
        assert option.is_selected(), f"{option.text} is not selected"

