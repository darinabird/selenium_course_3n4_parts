from selenium.webdriver.common.by import By


class MainPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    login_url = (By.CSS_SELECTOR, '[href="/en-gb/accounts/login/"]')
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    product_url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    b_button = (By.ID, '#add_to_basket_form')
    item_name = (By.CSS_SELECTOR, '.alertinner strong')
    item_price = (By.CSS_SELECTOR, 'p.price_color')
    total_price = (By.CLASS_NAME, '.basket-mini strong')