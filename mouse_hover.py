from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path = "D:\Chrome webdriver\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
more = driver.find_element_by_xpath("//*[@id='SW']/div[2]/div[2]/div/div/nav/ul/li[10]/a/span[2]/span[1]")
my_biz = driver.find_element_by_xpath("//*[@id='SW']/div[2]/div[2]/div/div/nav/ul/li[10]/div/a[1]")

actions = ActionChains(driver)
actions.move_to_element(more).move_to_element(my_biz).click().perform()
