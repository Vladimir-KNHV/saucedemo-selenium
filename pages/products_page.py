from components.item_view_component import ItemViewComponent
from components.navigation.navbar_component import NavbarComponent
from elements.dropdown import Dropdown
from elements.text import Text
from enums.sort_option import SortOption
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
import allure
import re
from tools.routes import AppRoute

class ProductsPage(BasePage):
    item_view_component: ItemViewComponent

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.navbar = NavbarComponent(driver)
        self.item_view_component = ItemViewComponent(driver)

        self._products_title = Text(driver, '//*[@data-test="title"]', 'products title')
        self._products_sort_dropdown = Dropdown(driver, '//*[@data-test="product-sort-container"]', 'dropdown')

    @allure.step('Check visible products page')
    def check_visible_products_page(self):
        self._products_title.check_visible()
        self._products_title.check_have_text('Products')
        self._products_sort_dropdown.check_visible()
        self._products_sort_dropdown.check_selected_option()
        self.item_view_component.check_visible(indexes=[1,2,3,4,5,6])
        self.navbar.check_visible()
        self.check_current_url(re.compile(f'.*{AppRoute.PRODUCTS.value}'))


    def sort_products(self, option: SortOption):
        self._products_sort_dropdown.sort(option)

    def get_sorted_products(self, option: SortOption):
        if option in (SortOption.NAME_AZ, SortOption.NAME_ZA):
            return self.item_view_component.get_all_names()
        return self.item_view_component.get_all_prices()