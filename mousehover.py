'''from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path="D:\\Chrome webdriver\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(10)
admin = driver.find_element_by_id("menu_admin_viewAdminModule")
user_mng = driver.find_element_by_id("menu_admin_UserManagement")
users = driver.find_element_by_id("menu_admin_viewSystemUsers")
actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_mng).move_to_element(users).click().perform()'''


'''from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path="D:\\Chrome webdriver\\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
actions = ActionChains(driver)
actions.double_click(element).perform()'''

from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="D:\\Chrome webdriver\\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions = ActionChains(driver)
actions.context_click(button).perform()



