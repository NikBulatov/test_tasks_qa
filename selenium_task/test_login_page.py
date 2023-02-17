import os
import pytest
from dotenv import load_dotenv

from .pages.employees_page import EmployeePage
from .pages.login_page import LoginPage
from .pages.operator_page import OperatorPage

load_dotenv('../.env')


class TestCase:
    URL = 'http://s2.corp.sigur.com/'
    LOGIN_URL = 'http://s2.corp.sigur.com/login'
    OPERATOR_URL = 'http://s2.corp.sigur.com/widgets/visits'
    EMPLOYEES_URL = 'http://s2.corp.sigur.com/system/employees'

    def test_operator_go_to_login_page(self, browser):
        login, password = (os.getenv('OPERATOR_LOGIN'),
                           os.getenv('OPERATOR_PASSWORD'))
        login_page = LoginPage(browser, TestCase.URL)
        login_page.open()
        login_page.should_be_login_page(TestCase.LOGIN_URL)
        login_page.login_operator(login, password)

        operator_page = OperatorPage(browser, browser.current_url)
        operator_page.should_be_operator_page(TestCase.OPERATOR_URL)

        employee_page = EmployeePage(browser, TestCase.EMPLOYEES_URL)
        employee_page.open()

        # TODO check page

        employee_page.should_be_add_employee_button()
        employee_page.open_employee_form()
        employee_page.add_new_employee()

        employee_page.should_be_created_new_employee()
        employee_page.should_be_correct_employee_data()
