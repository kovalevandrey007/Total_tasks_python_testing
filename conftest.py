import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chromium.options import ChromiumOptions

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']

@pytest.fixture(scope='session')
def init_browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
