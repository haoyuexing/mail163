import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    write_button = By.XPATH, "//span[text()='写 信']"

    username_text_view = By.ID, "spnUid"

    @allure.step(title="点击 写信")
    def click_write(self):
        self.click(self.write_button)

    def get_username(self):
        return self.find_element(self.username_text_view).text
