import time

from selenium import webdriver

driver = webdriver.Chrome()


class Youtube:

    def play_music_on_youtube(self, search_song):
        driver.get("https://www.youtube.com/")

        driver.find_element_by_xpath(
            "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys(search_song)
#        driver.maximize_window()
        driver.find_element_by_xpath(
            "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button/yt-icon").click()
        time.sleep(5)
        second_result = "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]"
        driver.find_element_by_xpath(second_result).click()

        #driver.find_element_by_xpath(
        #    "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string").click()


yb = Youtube()
searchsong = "tum hi ho" #"dil hi"
yb.play_music_on_youtube(searchsong)
