import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
gmail=driver.find_element(By.LINK_TEXT,"Gmail")
ActionChains(driver).move_to_element(gmail).perform()
time.sleep(5)