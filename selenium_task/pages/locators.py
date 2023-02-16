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
        By.CSS_SELECTOR,  # TODO for English
        '.MuiTypography-root.MuiTypography-body2[title="Виджеты"]')


class EmployeePageLocators:
    RU_LIST_TITLE = (
        By.CSS_SELECTOR,
        '.MuiTypography-root.MuiTypography-h2')
    RU_ADD_EMPLOYEE_BUTTON = (
        By.CSS_SELECTOR,  # TODO for English
        '.MuiButtonBase-root[title="Добавить нового сотрудника"]')
    ADD_EMPLOYEE_FORM = (By.ID, 'NewEmployeeForm')
    INPUT_FIELDS = (
        By.CSS_SELECTOR,  # TODO another selector
        '#NewEmployeeForm .MuiInputBase-input.MuiOutlinedInput-input[type="text"]')
    INPUT_COMMENTS_FIELD = (
        By.CSS_SELECTOR,
        '#NewEmployeeForm .MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputMultiline')
    SUBMIT_ADD_EMPLOYEE_BUTTON = (
        By.CSS_SELECTOR, 'button.MuiButtonBase-root.MuiButton-root')
    # ADD_PHOTO_BUTTON = (By.CSS_SELECTOR, '#NewEmployeeForm button')  # 1st elmnt

    EMPLOYEE_LIST = (
        By.CSS_SELECTOR,
        '.MuiBox-root .MuiTypography-colorTextPrimary > div:nth-child(2)')
    EMPLOYEE_CARD_BLOCK = (
        By.CSS_SELECTOR, 'div[role="tabpanel"] > .MuiBox-root')
    EMPLOYEE_NAME_IN_CARD = (
        By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-h4')
