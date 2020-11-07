from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def check_basket(self, browser):
        self.add_item(browser)
        self.naming_equality()
        self.check_price_equality()

        link = self.browser.find_element(*ProductPageLocators.product_url)
        link.click()
        return ProductPage(browser=self.browser, url=self.browser.current_url)

    def add_item(self, browser):
        '''
        Описать метод добавления в корзину.
        '''
        b_button = browser.find_element(*ProductPageLocators.b_button)
        b_button.click()


    def naming_equality(self):
        '''
        Сообщение о том, что товар добавлен в корзину.
        Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.

        --сейчас стоит, та проверка, которую смогла написать--
        '''
        assert self.is_element_present(
            *ProductPageLocators.item_name), 'Element isn\'t here'

    def check_price_equality(self):
        '''
        Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 

        --сейчас стоит, та проверка, которую смогла написать--
        '''
        assert self.is_element_present(
            *ProductPageLocators.item_price), 'Element isn\'t here'
