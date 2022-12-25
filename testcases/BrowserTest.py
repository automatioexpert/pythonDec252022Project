from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
src=driver.page_source
assert src.__contains__("Google")
print('Test Case Passed')
driver.quit()
