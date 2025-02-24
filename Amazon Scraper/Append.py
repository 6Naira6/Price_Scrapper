import pandas as pd
import numpy as np
import os

def appendiser(input_path):
    excel_file_list = os.listdir(input_path)
    excel_file_list.sort()
    df = pd.DataFrame()
    model_list = []
    a = 1
    for name in excel_file_list:
        if name.endswith(".xlsx"):
            df = pd.read_excel(input_path + name)
            s = df['Model'].values
            temp = s.tolist()
            for item in temp:
                model_list.append(item)

    model_list = list(dict.fromkeys(model_list))
    df = pd.DataFrame(model_list, columns=['Model'])
    df.to_excel("Archive/00.xlsx")
    excel_file_list = os.listdir(input_path)
    excel_file_list.sort()
    for name in excel_file_list:
        if name.endswith(".xlsx"):
            if a == 1:
                df = pd.read_excel(input_path + name)
                df = df.drop(axis = 1, columns = "Unnamed: 0")
                df = df.rename(columns = {'Price': name.replace(".xlsx", "")})
                a = 2
            else:
                df1 = pd.read_excel(input_path + name)
                df1 = df1.drop(axis = 1, columns = "Unnamed: 0")
                df1 = df1.rename(columns = {'Price': name.replace(".xlsx", "")})
                df = df.merge(df1, how = 'left')

    df.fillna(value = 0, inplace = True)
    df.to_excel(input_path + "Merged.xlsx")
    os.remove("Archive/00.xlsx")

appendiser("/Users/arian/Documents/Programming/Price Scraper/Amazon Scraper/Archive/")
