from selenium import webdriver

import time

class Facebook:

    def log_in_fb_project(self):
        driver = webdriver.Chrome(executable_path="D:\\Chrome webdriver\\chromedriver.exe")


        driver.get("https://www.facebook.com/")
        driver.find_element_by_xpath("//*[@id='email']").send_keys("muna.dhana@gmail.com")
        driver.find_element_by_xpath("//*[@id='pass']").send_keys("bonzer@7")
        time.sleep(20)
        driver.find_element_by_xpath("//*[@id='u_0_b']").click()

        time.sleep(40)
        driver.find_element_by_xpath("//*[@id='js_4m']/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div["
                                     "2]/div").send_keys("Hi how r u")
        driver.find_element_by_xpath("//*[@id='js_4f']/div[2]/div[3]/div[2]/button").click()


fb = Facebook()
fb.log_in_fb_project()

