from page_objects import init_page_objects
from test_data.user_info import username, account, password


class TestLogin:

    def test_login_success(self, driver):
        driver.get("https://www.104.com.tw/jobs/main/")

        init_page_objects(driver)
        home_page = driver.home_page_object
        login_page = driver.login_page_object
        member_page = driver.member_page_object

        home_page.click_login_btn()
        login_page.login(account, password)
        home_page.head_to_member_center().switch_to_new_tab()
        act_username = member_page.get_username()

        assert act_username == username, \
            f'User name verifying error, expected: "{username}", but actually get: "{act_username}".'
