from selenium import webdriver
email = "kanushka@gmail.com"
password = "kanushka"
driver = webdriver.Chrome('chromedriver.exe')

driver.get("http://localhost/kanushka/")
driver.find_element_by_id("textfield1").send_keys("Kanushka")
driver.find_element_by_id("textfield2").send_keys("Gupta")
driver.find_element_by_id("textfield3").send_keys(email)
driver.find_element_by_id("textfield4").send_keys(password)
driver.find_element_by_id("register").click()
