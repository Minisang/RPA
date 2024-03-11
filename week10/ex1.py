from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = 'http://www.naver.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

query = "무빙"
search_box = driver.find_element(By.CSS_SELECTOR,"#query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(1) > a ').click()
time.sleep(2)

news_thumbnail = driver.find_elements(By.CSS_SELECTOR,"img._fe_image_tab_content_thumbnail_image")
link_thumbnail = []
for img in news_thumbnail:
    src = img.get_attribute('src')
    if "http" in src :
        link_thumbnail.append(src)
        print(src)
import os
path_folder = 'C:/Temp/image/'
if not os.path.isdir(path_folder):
    os.mkdir(path_folder)
#link에서 이미지 다운로드
from urllib.request import urlretrieve
i = 0
for link in link_thumbnail:
    i+=1
    urlretrieve(link, path_folder + f'{i}.jpg')