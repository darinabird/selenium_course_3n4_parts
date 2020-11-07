from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.base_page import BasePage


def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.product_url
    page = ProductPage(browser, link)
    page.open()
    page.add_item()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item()
