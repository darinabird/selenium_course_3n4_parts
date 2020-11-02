from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def check_basket(self):
        self.add_item(self.browser)
        get_full_answer = self.solve_quiz_and_get_code()
        prepared_answer = get_full_answer.split(' ')[11]
        print('\nЭто твой ответ для степика:', prepared_answer)
        print('\nдальше ассерты сама)))')
        self.naming_equality()
        self.check_price_equality()

    def add_item(self, browser):
        '''
        Описать метод добавления в корзину.
        '''
        prefind = browser.find_element(*ProductPageLocators.pre_find)
        b_button = prefind.find_element(*ProductPageLocators.b_button)
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
