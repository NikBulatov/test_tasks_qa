from selenium.common import NoSuchElementException

from .base_page import BasePage
from .locators import EmployeePageLocators


class EmployeePage(BasePage):
    FORM_DATA = {
        "second_name": "Testov",
        "first_name": "Test",
        "last_name": "Testovich",
        "Position": "Manager",  # !!!
        "Number": "01",
        # TODO add contact data
        # "Email": "test@example.com",
        # "Phone number": "+7(123) 159-95-75",
        # "Telegram chat ID": "-9658412",
        # "Communication method": '',
    }
    EMPLOYEE_NAME = 'Testov Test Testovich'

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
            *EmployeePageLocators.INPUT_FIELDS)[:5]

        for field, value in zip(input_text_fields,
                                EmployeePage.FORM_DATA.values()):
            field.send_keys(value)

        self.browser.find_element(
            *EmployeePageLocators.INPUT_COMMENTS_FIELD).send_keys('Comment')

        self.browser.find_element(
            *EmployeePageLocators.SUBMIT_ADD_EMPLOYEE_BUTTON).click()

    def should_be_created_new_employee(self, employee_name):
        new_employee_name = None
        try:
            employee_names = self.browser.find_elements(
                *EmployeePageLocators.EMPLOYEE_LIST)
            new_employee_name = [name for name in employee_names
                                 if name.text() == employee_name][
                0]
        except NoSuchElementException:
            assert new_employee_name.text() is not None, "Employee doesn't exist"

    def should_be_employee_card_block(self):
        self.is_element_present(*EmployeePageLocators.EMPLOYEE_CARD_BLOCK)

    def should_be_correct_employee_name(self):
        assert self.is_element_present(
            *EmployeePageLocators.EMPLOYEE_NAME_IN_CARD).text() == EmployeePage.EMPLOYEE_NAME

    def open_employee_card_info(self):
        employee_names = self.browser.find_elements(
            *EmployeePageLocators.EMPLOYEE_LIST)
        [name for name in employee_names if
         name.text() == 'Testov Test Testovich'][0].click()
        self.should_be_employee_card_block()
        self.should_be_correct_employee_name()
