from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from tools.logger import get_logger
logger = get_logger("BASE_ELEMENT")

class  BaseElement:
    def __init__(self, driver: WebDriver, locator: str, name: str):
        self._driver = driver
        self._locator = locator
        self._name = name
        self._wait = WebDriverWait(driver, 15)
        self._EC = expected_conditions

    @property
    def _type_of(self) -> str:
        return 'Element'

    def _get_locator(self, index: int | None = None):
        by = 'xpath'
        value = self._locator
        if index is not None:
            value = f'({value})[{index}]'

        if index is None:
            step = f'Getting locator "{self._locator}"'
        else:
            step = f'Getting locator "{self._locator}" with index "{index}"'
        with allure.step(step):
            logger.info(step)
            return by, value


    def click(self, index: int | None = None):
        step = f'Clicking {self._type_of} with name "{self._name}"'
        with allure.step(step):
            locator = self._get_locator(index)
            logger.info(step)
            self._wait.until(self._EC.element_to_be_clickable(locator)).click()

    def scroll_to(self, index: int | None = None):
        step = f'Scroll to {self._type_of} with name "{self._name}"'
        with allure.step(step):
            locator = self._get_locator(index)
            element = self._wait.until(self._EC.presence_of_element_located(locator))
            logger.info(step)
            self._driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element
            )

    def check_visible(self, index: int | None = None):
        step = f'Checking {self._type_of} with name "{self._name}" is visible'
        with allure.step(step):
            locator = self._get_locator(index)
            logger.info(step)
            self._wait.until(self._EC.visibility_of_element_located(locator))

    def get_text(self, index: int | None = None):
        if index is None:
            step = f'Getting text from {self._type_of} with name "{self._name}"'
        else:
            step = f'Getting text from {self._type_of} with name "{self._name}" with index {index}'

        with allure.step(step):
            locator = self._get_locator(index)
            element = self._wait.until(self._EC.visibility_of_element_located(locator))
            logger.info(step)
            return element.text

    def get_all_texts(self) -> list[str]:
        step = f'Get all texts from {self._type_of} with name "{self._name}"'
        with allure.step(step):
            locator = self._get_locator()
            elements = self._wait.until(
                self._EC.visibility_of_all_elements_located(locator)
            )
            logger.info(step)
            return [element.text for element in elements]

    def check_have_text(self, text: str, index: int | None = None):
        step = f'Checking {self._type_of} with name "{self._name}" have text "{text}"'
        with allure.step(step):
            locator = self._get_locator(index)
            element = self._wait.until(self._EC.visibility_of_element_located(locator))
            logger.info(step)
            assert element.text == text

    def check_have_contain_text(self, text: str, index: int | None = None):
        step = f'Checking {self._type_of} with name "{self._name}" have contain text "{text}"'
        with allure.step(step):
            locator = self._get_locator(index)
            logger.info(step)
            self._wait.until(self._EC.text_to_be_present_in_element(locator, text))


