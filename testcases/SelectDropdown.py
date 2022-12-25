import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Register.html")
driver.find_element(By.CSS_SELECTOR, "#firstpassword").send_keys("P@ssw0rd7348488")
# identify dropdown with Select class
year = driver.find_element(By.ID, "yearbox")
sel = Select(year)
# select by select_by_visible_text() method
sel.select_by_value("1947")
time.sleep(5)

# Select Month
month = driver.find_element(By.CSS_SELECTOR, "[placeholder='Month']")
sel = Select(month)
sel.select_by_value("December")

# Select Date
day = driver.find_element(By.CSS_SELECTOR, "[placeholder='Day']")
day = Select(day)
day.select_by_value("25")
time.sleep(5)
day.select_by_index(4)
time.sleep(5)
print("All the values in the dropdown are selected")
