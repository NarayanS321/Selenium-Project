from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://letskodeit.teachable.com/p/practice")
element = driver.find_element_by_id("hondacheck").click()



