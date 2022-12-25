import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.way2automation.com/way2auto_jquery/tooltip.php")
#Switch to Frame
driver.switch_to.frame(0)
age=driver.find_element(By.CSS_SELECTOR,"#age")
ActionChains(driver).move_to_element(age).perform()
time.sleep(5)