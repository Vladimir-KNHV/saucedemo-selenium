from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.item_page import ItemPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage

import pytest

@pytest.fixture()
def login_page(driver: WebDriver) -> LoginPage:
    return LoginPage(driver=driver)


@pytest.fixture()
def products_page(driver: WebDriver) -> ProductsPage:
    return ProductsPage(driver=driver)

@pytest.fixture()
def products_page_with_state(driver_with_state: WebDriver) -> ProductsPage:
    return ProductsPage(driver=driver_with_state)

@pytest.fixture()
def cart_page(driver: WebDriver) -> CartPage:
    return CartPage(driver=driver)

@pytest.fixture()
def cart_page_with_state(driver_with_state: WebDriver) -> CartPage:
    return CartPage(driver=driver_with_state)

@pytest.fixture()
def item_page(driver: WebDriver) -> ItemPage:
    return ItemPage(driver=driver)

@pytest.fixture()
def item_page_with_state(driver_with_state: WebDriver) -> ItemPage:
    return ItemPage(driver=driver_with_state)


@pytest.fixture()
def checkout_complete_page(driver: WebDriver) -> CheckoutCompletePage:
    return CheckoutCompletePage(driver=driver)

@pytest.fixture()
def checkout_complete_page_with_state(driver_with_state: WebDriver) -> CheckoutCompletePage:
    return CheckoutCompletePage(driver=driver_with_state)


@pytest.fixture()
def checkout_info_page(driver: WebDriver) -> CheckoutInfoPage:
    return CheckoutInfoPage(driver=driver)

@pytest.fixture()
def checkout_info_page_with_state(driver_with_state: WebDriver) -> CheckoutInfoPage:
    return CheckoutInfoPage(driver=driver_with_state)


@pytest.fixture()
def checkout_overview_page(driver: WebDriver) -> CheckoutOverviewPage:
    return CheckoutOverviewPage(driver=driver)

@pytest.fixture()
def checkout_overview_page_with_state(driver_with_state: WebDriver) -> CheckoutOverviewPage:
    return CheckoutOverviewPage(driver=driver_with_state)



