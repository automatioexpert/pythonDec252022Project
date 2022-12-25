import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.eggradients.com/tool/double-click-test")

#element
clickHere=driver.find_element(By.XPATH, "//img[@class='tool-image ezlazyloaded']")
##action chain object
action=ActionChains(driver)
#double click operation
action.double_click(clickHere)
action.double_click(clickHere)
print("Double click done")
time.sleep(5)