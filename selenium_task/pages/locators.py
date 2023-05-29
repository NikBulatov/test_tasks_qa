from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_INPUT = (By.XPATH, '//input[@type="text"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    LOGIN_FORM = (By.XPATH, '//form')


class MainPageLocators:
    RU_WIDGET_TITLE = (
        By.XPATH,
        '//div[contains(@class, "MuiTypography-body2")]/div[text()="Виджеты" and not(@class)]')

    EN_WIDGET_TITLE = (
        By.XPATH,
        '//div[contains(@class, "MuiTypography-body2")]/div[text()="Widgets" and not(@class)]')


class EmployeePageLocators:
    RU_LIST_TITLE = (
        By.XPATH,
        '//div[contains(@class, "MuiTypography-h2")]/div[not(@class)]')
    RU_ADD_EMPLOYEE_BUTTON = (
        By.CSS_SELECTOR,
        '.MuiButtonBase-root[title="Добавить нового сотрудника"]')
    EN_ADD_EMPLOYEE_BUTTON = (
        By.CSS_SELECTOR,
        '.MuiButtonBase-root[title="Add new employee"]')

    ADD_EMPLOYEE_FORM = (By.ID, '#NewEmployeeForm')

    INPUT_FIELDS = (
        By.CSS_SELECTOR,  # TODO another selector
        '#NewEmployeeForm .MuiInputBase-input.MuiOutlinedInput-input[type="text"]')

    INPUT_COMMENTS_FIELD = (By.CSS_SELECTOR, '#NewEmployeeForm textarea')
    SUBMIT_ADD_EMPLOYEE_BUTTON = (By.XPATH, '//button[@type="submit"]')

    EMPLOYEE_LINK_LIST = (
        By.XPATH,
        '//div[contains(@class, "MuiTypography-colorTextPrimary")]')

    # use in web element which was founded by EMPLOYEE_LINK_LIST locator
    # //div[contains(@class, "MuiTypography-colorTextPrimary")]/div[not(@class)]
    EMPLOYEE_NAME_IN_LIST = (By.XPATH, './/div[1]')

    EMPLOYEE_CARD_BLOCK = (
        By.CSS_SELECTOR, 'div[role="tabpanel"] > .MuiBox-root')
    EMPLOYEE_NAME_IN_CARD = (
        By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-h4')
    EMPLOYEE_COMMENT_FIELD = (
        By.XPATH,  # TODO another selector
        '//div[contains(@class, "MuiTypography-h6")]/following-sibling::div')
