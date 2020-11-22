import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get(url="https://www.google.com/")

from selenium.webdriver.common.by import By
search_form = driver.find_element(By.TAG_NAME, "form")
print(type(search_form), search_form)

search_box = search_form.find_element(By.NAME, "q")
search_box.send_keys("webdriver")



driver.get(url="https://www.google.com/search?q=webdriver")
elements = driver.find_elements(By.XPATH, '//a[@href]')
for e in elements:
    if e != None:
        print(type(e.text), repr(e.text))

time.sleep(2)
driver.quit()