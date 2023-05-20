from selenium.webdriver.common.by import By

from page_objects import ActionUtils


class HomePage(ActionUtils):
    # Element locators
    login_btn = (By.LINK_TEXT, "登入")
    name_selector = (By.LINK_TEXT, "姓名")
    member_center_btn = (By.LINK_TEXT, "My104會員中心")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_btn(self):
        login_btn_element = self.find_clickable_element(self.login_btn)
        login_btn_element.click()
        return self

    def head_to_member_center(self, username):
        self.name_selector = (By.LINK_TEXT, username)
        self.find_clickable_element(self.name_selector).click()
        self.find_clickable_element(self.member_center_btn).click()
        return self
