from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = 'https://datalab.naver.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

menu_select = driver.find_element(By.CSS_SELECTOR,"#lnb > div > ul > li.list._keyword > a > span")
menu_select.click()
time.sleep(5)
query1 = "무빙"
search1_box = driver.find_element(By.CSS_SELECTOR,"#item_keyword1")
search1_box.send_keys(query1)

query2 = "디즈니플러스"
search2_box = driver.find_element(By.CSS_SELECTOR,"#item_keyword2")
search2_box.send_keys(query2)

year_select = driver.find_element(By.CSS_SELECTOR,"#content > div > div.keyword_trend > div.section_step > div > form > fieldset > div > div.form_row.hr > div.set_period")
year_select.click()

query_button = driver.find_element(By.CSS_SELECTOR,"#content > div > div.keyword_trend > div.section_step > div > form > fieldset > a")
query_button.click()
time.sleep(5)

down_button = driver.find_element(By.CSS_SELECTOR,"#content > div.section_keyword > div.keyword_trend > div.section_ca_board.w_space > div > div > div > div > div > div.graph_area > div.cont_file_down > a")
down_button.click()
time.sleep(5)