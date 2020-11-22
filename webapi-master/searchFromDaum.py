import selenium
import time

print(selenium.__version__)

#chrome://version/
#터미널 google-chrome --version
from selenium import webdriver
driver = webdriver.Chrome(executable_path='./chromedriver')
print(type(driver), driver)

driver.get(url="http://www.daum.net/")
from selenium.webdriver.common.by import By
search_form = driver.find_element(By.TAG_NAME, "form")
search_box = search_form.find_element(By.NAME, "q")
search_box.send_keys("딥러닝")