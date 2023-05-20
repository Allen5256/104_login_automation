from .action_utils import ActionUtils
from .home_page import HomePage
from .login_page import LoginPage
from .member_page import MemberPage


def init_page_objects(driver):
    driver.home_page_object = HomePage(driver)
    driver.login_page_object = LoginPage(driver)
    driver.member_page_object = MemberPage(driver)
