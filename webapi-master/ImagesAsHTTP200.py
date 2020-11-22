import selenium
from selenium import webdriver
import wget
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.coupang.com/np/search?q=컴퓨터'
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get(url=url)
elements=driver.find_elements(By.XPATH, '//img[@class="search-product-wrap-img"]')
down_path = './pictures'
for element in elements:
    src = element.get_attribute('src')
    #download image
    img_txt = src.split('/')[-1]
    image_name = down_path+img_txt
    #첫번째 방법
    #wget.download(url=src, out=image_name)  #HTTP Error 403:Forbidden
    #두번째 방법
    with urllib.request.urlopen(src) as response, open(f'./pictures/{image_name}', 'wb') as out_file:
        data = response.read()
        out_file.write(data)