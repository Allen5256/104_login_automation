from selenium.webdriver.common.by import By

from page_objects import ActionUtils


class LoginPage(ActionUtils):
    # Element locators
    account_input = (By.ID, "username")
    passwd_input = (By.ID, "password")
    login_btn = (By.ID, "submitBtn")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, account, password):
        self.find_present_element(self.account_input).send_keys(account)
        self.find_present_element(self.passwd_input).send_keys(password)
        self.find_clickable_element(self.login_btn).click()
        return self
