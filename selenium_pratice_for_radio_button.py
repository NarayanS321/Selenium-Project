from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

#driver.get("https://letskodeit.teachable.com/p/practice")
driver.get("radiobtn.html")

time.sleep(15)
driver.find_element_by_xpath("/html/body/form/input[2]").click()
#driver.find_element_by_id("female").click()
time.sleep(2)
#radio_button =driver.find_element_by_xpath("//*[@id='bmwradio']").is_selected()
#print(radio_button)

radio_btns = driver.find_elements_by_name("gender")
for each_radio_btn in radio_btns:
    #print(each_radio_btn.text)
    if each_radio_btn.is_selected():
        print("selected:", each_radio_btn.text)
    else:
        print("Not selected:", each_radio_btn.text)

"""element = driver.find_element_by_id("carselect")

drp = Select(element)

drp.select_by_visible_text("Benz")
"""

