from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

query = "무빙"

url = 'https://www.naver.co.kr/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

search_box = driver.find_element(By.CSS_SELECTOR, "#query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#lnb > div.lnb_group > div >
div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > 
div:nth-child(1) > a').click()
time.sleep(2)