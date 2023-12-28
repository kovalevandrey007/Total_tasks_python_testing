import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.chromium.options import ChromiumOptions
import logging

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, testdata['loc1'])
    LOCATOR_PASS_FIELD = (By.XPATH, testdata['loc2'])
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, testdata['loc3'])
    LOCATOR_TOUCH_ABOUT = (By.XPATH, testdata['loc4'])
    LOCATOR_SIZE_ABOUT = (By.XPATH, testdata['loc5'])

class OperationsHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.init_browser = None

    def enter_login(self, word):
        logging.info(f"Senf {word} of element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Senf {word} of element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_touch_about(self):
        logging.info('Click to "About"')
        self.find_element(TestSearchLocators.LOCATOR_TOUCH_ABOUT).click()


    def get_size_about(self):
        font_size = self.find_element(TestSearchLocators.LOCATOR_SIZE_ABOUT).value_of_css_property('font-size')
        logging.info(f'We find-size = {font_size} in success field')
        return font_size

