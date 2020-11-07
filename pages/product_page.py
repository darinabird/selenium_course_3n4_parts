from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage, ProductPageLocators):
    # --- unnecessary part ---
    
    # def check_basket(self, browser):
    #     self.add_item(browser)
    #     self.naming_equality()
    #     self.check_price_equality()

    #     link = self.browser.find_element(*ProductPageLocators.product_url)
    #     link.click()
    #     return ProductPage(browser=self.browser, url=self.browser.current_url)

    def add_item(self):
        '''
        Описать метод добавления в корзину.
        '''
        b_button = self.browser.find_element(*ProductPageLocators.b_button)
        b_button.click()
        # активация скидки
        self.solve_quiz_and_get_code()

    def naming_equality(self):
        '''
        Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        '''
        assert self.item_name == self.item_bname, 'Naming is the same'

    def check_price_equality(self):
        '''
        Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 
        '''
        assert self.item_price == self.total_price, 'Price is the same'
