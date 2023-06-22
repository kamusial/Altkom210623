import sys

import pytest
from selenium import webdriver
from selenium4_POM import *
from selenium2 import make_screenshot
import pytest
import pytest_html
import time

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
]

# @pytest.mark.parametrize('username, url', [('standard_user', 'https://www.saucedemo.com/inventory.html'), \
#                          ('locked_out_user', 'https://www.saucedemo.com/')])
@pytest.mark.skip(reason='duzy test')
@pytest.mark.parametrize('username, password, url', test_data)
def test_login_page(username, password, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    assert driver.current_url == 'https://www.saucedemo.com/'
    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    time.sleep(1)
    try:
        assert driver.current_url == url
    except AssertionError:
        print('Logowanie nie powiodlo sie')
        raise
    else:
        print('Logowanie poprawne')
    finally:
        print('koniec')
        driver.quit()


xfail = pytest.mark.xfail

@xfail
def test_one():
    assert api_v1() == 2


def test_two():
    if True:
        pytest.skip('zla konfiguracja')
    assert api_v2() == 1

skip_on_windows = pytest.mark.skipif(sys.platform == "win32", reason="tests for linux only")
@skip_on_windows
def test_three():
    assert api_v3() == 1

@pytest.mark.skipif(sys.version_info < (3, 10), reason='zly python')
def test_four():
    assert api_v4() == 1