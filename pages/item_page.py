from components.item_view_component import ItemViewComponent
from components.navigation.navbar_component import NavbarComponent
from elements.button import Button
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
import re
from tools.routes import AppRoute

class ItemPage(BasePage):
    def __init__(self,driver: WebDriver):
        super().__init__(driver)

        self.item_view_component = ItemViewComponent(driver)
        self.navbar = NavbarComponent(driver)

        self._back_to_products_button = Button(driver, '//*[@data-test="back-to-products"]', 'back_to_products_button')

    def click_back_to_products_button(self):
        self._back_to_products_button.click()

    def check_visible_item_page(self):
        self.item_view_component.check_visible()
        self._back_to_products_button.check_have_text('Back to products')
        self.check_current_url(re.compile(f'.*{AppRoute.ITEM.value}'))

