from selenium.common.exceptions import (NoSuchElementException,
                                        TimeoutException)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=1):
        # try:
        #     WebDriverWait(self.browser, timeout).until(
        #         EC.presence_of_element_located((how, what)))
        # except TimeoutException:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_be_correct_url(self, correct_url):
        assert correct_url == self.browser.current_url
