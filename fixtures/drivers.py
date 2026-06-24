from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Generator
import allure
from config import settings
from tools.selenium.driver import create_driver


@pytest.fixture(params=settings.browsers)
def driver(request) -> Generator[WebDriver, None, None]:
    browser = create_driver(request.param)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def initialize_driver_state():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=options)
    browser.get(str(settings.app_url))
    try:
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="username"]'))).send_keys(
            settings.test_user.username)
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="password"]'))).send_keys(
            settings.test_user.password)
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="login-button"]'))).click()

        cookies = browser.get_cookies()
        return cookies
    finally:
        browser.quit()


@pytest.fixture()
def driver_with_state(driver: WebDriver, initialize_driver_state) -> Generator[WebDriver, None, None]:
    driver.get(str(settings.app_url))

    cookies = initialize_driver_state

    for cookie in cookies:
        driver.add_cookie(cookie)

    yield driver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield  # Выполняем тест
    report = outcome.get_result()  # Получаем результат
    setattr(item, f"rep_{report.when}", report)  # Привязываем его к тесту


@pytest.fixture(autouse=True)
def take_screenshot_on_failure(request, driver: WebDriver):
    yield
    if request.node.rep_call.failed:  # Если тест упал
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="Screen on failure",
            attachment_type=allure.attachment_type.PNG
        )