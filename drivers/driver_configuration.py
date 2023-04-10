import configuration
from selenium import webdriver


def setup_driver():
    if configuration.BROWSER == "chrome":
        return __create_chrome_driver()
    elif configuration.BROWSER == "firefox":
        return webdriver.Firefox(executable_path="path")
    elif configuration.BROWSER == "edge":
        return webdriver.Edge(executable_path="path")
    else:
        print("Unknown browser, chrome set as default")
        return __create_chrome_driver()


def __create_chrome_driver():
    return webdriver.Chrome(executable_path=configuration.CHROME_DRIVER_DIRECTORY)
