from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\\Chrome webdriver\\chromedriver.exe")


driver.get("https://www.odisha.gov.in/")

element = driver.find_element_by_class_name("dropdown-toggle")


drp = Select(element)

drp.select_by_visible_text("State Assembly")
print(len(drp.options))






