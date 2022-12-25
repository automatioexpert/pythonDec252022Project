import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.way2automation.com/way2auto_jquery/droppable.php#load_box")
#Switch to Frame
driver.switch_to.frame(0)
drag = driver.find_element(By.CSS_SELECTOR, "div#draggable")
drop = driver.find_element(By.CSS_SELECTOR, "div#droppable")
chains = ActionChains(driver)
chains.drag_and_drop(drag, drop).perform()
time.sleep(5)
