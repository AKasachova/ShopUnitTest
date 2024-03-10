from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class CommonOps:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_to_element(self, locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find(locator))
        actions.perform()

    def make_screenshot_of_page(self, path):
        self.driver.save_screenshot(path)
