import allure

from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from elements.button import Button
from elements.input import Input
from elements.base_element import BaseElement


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self._username_input = Input(driver, '//*[@data-test="username"]', 'username')
        self._password_input = Input(driver, '//*[@data-test="password"]', 'password')
        self._login_button = Button(driver, '//*[@data-test="login-button"]', 'login button')
        self._login_error_alert = BaseElement(driver, '//*[@data-test="error"]', 'login error alert')

    @allure.step('Fill login form')
    def fill_login_form(self, username: str, password: str):
        self._username_input.fill(username)
        self._username_input.check_have_value(username)

        self._password_input.fill(password)
        self._password_input.check_have_value(password)

    def click_login_button(self):
        self._login_button.click()

    @allure.step('Check login error alert')
    def check_login_error_alert(self, epic_sadface):
        self._login_error_alert.check_visible()
        self._login_error_alert.check_have_text(epic_sadface)