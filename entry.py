import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class EnterData:
    def __init__(self, g_link, addresses, prices, links):
        self.driver = webdriver.Chrome(executable_path="C:/Developement/Chromedriver.exe")
        self.driver.get(g_link)

        # for i in range(2):
        for i in range(len(addresses)):
            time.sleep(0.5)
            address_bar = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
            price_bar = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
            link_bar = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"

            self.driver.find_element_by_xpath(address_bar).send_keys(addresses[i])
            self.driver.find_element_by_xpath(price_bar).send_keys(prices[i])
            self.driver.find_element_by_xpath(link_bar).send_keys(links[i])

            self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()

            # next form
            self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
