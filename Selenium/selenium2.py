from selenium import webdriver
from time import sleep
import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


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
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.get('https://saucedemo.com/')
    #width = 1920
    #height = driver.execute_script('return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentELement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);')
    #height = driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    #driver.set_window_size(100, 100)
    #print(height)
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

    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
    driver.find_element(By.TAG_NAME,'body').screenshot('web_screenshot.png')

    driver.quit()

