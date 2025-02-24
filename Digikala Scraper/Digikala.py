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
import numpy as np


price_dict = {'Model':[], 'Price':[]}
samsung_url = "https://www.digikala.com/samsung-brand/mobile-phone/?no_redirect=1&sort=21"
watch_url = "https://www.digikala.com/search/category-wearable-gadget/?brands%5B0%5D=18&brands%5B1%5D=10"
apple_url = "https://www.digikala.com/apple-brand/mobile-phone/?no_redirect=1&sort=21"
xiaomi_url = "https://www.digikala.com/xiaomi-brand/mobile-phone/?no_redirect=1&sort=21"
nokia_url = "https://www.digikala.com/nokia-brand/mobile-phone/?no_redirect=1&sort=21"
huawei_url = "https://www.digikala.com/huawei-brand/mobile-phone/?no_redirect=1&sort=21"
honor_url = "https://www.digikala.com/honor-brand/mobile-phone/?no_redirect=1&sort=21"
motorola_url = "https://www.digikala.com/motorola-brand/mobile-phone/?no_redirect=1&sort=21"
realme_url = "https://www.digikala.com/realme-brand/mobile-phone/?no_redirect=1&sort=21"
nothing_url = "https://www.digikala.com/nothing-brand/mobile-phone/?no_redirect=1&sort=21"
orod_url = "https://www.digikala.com/orod-brand/mobile-phone/?no_redirect=1&sort=21"
gplus_url = "https://www.digikala.com/g-plus-brand/mobile-phone/?no_redirect=1&sort=21"
oneplus_url = "https://www.digikala.com/oneplus-brand/mobile-phone/?no_redirect=1&sort=21"
glx_url = "https://www.digikala.com/glx-brand/mobile-phone/?no_redirect=1&sort=21"
daria_url = "https://www.digikala.com/daria-brand/mobile-phone/?no_redirect=1&sort=21"

name_place = "/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section[1]/div[2]/div[1]/div/div[%d]/a/div/article/div[2]/div[2]/div[2]/h2"
name_place_watch = "/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[3]/section/div[2]/div[%d]/a/div/article/div[2]/div[2]/div[2]/h3"
price_place = "/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section[1]/div[2]/div[1]/div/div[%d]/a/div/article/div[2]/div[2]/div[4]/div[1]/div/span"
price_place_watch = "/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[3]/section/div[2]/div[%d]/a/div/article/div[2]/div[2]/div[4]/div[1]/div/span"
price_place_sales = "/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section[1]/div[2]/div[1]/div/div[%d]/a/div/article/div[2]/div[2]/div[4]/div[1]/div[2]/span"
price_place_slaes_watch = "/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[3]/section/div[2]/div[%d]/a/div/article/div[2]/div[2]/div[4]/div[1]/div[2]/span"


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

def scrap(base_url):
    driver.implicitly_wait(30)
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)
    #driver.switch_to.default_content()
    #driver.switch_to.frame(driver.find_element_by_xpath("/html/body/iframe"))
    #wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,'iframe:not([id^=web-developer])')))

    try:
        for i in range(200):
            scrap_url_name = name_place % (i + 1)
            scrap_url_price = price_place % (i + 1)
            price = driver.find_element(By.XPATH, scrap_url_price).text
            if (price[:7] == "ناموجود"):
                break
            elif (price.rfind("٪") != -1):
                scrap_url_price = price_place_sales % (i + 1)
                price = driver.find_element(By.XPATH, scrap_url_price).text
            price = price.replace(",", "")
            int_price = english_numbers(price)
            model = driver.find_element(By.XPATH, scrap_url_name).text
            price_dict['Model'].append(model)
            price_dict['Price'].append(int_price)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    except:
        pass

def scrap_2(base_url):
    driver.implicitly_wait(30)
    driver.get(base_url)
#    try:
#        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/svg")
#    except:
#        pass

    try:
        for i in range(200):
            scrap_url_name = name_place_watch % (i + 1)
            scrap_url_price = price_place_watch % (i + 1)
            price = driver.find_element(By.XPATH, scrap_url_price).text
            if (price[:7] == "ناموجود"):
                break
            elif (price.rfind("٪") != -1):
                scrap_url_price = price_place_slaes_watch % (i + 1)
                price = driver.find_element(By.XPATH, scrap_url_price).text
            price = price.replace(",", "")
            int_price = english_numbers(price)
            model = driver.find_element(By.XPATH, scrap_url_name).text
            price_dict['Model'].append(model)
            price_dict['Price'].append(int_price)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    except:
        pass

def data_sort():
    header = ["Model"]
    df = pd.DataFrame.from_dict(price_dict)
    df.to_excel('/Users/arian/Documents/Programming/Price Scraper/Torob Scraper/digi_list.xlsx', columns = header, index = False)
    df.to_excel("output_digi.xlsx")


#service = Service('/Users/arian/Documents/Programming/Price Scraper/chromedriver')
#service.start()
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage') 
options.add_argument('--no-sandbox')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--blink-settings=imagesEnabled=false')

#driver = webdriver.Remote(service.service_url, options=options)
driver = webdriver.Chrome(options=options)
scrap(samsung_url)
scrap(apple_url)
scrap(xiaomi_url)
scrap(nokia_url)
scrap(huawei_url)
scrap(honor_url)
scrap(motorola_url)
scrap(realme_url)
scrap(nothing_url)
scrap(orod_url)
scrap(gplus_url)
scrap(oneplus_url)
scrap(glx_url)
scrap(daria_url)
scrap_2(watch_url)
driver.quit()

"""
driver = webdriver.Remote(service.service_url, options=options)
scrap_2(watch_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(apple_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(xiaomi_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(nokia_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(huawei_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(honor_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(motorola_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(realme_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(nothing_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(orod_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(gplus_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(oneplus_url)
driver.quit()

driver = webdriver.Remote(service.service_url, options=options)
scrap(glx_url)
driver.quit()
"""

data_sort()
