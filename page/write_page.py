import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class WritePage(BaseAction):

    addressee_text_field = By.CLASS_NAME, 'nui-editableAddr-ipt'

    title_text_field = By.XPATH, '//*[@class="nui-ipt-input" and @maxlength="256"]'

    content_frame = By.CLASS_NAME, "APP-editor-iframe"

    content_text_field = By.XPATH, "//body[@class='nui-scroll']"

    send_button = By.XPATH, '//span[text()="发送"]'

    success_hint_text_view = By.XPATH, "//*[text()='发送成功']"

    @allure.step(title="输入 收件人")
    def input_addressee(self, text):
        self.input(self.addressee_text_field, text)

    @allure.step(title="输入 标题")
    def input_title(self, text):
        self.input(self.title_text_field, text)

    def get_content_frame(self):
        return self.find_element(self.content_frame)

    @allure.step(title="输入 正文")
    def input_content(self, text):
        self.driver.switch_to.frame(self.get_content_frame())
        self.input(self.content_text_field, text)
        self.driver.switch_to.default_content()

    @allure.step(title="点击 发送")
    def click_send(self):
        self.click(self.send_button)

    def is_send_success(self):
        return self.is_feature_exits(self.success_hint_text_view)
