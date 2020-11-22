import selenium
import time

print(selenium.__version__)

#chrome://version/
#터미널 google-chrome --version
from selenium import webdriver
driver = webdriver.Chrome(executable_path='./chromedriver')
print(type(driver), driver)

driver.get(url="http://www.google.com/")
print(type(driver.page_source), driver.page_source)
time.sleep(1)
driver.quit()