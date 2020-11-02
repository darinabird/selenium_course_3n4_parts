from time import sleep
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.main_page import MainPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    browser.get(link)
    sleep(3)
    ProductPage(browser, link).check_basket()

    
