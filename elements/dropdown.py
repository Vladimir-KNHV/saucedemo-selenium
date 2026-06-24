from elements.base_element import BaseElement
from enums.sort_option import SortOption
from selenium.webdriver.support.ui import Select
import allure
from tools.logger import get_logger
logger = get_logger("DROPDOWN_ELEMENT")


class Dropdown(BaseElement):

    @property
    def _type_of(self) -> str:
        return 'Dropdown'

    def sort(self, option: SortOption):
        step = f'{self._type_of} sort with value {option.name}'
        with allure.step(step):
            locator = self._get_locator()
            element = self._wait.until(self._EC.element_to_be_clickable(locator))
            logger.info(step)
            Select(element).select_by_value(option.value)


    def check_selected_option(self, option: SortOption = SortOption.NAME_AZ):
        step = f'Check {self._type_of} selected option is "{option.name}"'
        with allure.step(step):
            logger.info(step)
            locator = self._get_locator()
            element = self._wait.until(self._EC.visibility_of_element_located(locator))
            select = Select(element)
            logger.info(step)
            assert select.first_selected_option.get_attribute("value") == option.value




