from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://letskodeit.teachable.com/p/practice")

time.sleep(5)


class LetsCodeItWebPageTesting:

    def Multiple_Select_Example(self):
        multi_select = driver.find_element_by_id("multiple-select-example")

        drp = Select(multi_select)
        drp.select_by_visible_text("Apple")
        drp.select_by_visible_text("Orange")
        select_text2 = drp.all_selected_options
        for i in select_text2:
            print(i.text)

    def select_Class_Example(self):
        item_select = driver.find_element_by_xpath("//*[@id='carselect']")
        #drpdwn = driver.find_element_by_id("mycars")
        drop_down = Select(item_select)
        drop_down.select_by_visible_text("Benz")
        selected_item = drop_down.all_selected_options
        for i in selected_item:
            print(i.text)


mlt = LetsCodeItWebPageTesting()
mlt.Multiple_Select_Example()
mlt.select_Class_Example()
