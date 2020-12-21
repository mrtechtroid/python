# Github: Mr Techtroid
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
# a = input("Search Term:")
a = "Mr Techtroid"
url = "https://google.com"
driver = webdriver.Chrome()
driver.get(url)
searchBox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//input[contains(@title, "Search")]')))
searchBox.send_keys(a)
searchBox.send_keys(Keys.ENTER)



