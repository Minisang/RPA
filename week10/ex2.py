from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = 'https://trends.google.com/trends/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

menu_select = driver.find_element(By.CSS_SELECTOR,"#gb > div.gb_od.gb_id > div.gb_nd.gb_xd.gb_Re.gb_Be.gb_Qe.gb_Oe.gb_Se.gb_Ce > div.gb_de.gb_ce > div > div > div:nth-child(2) > div.VfPpkd-dgl2Hf-ppHlrf-sM5MNb > button")
menu_select.click() 
time.sleep(3)

query = "K-pop"
date_select = driver.find_element(By.CSS_SELECTOR,"#select_value_label_11 > span:nth-child(1) > div")
date_select.click()
year_select = driver.find_element(By.CSS_SELECTOR,"#select_option_15")
year_select.click()
search_box = driver.find_element(By.CSS_SELECTOR,"#input-29")
search_box.send_keys(query)
search_box.send_keys(Keys.ENTER)
time.sleep(5)
#select_value_label_172 > span:nth-child(1) > div
down_button = driver.find_element(By.CSS_SELECTOR,"body > div.trends-wrapper > div:nth-child(2) > div > md-content > div > div > div:nth-child(1) > trends-widget > ng-include > widget > div > div > div > widget-actions > div > button.widget-actions-item.export")
down_button.click()
time.sleep(10)