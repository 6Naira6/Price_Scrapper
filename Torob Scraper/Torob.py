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


price_dict = {}
base_url = "https://torob.com/search/?query="
base_name_place1 = "/html/body/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[%d]/div[1]/div/div/a"
base_name_place2 = "/html/body/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div[%d]/div[1]/div/div/a"
base_price_place1 = "/html/body/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[%d]/div[3]/a[1]"
base_price_place2 = "/html/body/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div[%d]/div[3]/a[1]"
click_place = "/html/body/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/a/div/h2"
item_list = pd.read_csv("item_list.csv")

def english_numbers(price):
    price = price.replace('۰', '0')
    price = price.replace('۱', '1')
    price = price.replace('۲', '2')
    price = price.replace('۳', '3')
    price = price.replace('۴', '4')
    price = price.replace('۵', '5')
    price = price.replace('۶', '6')
    price = price.replace('۷', '7')
    price = price.replace('۸', '8')
    price = price.replace('۹', '9')
    return (int(price))

def scrap(phone):
    try:
        for i in range(4):
            scrap_url_name = base_name_place1 % (i + 1)
            scrap_url_price = base_price_place1 % (i + 1)
            price = driver.find_element(By.XPATH, scrap_url_price).text
            if (price[:7] == "ناموجود"):
                break
            price = price.replace("٫", "")
            price = price.replace(" تومان", "")
            int_price = english_numbers(price)
            shop = driver.find_element(By.XPATH, scrap_url_name).text
            shop = shop.replace("\u200c", " ")
            price_dict[phone]['Shop'].append(shop)
            price_dict[phone]['Price'].append(int_price)
    except:
        pass

    try:
        for i in range(200):
            scrap_url_name = base_name_place2 % (i + 5)
            scrap_url_price = base_price_place2 % (i + 5)
            price = driver.find_element(By.XPATH, scrap_url_price).text
            if (price[:7] == "ناموجود"):
                break
            price = price.replace("٫", "")
            price = price.replace(" تومان", "")
            int_price = english_numbers(price)
            shop = driver.find_element(By.XPATH, scrap_url_name).text
            shop = shop.replace("\u200c", " ")
            price_dict[phone]['Shop'].append(shop)
            price_dict[phone]['Price'].append(int_price)
    except:
        pass

def search(search_url, phone, a):
    driver.implicitly_wait(20)
    driver.get(search_url)
    try:
        driver.find_element(By.XPATH, click_place).click()
    except:
        pass

    # Makes it only look for Tehran based shops
    #if (a == 1):
        #driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/span").click()
        #driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/div[1]").click()
        #driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div[3]/div[1]").click()
        #driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]/div[1]/button").click()

    try:
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div").click()
    except:
        pass

    driver.implicitly_wait(1)
    scrap(phone)

def url_maker():
    a = 1
    col = item_list['Model']
    for phone in col:
        price_dict[phone] = {'Shop':[], 'Price':[]}
        search_name = phone.replace(" ", "%20")
        search_name = search_name.replace("/", "%2F")
        search_url = base_url + search_name
        search(search_url, phone, a)
        print("progress")
        a = 0

def ohe(stores, shop, price):
    thelist = [0] * len(stores)
    for i, value in enumerate(stores):
        if value in shop:
            x = shop.index(value)
            thelist[i] = price[x]
    return thelist

def priority_sort(df):
    df2 = df.loc[["جی جی مو", "کالاتیک",  "موبایل 140", "تکنولایف", "موبودیجی", "مقداد آی تی", "لوتوس", "19 کالا", "گوشی شاپ", "دیجی دو"], : ]
    df2.to_excel("prio_output.xlsx")

def analysis(df):
    df1 = df.replace(0, np.nan)
    df_analysis = df1.describe()
    df_analysis.to_excel("analysis.xlsx")
    analysis_dict = {}
    for phone in price_dict:
        mean = df1[phone].mean()
        std = df1[phone].std()
        for i, price in enumerate(df1[phone]):
            if (price > mean + std) or (price < mean - std):
                df1[phone][i] = 0
        df2 = df1.replace(0, np.nan)
        mean = df2[phone].mean()
        std = df2[phone].std()
        min = df2[phone].min()
        max = df2[phone].max()
        tfp = df2[phone].quantile(0.25)
        fp = df2[phone].quantile(0.50)
        sfp = df2[phone].quantile(0.75)
        analysis_dict[phone] = [mean, std, min, tfp, fp, sfp, max]
    df_analysis = pd.DataFrame.from_dict(analysis_dict)
    df_analysis.index = ["mean", "std", "min", "25%", "50%", "75%", "max"]
    df_analysis.to_excel("analysis.xlsx")

def data_sort():
    stores = []
    for phone in price_dict.values():
        stores += phone['Shop']        

    stores = list(dict.fromkeys(stores))
    #print(stores)
    #stores = list(set(stores))
    new_dict = {}
    for phone in price_dict:
        new_dict[phone] = ohe(stores, price_dict[phone]['Shop'], price_dict[phone]['Price'])
    df = pd.DataFrame.from_dict(new_dict)
    df.index = stores
    df.to_excel("output.xlsx")
    analysis(df)
    #priority_sort(df)


service = Service('/Users/arian/Documents/Programming/Price Scraper/chromedriver')
service.start()
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Remote(service.service_url, options=options)

url_maker()
data_sort()
# print(price_dict)
pickle_out = open("donttouchmypicklebro.pickle", 'wb')
pickle.dump(price_dict, pickle_out)
pickle_out.close()
