from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\\Chrome webdriver\\chromedriver.exe")


driver.get("https://www.facebook.com/")
email_log = driver.find_element_by_xpath("//*[@id='email']")