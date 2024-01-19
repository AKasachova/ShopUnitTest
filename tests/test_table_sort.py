import pytest
from selenium import webdriver
from src.table_sort import get_filtered_employees
from pytest_check import check


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://demo.seleniumeasy.com/table-sort-search-demo.html")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_table_sort(browser):
    age_to_filter_1 = 30
    salary_to_filter_1 = 675000.0
    filtered_employees = get_filtered_employees(browser, age_to_filter_1, salary_to_filter_1)
    for employee in filtered_employees:
        with check:
            assert employee.age > age_to_filter_1 and employee.salary <= salary_to_filter_1, (
                f"Employee doesn't much needed salary or age.\n"
                f" the Employee age: {employee.age}, the Employee salary: {employee.salary}"
            )
