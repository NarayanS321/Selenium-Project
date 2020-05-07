from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\Chrome webdriver\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))



for link in links:
    print([link.text],end='    ' )
    print([link.get_attribute("href")])


driver.quit()
