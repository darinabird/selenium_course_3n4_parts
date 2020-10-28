from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):

        login_link = self.browser.find_element_by_css_selector(*MainPageLocators.login_link)
        login_link.click()

    # метод проверяющий наличие ссылки
    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.login_link), "Login link isn't presented"
