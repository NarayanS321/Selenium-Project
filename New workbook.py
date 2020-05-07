from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\Chrome webdriver\chromedriver.exe")

driver.get("https://www.google.com/")

driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("facebook.com")

time.sleep(30)

driver.find_element_by_name("btnK").click()

time.sleep(15)

driver.find_element_by_id("gsr").click()


