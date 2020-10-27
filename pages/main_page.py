from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        
        # неясно почему не импортируется self как browser ??
        login_link = self.find_element_by_css_selector('#login_link')
        login_link.click()
