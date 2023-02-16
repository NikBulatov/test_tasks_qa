import os
import pytest
from dotenv import load_dotenv
from .pages.login_page import LoginPage
from .pages.operator_page import OperatorPage

load_dotenv('../.env')


class TestOperatorLogin:
    URL = 'http://s2.corp.sigur.com/'
    LOGIN_URL = 'http://s2.corp.sigur.com/login'
    OPERATOR_URL = 'http://s2.corp.sigur.com/widgets/visits'

    def test_operator_go_to_login_page(self, browser):
        login, password = (os.getenv('OPERATOR_LOGIN'),
                           os.getenv('OPERATOR_PASSWORD'))
        login_page = LoginPage(browser, TestOperatorLogin.URL)
        login_page.open()
        login_page.should_be_login_page(TestOperatorLogin.LOGIN_URL)
        login_page.login_operator(login, password)

        operator_page = OperatorPage(browser, browser.current_url)
        operator_page.should_be_operator_page(TestOperatorLogin.OPERATOR_URL)

    def test_(self):
        pass
