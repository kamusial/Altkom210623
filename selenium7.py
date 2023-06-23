from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/")

# accept = driver.find_element('id', 'accept-choices')
# accept.click()

driver.maximize_window()
driver.find_element('id', 'accept-choices').click()
time.sleep(1)

# driver.find_element('id', 'navbtn_tutorials').click()
# driver.find_element('xpath', '//*[@id="nav_tutorials"]/div/div/div[2]/a[1]').click()

menu = driver.find_element('id', 'navbtn_tutorials')
HTMLtutorial = driver.find_element('xpath', '//*[@id="nav_tutorials"]/div/div/div[2]/a[1]')

webdriver.ActionChains(driver).move_to_element(menu).click().move_to_element(HTMLtutorial).click().perform()

HTML_form_attributes = driver.find_element('xpath','//*[@id="leftmenuinnerinner"]/a[40]')
HTML_form_attributes.click()

tryityourself = driver.find_element('xpath', '//*[@id="main"]/div[3]/a')
tryityourself.click()
print(driver.title)

currentWindowName = driver.current_window_handle
windowNames = driver.window_handles
#print(windowNames)

for okno in windowNames:
    if okno != currentWindowName:
        driver.switch_to.window(okno)

print(driver.title)

driver.switch_to.frame(driver.find_element(By.ID, 'iframeResult'))
firstName = driver.find_element(By.ID, 'fname')

if firstName.is_enabled():
    firstName.clear()
    firstName.send_keys('Kamil')
else:
    print('nie da sie kliknac')

driver.close()
driver.switch_to.window(currentWindowName)
print(driver.title)

#driver.back()

inputTypes = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[42]')
inputTypes.click()

tryCheckbox = driver.find_element('xpath', '//*[@id="main"]/div[13]/a')
tryCheckbox.click()

currentWindow_name = driver.current_window_handle
windowNames = driver.window_handles

for window in windowNames:
    if window != currentWindow_name:
        driver.switch_to.window(window)

print(driver.title)

driver.switch_to.frame(driver.find_element(By.ID, 'iframeResult'))

bike = driver.find_element(By.ID, 'vehicle1')
bike.click()
print('zaznaczyles ', driver.find_element('xpath', '/html/body/form/label[1]').text)
time.sleep(1)
driver.close()
driver.switch_to.window(currentWindowName)
time.sleep(1)
driver.quit()
