from selenium import webdriver
email = "kanushka@gmail.com"
password = "kanushka"
driver = webdriver.Chrome('chromedriver.exe')

driver.get("http://localhost/kanushka/")
driver.find_element_by_id("name").send_keys(email)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("login").click()
