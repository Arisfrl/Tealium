from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
driver = webdriver.Chrome()
print(os.path.abspath(os.curdir))
driver.get("https://ecommerce.tealiumdemo.com/")
driver.find_element(By.XPATH,"//span[@class='label'][normalize-space()='Account']").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Register").click()
driver.save_screenshot("screenshot.png")