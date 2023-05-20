import pytest
from selenium import webdriver


@pytest.fixture(name='drive')
def init_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
