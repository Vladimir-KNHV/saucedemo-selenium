from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from typing import Pattern
from tools.routes import AppRoute
from config import settings


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 15)
        self._EC = EC

    def open(self, route: AppRoute):
        with allure.step(f'Opening url "{str(settings.app_url)}{route.value}"'):
            self._driver.get(f"{str(settings.app_url)}{route.value}")

    def check_current_url(self, pattern: Pattern[str]):
        with allure.step(f'Checking current url matches pattern "{pattern.pattern}"'):
            self._wait.until(
                lambda d: pattern.search(d.current_url)
            )

    def check_url_not_contain_pattern(self, pattern: Pattern[str]):
        with allure.step(f'Checking URL does not match pattern "{pattern.pattern}"'):
            self._wait.until(
                lambda d: not pattern.search(d.current_url)
            )
