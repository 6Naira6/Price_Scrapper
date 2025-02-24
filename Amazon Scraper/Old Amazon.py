from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import pickle
import numpy as np


price_dict = {'Model':[], 'Price':[]}
base_url = "https://www.amazon.ae/stores/page/917345DC-9ACC-4D6E-9B8E-835576113E75?ingress=2&visitId=abec095c-efcd-48cc-aa49-e57aa5f62e8f&ref_=ast_bln#nav-top"
name_place = "/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/ul/li[%d]/div[2]/div[4]/div[1]/div[1]/a"
price_place = "/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/ul/li[%d]/div[2]/div[4]/div[1]/div[3]/span/span/span[2]"
price_place_2 = "/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/ul/li[%d]/div[2]/div[4]/div[1]/div[2]/span/span/span[2]"    #no review
button_place = "/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/div[2]/button"
search_url = "https://www.amazon.ae/stores/page/1DA767D8-9DEB-4DAC-ADFC-503CA2F3BBDD/search?ingress=2&visitId=abec095c-efcd-48cc-aa49-e57aa5f62e8f&ref_=ast_bln&terms=XXXXXX#nav-top"
list_model = ["A04", "A23", "A33", "A53", "A73", "A24", "A34", "A54"]


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def scrap():
    driver.implicitly_wait(2)
    driver.get(base_url)

    try:
        for i in range(10):
            if (check_exists_by_xpath(button_place) == True):
                driver.find_element_by_xpath(button_place).click()
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    except:
        pass

    for i in range(200):
        scrap_url_name = name_place % (i + 1)
        scrap_url_price = price_place % (i + 1)
        if (check_exists_by_xpath(scrap_url_name) == False):
            break
        try:
            price = driver.find_element(By.XPATH, scrap_url_price).text
        except:
            try:
                scrap_url_price = price_place_2 % (i + 1)
                price = driver.find_element(By.XPATH, scrap_url_price).text
            except:
                continue
        price = price.replace(",", "")
        int_price = int(price)
        model = driver.find_element(By.XPATH, scrap_url_name).text
        price_dict['Model'].append(model)
        price_dict['Price'].append(int_price)

    for i in range(5):
        test = search_url.replace("XXXXXX", list_model[i])
        driver.get(test)
        for i in range(20):
            scrap_url_name = name_place % (i + 1)
            scrap_url_price = price_place % (i + 1)
            try:
                price = driver.find_element(By.XPATH, scrap_url_price).text
            except:
                try:
                    scrap_url_price = price_place_2 % (i + 1)
                    price = driver.find_element(By.XPATH, scrap_url_price).text
                except:
                    continue
            try:
                price = price.replace(",", "")
                int_price = int(price)
                model = driver.find_element(By.XPATH, scrap_url_name).text
                if model not in price_dict['Model']:
                    price_dict['Model'].append(model)
                    price_dict['Price'].append(int_price)
            except:
                pass


def data_sort():
    df = pd.DataFrame.from_dict(price_dict)
    df.to_excel("output_amazon.xlsx")


service = Service('/Users/arian/Documents/Programming/Price Scraper/chromedriver')
service.start()
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Remote(service.service_url, options=options)

scrap()
data_sort()
