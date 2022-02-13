from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import urljoin
import time
import lxml
# import requests


class ZillowData:

    def __init__(self, link, headers):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.options.add_argument('window-size=1440,1440')

        self.driver = webdriver.Chrome(executable_path="C:\Developement\Chromedriver.exe", options=self.options)
        self.link = link

        self.addresses = []
        self.links = []
        self.prices = []

        # response = requests.get(url=self.link, headers=headers)
        # print(response.status_code)
        # soup = BeautifulSoup(response.text, "lxml")
        self.use_soup()

    def use_soup(self):
        self.driver.get(self.link)

        time.sleep(10)

        #scroll down
        for _ in range(20):
            webdriver.ActionChains(self.driver).key_down(Keys.TAB).perform()
        for _ in range(120):
            webdriver.ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()

        page_source = self.driver.page_source

        soup = BeautifulSoup(page_source, 'lxml')
        self.driver.close()
        self.addresses = [address.text for address in soup.find_all(class_="list-card-addr")]
        self.prices = [price.text.replace("/mo", "").split("+")[0] for price in soup.find_all(class_="list-card-price")]
        self.links = [str(link.get('href')) for link in soup.find_all(class_="list-card-link")][1::2]

        for i in range(len(self.links)):
            if not self.links[i].startswith("http"):
                self.links[i] = "https://www.zillow.com" + self.links[i]
