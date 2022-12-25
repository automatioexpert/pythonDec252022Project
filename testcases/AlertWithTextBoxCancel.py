import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
url="https://demo.automationtesting.in/Alerts.html"
driver.get(url)
driver.find_element(By.CSS_SELECTOR,"a[href*='Text']").click()
driver.find_element(By.CSS_SELECTOR,"button[onclick='promptbox()']").click()
time.sleep(4)
#Accepting / Dismissing alert prompts:

#Alert(driver).accept()
time.sleep(4)
Alert(driver).dismiss()
print(driver.find_element(By.CSS_SELECTOR,"p#demo1").text)
txt=driver.find_element(By.CSS_SELECTOR,"p#demo1").text
assert txt.__contains__("Hello Automation Testing user How are you today")

print("Alert Accept is accepted!!")