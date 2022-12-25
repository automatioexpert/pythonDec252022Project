import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(25)
driver.get("https://www.flipkart.com/")
electronics = driver.find_element(By.XPATH, "//div[contains(text(),'Electronics')]")
audio = driver.find_element(By.LINK_TEXT, "Audio")
All = driver.find_element(By.LINK_TEXT, "All")

action = ActionChains(driver)
action.move_to_element(electronics)
action.move_to_element(audio)
action.move_to_element(All)
action.perform()
time.sleep(5)
print("Mouser hove done!!")
