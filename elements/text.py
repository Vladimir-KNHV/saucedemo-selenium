from elements.base_element import BaseElement
import allure


class Text(BaseElement):
    @property
    def _type_of(self) -> str:
        return 'Text'


