import time
import pytest

from base.base_analyze import analyze_data
from base.base_page import Page


class TestSend:

    @pytest.fixture(params=["Chrome", "Firefox"], autouse=True)
    def setup(self, request):
        exec("from selenium import webdriver")
        self.driver = eval("webdriver.%s()" % request.param)
        self.driver.get("https://mail.163.com")
        self.page = Page(self.driver)

        def teardown():
            self.driver.quit()

        request.addfinalizer(teardown)

    @pytest.mark.parametrize("args", analyze_data())
    def test_send(self, args):
        addressee = args["addressee"]
        title = args["title"]
        content = args["content"]

        self.page.login.login()
        self.page.home.click_write()
        self.page.write.input_addressee(addressee)
        self.page.write.input_title(title)
        self.page.write.input_content(content)
        self.page.write.click_send()
        assert self.page.write.is_send_success()
