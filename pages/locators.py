from selenium.webdriver.common.by import By


class MainPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    login_url = (By.CSS_SELECTOR, '[href="/en-gb/accounts/login/"]')
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")