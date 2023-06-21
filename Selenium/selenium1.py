from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()   #otwarte okno przeglądarki
time.sleep(1)
driver.get('https://google.com')
print('Nazwa strony',driver.title)
time.sleep(1)

button1_accept = driver.find_element('id', 'L2AGLb')
print(button1_accept)
button1_accept.click()
time.sleep(1)
search_field = driver.find_element('name', 'q')
search_field.send_keys('Wrocław wypadek rosomak')
time.sleep(1)
search_button = driver.find_element('name','btnK')
search_field.send_keys(Keys.ENTER)
#search_button.submit()

time.sleep(1)

driver.quit()