from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
#driver.get("https://letskodeit.teachable.com/p/practice")
driver.get("file:///C:/Users/NARAYAN%20SAHOO/PycharmProjects/Selenium%20Project/letskodepage.html")

time.sleep(5)
#item_select = driver.find_elements_by_xpath("//*[@id='carselect']")
drpdwn = driver.find_element_by_id("mycars")
drop_down = Select(drpdwn)
drop_down.select_by_visible_text("Benz")
selected_item = drop_down.all_selected_options
for i in selected_item:
    print(i.text)

