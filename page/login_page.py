import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    switch_login_type_button = By.ID, "lbNormal"

    login_frame = By.TAG_NAME, "iframe"

    username_text_field = By.NAME, "email"

    password_text_field = By.NAME, "password"

    login_button = By.ID, "dologin"

    @allure.step(title="切换 登录模式")
    def click_switch_login_type(self):
        self.click(self.switch_login_type_button)

    def get_login_frame(self):
        return self.find_element(self.login_frame)

    @allure.step(title="输入 用户名")
    def input_username(self, text):
        self.driver.switch_to.frame(self.get_login_frame())
        self.input(self.username_text_field, text)
        self.driver.switch_to.default_content()

    @allure.step(title="输入 密码")
    def input_password(self, text):
        self.driver.switch_to.frame(self.get_login_frame())
        self.input(self.password_text_field, text)
        self.driver.switch_to.default_content()

    @allure.step(title="点击 登录")
    def click_login(self):
        self.driver.switch_to.frame(self.get_login_frame())
        self.click(self.login_button)
        self.driver.switch_to.default_content()

    @allure.step(title="登录 hitfeat账号")
    def login(self):
        self.click_switch_login_type()
        self.input_username("hitfeat")
        self.input_password("hitfeat123000")
        self.click_login()

