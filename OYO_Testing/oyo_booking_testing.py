import time
from selenium.webdriver.ui import Webdriverwait

from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(3)


class OyoRoom:

    def oyoroom_testing(self):
        base_url = driver.get("https://www.oyorooms.com/")
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="autoComplete__home"]').send_keys("Bhubaneswar")
        find_location = driver.find_element_by_xpath(
            "//*[@id='root']/div/div[3]/div[1]/div[3]/div/div/div/div[1]/div/span/div/div/div[1]")
        find_location.click()

        search_date = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[3]/div[1]/div[3]/div/div/div/div[2]/div/div')
        search_date.click()
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div[3]/div[1]/div[3]/div/div/div/div[2]/div/span/div/div/div[3]/table/tbody/tr["
            "1]/td[3]/span").click()
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div[3]/div[1]/div[3]/div/div/div/div[2]/div/span/div/div/div[3]/table/tbody/tr["
            "1]/td[5]/span").click()
        search_room_guest = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]/div[3]/div/div["
                                                         "1]/div/div[3]/div/div")
        search_room_guest.click()
        add_guest = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]/div[3]/div/div[1]/div/div["
                                                 "3]/div/span/div/div[2]/div[1]/div/div[2]/span[3]")
        add_guest.click()
        add_room = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]/div[3]/div/div[1]/div/div["
                                                "3]/div/span/div/div[3]/div/div[2]/button")
        add_room.click()
        search_button = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]/div[3]/div/div/div/div["
                                                     "4]/button")
        search_button.click()

        collection_radio_button = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div[2]/aside/div["
                                                               "2]/div[3]/div/div/label[1]/span")
        collection_radio_button.click()


oyo = OyoRoom()
oyo.oyoroom_testing()
