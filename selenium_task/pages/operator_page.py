from .base_page import BasePage
from .locators import MainPageLocators


class OperatorPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(OperatorPage, self).__init__(*args, **kwargs)

    def should_be_operator_page(self, url):
        self.should_be_widgets_title()
        self.should_be_correct_url(url)

    def should_be_widgets_title(self):
        # TODO language choosing should be in another place
        title = {
            'ru': 'Виджеты',
            'en': 'Widgets'
        }
        assert self.is_element_present(*MainPageLocators.RU_WIDGET_TITLE)
        assert self.browser.find_element(
            *MainPageLocators.RU_WIDGET_TITLE).text == title.get('ru')
