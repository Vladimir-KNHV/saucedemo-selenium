from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver
from config import settings, Browser


def create_driver(browser_type: Browser) -> WebDriver:
    if browser_type == Browser.CHROME:
        options = ChromeOptions()
        options.add_argument('--incognito')

        if settings.headless:
            options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)

        return driver

    elif browser_type == Browser.FIREFOX:
        options = FirefoxOptions()

        if settings.headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080)
        return driver

    raise ValueError(f'Unsupported browser: {browser_type}')