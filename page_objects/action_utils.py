from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class ActionUtils:
    def __init__(self, driver):
        self.driver = driver

    def find_present_element(self, locator, timeout=10):
        try:
            elem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator)))
        except TimeoutException:
            return None
        return elem

    def find_present_elements(self, locator, timeout=10):
        try:
            elems = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((locator)))
        except TimeoutException:
            return []
        return elems

    def find_clickable_element(self, locator, timeout=10):
        try:
            elem = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((locator)))
        except TimeoutException:
            return None
        return elem

    def click_element(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((locator))).click()
            return self
        except TimeoutException:
            return self

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self
