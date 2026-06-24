from elements.base_element import BaseElement
import allure
from tools.logger import get_logger
logger = get_logger("INPUT_ELEMENT")

class Input(BaseElement):

    @property
    def _type_of(self) -> str:
        return 'Input'

    def fill(self, value: str):
        step = f'Fill {self._type_of} with name "{self._name}" to value "{value}"'
        with allure.step(step):
            locator = self._get_locator()
            element = self._wait.until(self._EC.visibility_of_element_located(locator))
            element.clear()
            logger.info(step)
            element.send_keys(value)

    def check_have_value(self, value: str):
        step = f'Checking {self._type_of} with name "{self._name}" have value "{value}"'
        with allure.step(step):
            locator = self._get_locator()
            element = self._wait.until(self._EC.visibility_of_element_located(locator))
            logger.info(step)
            assert element.get_attribute("value") == value