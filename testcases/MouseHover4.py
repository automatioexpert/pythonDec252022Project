import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(14)
driver.get("https://www.flipkart.com/")
twoWheeler = driver.find_element(By.XPATH, "//div[contains(text(),'Two Wheelers')]")

action = ActionChains(driver)
action.move_to_element(twoWheeler).perform()
time.sleep(3)
electricVehicle = driver.find_element(By.LINK_TEXT, "Electric Vehicles")
electricVehicle.click()
time.sleep(10)
