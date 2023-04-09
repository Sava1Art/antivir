from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, base_page_element):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_page_element = base_page_element

    def click(self, by_locator):
        self.wait.until(ec.element_to_be_clickable(by_locator)).click()

    def send_keys(self, by_locator, value):
        self.wait.until(ec.element_to_be_clickable(by_locator)).send_keys(value)

    def is_displayed(self, by_locator):
        return self.wait.until(ec.presence_of_element_located(by_locator)).is_displayed()

    def is_page_displayed(self):
        return self.wait.until(ec.presence_of_element_located(self.base_page_element)).is_displayed()
