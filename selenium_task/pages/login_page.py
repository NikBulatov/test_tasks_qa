from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    LOGIN_URL = 'http://172.19.5.189/login'

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_correct_url(LoginPage.LOGIN_URL)

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form isn't presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_INPUT), "Login field isn't presented"
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD_INPUT), "Password field isn't presented"

    def login_operator(self, login: str, password: str):
        if isinstance(login, str) and isinstance(password, str):
            login_field = self.browser.find_element(
                *LoginPageLocators.LOGIN_INPUT)
            login_field.send_keys(login)
            password_field = self.browser.find_element(
                *LoginPageLocators.PASSWORD_INPUT)
            password_field.send_keys(password)
            self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        else:
            raise ValueError(
                "login and password arguments should be 'str' type")
