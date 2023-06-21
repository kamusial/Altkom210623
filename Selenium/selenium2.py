from selenium import webdriver
from time import sleep
import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# def make_screenshot(przegladarka):
#     teraz=datetime.datetime.now()
#     nazwa = teraz.strftime('Screen_%H%M%S.png')
#     path1 = 'logi\\' + nazwa
#     path2 = 'C:\\Users\\Student\\Desktop\\Public\\now.png'
#     path3 = r'C:\Users\Student\Desktop\Public\now.png'
#     przegladarka.get_screenshot_as_file(path2)


def make_screenshot(przegladarka, sciezka=r'C:\Users\Student\Desktop\Public'):
    teraz=datetime.datetime.now()
    nazwa = teraz.strftime('Screen_%H%M%S.png')
    przegladarka.get_screenshot_as_file(sciezka+'\\'+nazwa)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://saucedemo.com/')
    print('Nazwa strony',driver.title)
    sleep(1)

    try:
        username_field = driver.find_element(By.ID, 'user-name')
    except NoSuchElementException:
        make_screenshot(driver)
        raise
    #    username_field = driver.find_element('id', 'user-name')  #znajdź poprawny

    username_field.clear()
    username_field.send_keys('standard_user')

    passwd_field = driver.find_element('xpath', '//*[@id="password"]')
    username_field.clear()
    passwd_field.send_keys('secret_sauce')
    sleep(1)
    login_button = driver.find_element('name', 'login-button')

    if not login_button.get_attribute('disabled'):
        login_button.click()

    sleep(1)
    make_screenshot(driver)
    print('Print selenium2')
    driver.quit()