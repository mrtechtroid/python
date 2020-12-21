# Github: Mr Techtroid
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
driver = webdriver.Chrome()
driver.get("https://10fastfingers.com/typing-test/english")
# driver.get("https://10fastfingers.com/competition/5f95787212d45")
typebox= WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//input[contains(@type, "text")]')))
time.sleep(10)
for i in range(349):
	highwordbox = driver.find_element_by_class_name('highlight')
	print(highwordbox.text)
	typebox.send_keys(highwordbox.text)
	typebox.send_keys(" ")
	time.sleep(0.0001)

