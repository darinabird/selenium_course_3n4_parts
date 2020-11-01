from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    def add_item_to_basket(self):

        b_button = self.browser.find_element(By.CSS_SELECTOR, "")
        b_button.click()

    