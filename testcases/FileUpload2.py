import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
driver.back()
time.sleep(3)
driver.get("https://www.google.com")
driver.forward()
time.sleep(3)
driver.back()
time.sleep(3)
time.sleep(3)
print("Done!!!")