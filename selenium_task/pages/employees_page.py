from selenium.common import NoSuchElementException

from .base_page import BasePage
from .locators import EmployeePageLocators


class EmployeePage(BasePage):
    FORM_DATA = {
        "second_name": "Testov",
        "first_name": "Test",
        "last_name": "Testovich",

        # TODO add data below
        # "Position": "Manager",  # !!!
        # "Number": "01",
        # "Email": "test@example.com",
        # "Phone number": "+7(123) 159-95-75",
        # "Telegram chat ID": "-9658412",
        # "Communication method": '',
    }
    EMPLOYEE_NAME = 'Testov Test Testovich'
    COMMENT_DATA = 'Comment'

    def __init__(self, *args, **kwargs):
        super(EmployeePage, self).__init__(*args, **kwargs)

    def should_be_add_employee_button(self):
        assert self.is_element_present(
            *EmployeePageLocators.RU_ADD_EMPLOYEE_BUTTON)

    def should_be_add_new_employee_form(self):
        assert self.is_not_element_present(
            *EmployeePageLocators.ADD_EMPLOYEE_FORM)

    def open_employee_form(self):
        self.browser.find_element(
            *EmployeePageLocators.RU_ADD_EMPLOYEE_BUTTON).click()
        self.should_be_add_new_employee_form()

    def add_new_employee(self):
        # TODO add photo
        # self.browser.find_element(
        #     EmployeePageLocators.ADD_PHOTO_BUTTON).send_keys('')

        input_text_fields = self.browser.find_elements(
            *EmployeePageLocators.INPUT_FIELDS)[:3]

        for field, value in zip(input_text_fields,
                                EmployeePage.FORM_DATA.values()):
            field.send_keys(value)

        self.browser.find_element(
            *EmployeePageLocators.INPUT_COMMENTS_FIELD).send_keys(
            EmployeePage.COMMENT_DATA)

        self.browser.find_element(
            *EmployeePageLocators.SUBMIT_ADD_EMPLOYEE_BUTTON).click()

    def should_be_created_new_employee(self):
        employee_list = None
        try:
            employee_list = [name for name in self.browser.find_elements(
                *EmployeePageLocators.EMPLOYEE_LINK_LIST) if
                             name.text == EmployeePage.EMPLOYEE_NAME]
            if EmployeePage.EMPLOYEE_NAME not in map(lambda x: x.text,
                                                     employee_list):
                raise NoSuchElementException
            self.open_employee_card_info(employee_list)
        except NoSuchElementException:
            assert employee_list is not None, "Employee doesn't exist"

    def should_be_employee_card_block(self):
        assert self.is_element_present(
            *EmployeePageLocators.EMPLOYEE_CARD_BLOCK)

    def should_be_correct_employee_name(self):
        assert self.is_element_present(
            *EmployeePageLocators.EMPLOYEE_NAME_IN_CARD)
        assert self.browser.find_element(
            *EmployeePageLocators.EMPLOYEE_NAME_IN_CARD).text == EmployeePage.EMPLOYEE_NAME

    def should_be_correct_comments(self):
        assert self.is_element_present(
            *EmployeePageLocators.EMPLOYEE_COMMENT_FIELD)
        assert self.browser.find_element(
            *EmployeePageLocators.EMPLOYEE_COMMENT_FIELD).text == EmployeePage.COMMENT_DATA

    def open_employee_card_info(self, employee_list):
        employee_list[0].click()
        self.should_be_employee_card_block()

    def should_be_correct_employee_data(self):
        self.should_be_correct_employee_name()
        self.should_be_correct_comments()
