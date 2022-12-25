import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
url="https://demo.automationtesting.in/Alerts.html"
driver.get(url)
driver.find_element(By.CSS_SELECTOR,"a[href*='Cancel']").click()
driver.find_element(By.CSS_SELECTOR,"button[onclick='confirmbox()']").click()
time.sleep(4)
#Accepting / Dismissing alert prompts:

Alert(driver).accept()
time.sleep(4)
#Alert(driver).dismiss()
print("Alert is accepted!!")