from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\Chrome webdriver\chromedriver.exe")

#driver.get("https://www.makemytrip.com/")

driver.f

driver.get("https://www.google.com/")
driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("new hind movie")

time.sleep(15)
#driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()
driver.find_element_by_name("btnK").click()


#time.sleep(50)

#driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input").send_keys("BBI")

#driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input").send_keys("BBI")
#driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/input").send_keys("CCU")

#driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div[2]/p/a").click()


#time.sleep(10)
#driver.close()