from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterForm(BasePage):

    def __init__(self, driver, base_page_element=(By.XPATH, "//div[@class='register']")):
        super().__init__(driver, base_page_element)

    __username = (By.ID, "username")
    __password = (By.ID, "password")
    __email = (By.ID, "email")
    __register_button = (By.XPATH, "//input[@value='Register']")

    def register(self, username, password, email):
        self.send_keys(self.__username, username)
        self.send_keys(self.__password, password)
        self.send_keys(self.__email, email)
        self.click(self.__register_button)
