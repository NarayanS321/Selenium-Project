from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()

driver.get("https://letskodeit.teachable.com/p/practice")

time.sleep(5)




class MultSelector:

    def Selected_by_drp(self):
        multi_select = driver.find_element_by_id("multiple-select-example")

        drp = Select(multi_select)
        drp.select_by_visible_text("Apple")
        drp.select_by_visible_text("Orange")
        select_text2 = drp.all_selected_options
        for i in select_text2:
            print(i.text)


mlt = MultSelector()
mlt.Selected_by_drp()
