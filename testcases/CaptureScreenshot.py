import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
url = "https://demo.automationtesting.in/Alerts.html"
driver.get(url)
driver.find_element(By.CSS_SELECTOR, "a[href*='Text']").click()

pic1 = driver.get_screenshot_as_png()
print(type(pic1))
title = driver.execute_script('return document.title;')
print(title)
# print(pic1)
# driver.save_screenshot('./s2.png')
# driver.save_full_page_screenshot('/Screenshots/foo.png')
print("Alert Accept is accepted!!")
driver.fullscreen_window()
print(driver.get_window_position())
#print(driver.get_window_rect().get())
print(driver.get_window_size())
driver.refresh()
print(driver.page_source)