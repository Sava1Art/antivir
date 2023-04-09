from selenium import webdriver
import configuration
from drivers.browser_actions import BrowserActions
from pages.autorization_page.login_form import LoginForm
from pages.autorization_page.register_form import RegisterForm

driver = webdriver


def setup_module():
    global driver
    browser = BrowserActions()
    browser.go_to_url(url=configuration.URL)
    driver = browser.get_driver()


def test_login():
    login_form = LoginForm(driver)
    assert login_form.is_page_displayed(), "Login form isn't opened"
    login_form.login(configuration.LOGIN, configuration.PASS)
    assert not login_form.is_page_displayed(), "Login isn't successful"


def test_register():
    LoginForm(driver).switch_to_register_form()
    register_form = RegisterForm(driver)
    assert register_form.is_page_displayed()
    register_form.register(configuration.LOGIN, configuration.PASS, configuration.EMAIL)
    assert not register_form.is_page_displayed(), "Login isn't successful"


def teardown_module():
    BrowserActions().close_browser()
