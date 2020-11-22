import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get(url="https://www.google.com/")

driver.find_element(By.NAME, "q").send_keys("webdriver"+Keys.ENTER)


SearchInput = driver.find_element(By.NAME, "q")
#SearchInput = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
SearchInput.send_keys("selenium")
SearchInput.clear()
