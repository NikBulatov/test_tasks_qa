from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_INPUT = (
        By.CSS_SELECTOR,
        '.MuiInputBase-input.MuiOutlinedInput-input[type="text"]')
    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        '.MuiInputBase-input.MuiOutlinedInput-input[type="password"]')
    SUBMIT_BUTTON = (
        By.CSS_SELECTOR,
        '.MuiButton-root[type="submit"]')
    LOGIN_FORM = (
        By.CSS_SELECTOR,
        'form[autocomplete="on"]')


class MainPageLocators:
    RU_WIDGET_TITLE = (
        By.CSS_SELECTOR,
        '.MuiTypography-root.MuiTypography-body2[title="Виджеты"]')  # TODO
