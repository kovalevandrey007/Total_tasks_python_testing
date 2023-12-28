from test_page import OperationsHelper
import logging
import yaml


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

def test_step_1(init_browser):
    logging.info("Test1 starting")
    test_page = OperationsHelper(init_browser)
    test_page.go_to_site()
    test_page.enter_login(testdata['login'])
    test_page.enter_pass(testdata['password'])
    test_page.click_login_button()
    test_page.get_touch_about()
    test_page.get_size_about()
    assert test_page.get_size_about() == f'32px'