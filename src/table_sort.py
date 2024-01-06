from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Employee:
    def __init__(self, name, position, office, age, salary):
        self.name = name
        self.position = position
        self.office = office
        self.age = age
        self.salary = salary


def get_filtered_employees(browser, age_to_filter, salary_to_filter):
    dropdown = browser.find_element(By.NAME, "example_length")
    select = Select(dropdown)
    select.select_by_value("10")
    paginator = browser.find_element(By.CSS_SELECTOR, "div#example_paginate span")
    paginator_pages = paginator.find_elements(By.CSS_SELECTOR, "a.paginate_button")
    count = len(paginator_pages)
    i = 1
    sorted_employees = []
    while i <= count:
        current_paginator_page = browser.find_element(By.CSS_SELECTOR, f"div#example_paginate span a.paginate_button:nth-child({i})")
        table_rows = browser.find_elements(By.CSS_SELECTOR, "table#example tbody tr")
        for row in table_rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            name = columns[0].text
            position = columns[1].text
            office = columns[2].text
            age = int(columns[3].text)
            salary_str = columns[5].text[1:]
            salary = float(salary_str.replace(",", "").replace("/y", ""))

            if age > age_to_filter and salary <= salary_to_filter:
                employee_sorted = Employee(name, position, office, age, salary)
                sorted_employees.append(employee_sorted)
        i += 1
    return sorted_employees


# Example usage:
browser_1 = webdriver.Chrome()
browser_1.get("https://demo.seleniumeasy.com/table-sort-search-demo.html")

# Set age and salary
age_to_filter_1 = 30
salary_to_filter_1 = 675000.0
filtered_employees = get_filtered_employees(browser_1, age_to_filter_1, salary_to_filter_1)

# Print the result
for employee in filtered_employees:
    print(f"Name: {employee.name}, Position: {employee.position}, Office: {employee.office}, Age: {employee.age}, Salary: {employee.salary}")

browser_1.quit()
