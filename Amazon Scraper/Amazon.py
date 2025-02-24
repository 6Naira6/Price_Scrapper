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
name_place = "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[%d]/div/div/div/div/div[2]/div[1]/h2/a/span"
price_place = "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[%d]/div/div/div/div/div[2]/div[3]/div/a/span/span[2]/span[2]"
price_place_2 = "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[%d]/div/div/div/div/div[2]/div[2]/div/a/span/span[2]/span[2]"    # no review    
price_place_3 = "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[%d]/div/div/div/div/div[2]/div[4]/div/a/span/span[2]/span[3]"    # sale
button_place = "/html/body/div[1]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/button"
search_url = "https://www.amazon.ae/s?k=XXXXXX&i=electronics&rh=n%3A11601326031%2Cn%3A12303750031%2Cn%3A15415001031&dc&ds=v1%3Aw3ExLvQHQfU8wbcRIIwWFJysGdbBm7DLU7pkDAX9sC4&qid=1686038800&rnid=11601326031&ref=sr_nr_n_3"
list_model = ["A04", "A13", "A14", "A23", "A24", "A33", "A34", "A53", "A54", "A73", "S21+FE", "S23+ultra"]


def scrap():
    for names in list_model:
        test = search_url.replace("XXXXXX", names)
        driver.implicitly_wait(1)
        driver.get(test)
        print(names)
        for i in range(23):
            scrap_url_name = name_place % (i + 1)
            scrap_url_price = price_place % (i + 1)
            try:
                price = driver.find_element(By.XPATH, scrap_url_price).text
            except:
                try:
                    scrap_url_price = price_place_2 % (i + 1)
                    price = driver.find_element(By.XPATH, scrap_url_price).text
                except:
                    try:
                        scrap_url_price = price_place_3 % (i + 1)
                        price = driver.find_element(By.XPATH, scrap_url_price).text
                    except:
                        continue
            try:
                price = price.replace(",", "")
                int_price = int(price)
                model = driver.find_element(By.XPATH, scrap_url_name).text
                if model not in price_dict['Model']:
                    if ((names in model) or ("S21 (FE)")) and ("Samsung Galaxy" in model):
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
options.add_argument('--headless')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--blink-settings=imagesEnabled=false')
#driver = webdriver.Remote(service.service_url, options=options)
driver = webdriver.Chrome(options=options)


scrap()
data_sort()
