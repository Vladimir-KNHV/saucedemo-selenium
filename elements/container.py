from elements.base_element import BaseElement
import allure
from tools.logger import get_logger
logger = get_logger("CONTAINER_ELEMENT")

class Container(BaseElement):
    @property
    def _type_of(self) -> str:
        return 'Container'

    def count(self) -> int:
        step = f'Getting count of {self._type_of} with name "{self._name}"'
        with allure.step(step):
            locator = self._get_locator()
            elements = self._driver.find_elements(*locator)
            logger.info(step)
            return len(elements)



