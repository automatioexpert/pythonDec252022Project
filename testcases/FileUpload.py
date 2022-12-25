import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='First Name']").send_keys("User3474734")
#driver.find_element(By.CSS_SELECTOR,"input#imagesrc").click()
#driver.find_element(By.CSS_SELECTOR,"input#imagesrc").send_keys("C:\\Users\\valmiki\\Desktop\\vv.png")
file=driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file.send_keys("C:\\Users\\valmiki\\Desktop\\vv.png")
time.sleep(5)
print("File Upload successfully")
