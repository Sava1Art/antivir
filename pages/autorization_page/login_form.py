from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginForm(BasePage):

    def __init__(self, driver, base_page_element=(By.XPATH, "//div[@class='login']")):
        super().__init__(driver, base_page_element)

    __username = (By.ID, "username")
    __password = (By.ID, "password")
    __login_button = (By.XPATH, "//input[@value='Login']")
    __register_button = (By.XPATH, "//a[contains(@href,'register')]")

    def login(self, username, password):
        self.send_keys(self.__username, username)
        self.send_keys(self.__password, password)
        self.click(self.__login_button)

    def switch_to_register_form(self):
        self.click(self.__register_button)
