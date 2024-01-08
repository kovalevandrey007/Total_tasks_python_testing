import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.chromium.options import ChromiumOptions
import logging

with open('./locators.yaml', encoding='utf-8') as f:
    locators = yaml.safe_load(f)


class TestSearchLocators:
    LOCATOR_LOGIN_BTN = None
    ids = dict()
    with open('./locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.info(f"Send {word} to element {element_name}")
        field = self.find_element(locator)

        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True


    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f"Exception with click")
            return False
        logging.info(f"Clicked {element_name} button")
        return True

    # EDIT TEXT
    def __init__(self, driver):
        super().__init__(driver)
        self.init_browser = None

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description="password form")

    def get_size_about(self):
        font_size = self.find_element(TestSearchLocators.ids['LOCATOR_SIZE_ABOUT']).value_of_css_property('font-size')
        logging.info(f'We find-size = {font_size} in success field')
        return font_size

    # BUTTON
    def get_touch_about(self):
        logging.info('Click to "About"')
        self.find_element(TestSearchLocators.ids['LOCATOR_TOUCH_ABOUT']).click()

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.ids['LOCATOR_LOGIN_BTN']).click()
