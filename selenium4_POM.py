#Page Object Model
from selenium import webdriver
import warnings

class LoginPage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.username_field_id = 'user-name'
        self.password_field_id = 'password'
        self.login_button_name = 'login-button'

    def open(self):
        self.driver.get('https://www.saucedemo.com')

    def enter_username(self, username):
        field = self.driver.find_element('id', self.username_field_id)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element('id', self.password_field_id)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        button = self.driver.find_element('name', self.login_button_name)
        button.click()


def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return 1



