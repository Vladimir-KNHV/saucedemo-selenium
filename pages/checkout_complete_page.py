from components.navigation.navbar_component import NavbarComponent
from elements.button import Button
from elements.image import Image
from elements.container import Container
from elements.text import Text
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
import allure
import re
from tools.routes import AppRoute


class CheckoutCompletePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.navbar = NavbarComponent(driver)

        self._checkout_complete_title = Text(driver, '//*[@data-test="title"]', 'checkout_complete_title')

        self._checkout_complete_confirmation = Container(driver, '//*[@data-test="checkout-complete-container"]', 'complete_information')
        self._confirmation_image = Image(driver, '//*[@data-test="pony-express"]', 'confirmation_image')
        self._confirmation_title = Text(driver, '//*[@data-test="complete-header"]', 'confirmation_title')
        self._confirmation_description = Text(driver, '//*[@data-test="complete-text"]', 'confirmation_description')

        self._checkout_complete_back_home_button = Button(driver, '//*[@data-test="back-to-products"]', 'back+home_button')

    @allure.step('Check visible checkout complete page')
    def check_visible_checkout_complete_page(self):
        self._checkout_complete_title.check_visible()
        self._checkout_complete_title.check_have_text('Checkout: Complete!')
        self._checkout_complete_confirmation.check_visible()
        self._confirmation_image.check_visible()
        self._confirmation_title.check_visible()
        self._confirmation_title.check_have_text('Thank you for your order!')
        self._confirmation_description.check_visible()
        self._confirmation_description.check_have_text(
            'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
        )
        self.check_current_url(re.compile(f'.*{AppRoute.CHECKOUT_COMPLETE.value}'))

    def click_back_home_button(self):
        self._checkout_complete_back_home_button.click()
