from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
googleSearchBtn=driver.find_element(By.XPATH,"(//input[@value='Google Search'][@name='btnK'])[2]")

actions= ActionChains(driver)
actions.move_to_element(googleSearchBtn)
actions.context_click(googleSearchBtn)
actions.perform()
