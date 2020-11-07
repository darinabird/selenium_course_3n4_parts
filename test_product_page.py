from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.main_page import MainPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = MainPage(browser, link)
    page.open()

# вызвать методы из product_page.py
# проверить цену книги с ценой корзины

# название карточки сверить с названием корзины
