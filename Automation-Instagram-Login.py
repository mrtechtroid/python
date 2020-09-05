from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
credentials = open("logincred.txt").readlines()
username = credentials[0].replace('\n','')
password = credentials[1]
urlToUse = 'https://instagram.com'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(options=options)
driver.get(urlToUse)
usernamebox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//input[@name = "username"]')))
usernamebox.send_keys(username)
passwordbox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//input[@name = "password"]')))
passwordbox.send_keys(password)
passwordbox.send_keys(Keys.ENTER)

