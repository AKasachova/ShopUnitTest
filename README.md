# Running Selenium Tests (Windows) in Selenoid

Set the environment variable `RUN_IN_SELENOID` to `True`, set `BROWSER` to `chrome`/`firefox` (choose browser in which
you want to run tests), then execute the following commands:

pytest -v -s --alluredir results
allure serve results

# Running Selenium Tests (Windows) locally

Set the environment variable `RUN_IN_SELENOID` not to `True`, set `BROWSER` to `chrome`/`firefox` (choose browser in which
 you want to run tests), then execute the following commands:

pytest -v -s --alluredir results
allure serve results


