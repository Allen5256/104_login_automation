from selenium.webdriver.common.by import By

from page_objects import ActionUtils


class MemberPage(ActionUtils):
    # Element locators
    user_info_name = (By.CLASS_NAME, "h2 mb-3")

    def __init__(self, driver):
        super().__init__(driver)

    def get_username(self):
        username = self.find_present_element(self.user_info_name)
        return username
