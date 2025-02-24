import pandas as pd
import numpy as np
import os

def appendiser(input_path):
    excel_file_list = os.listdir(input_path)
    df = pd.DataFrame()
    a = 1
    for name in excel_file_list:
        if name.endswith(".xlsx"):
            if a == 1:
                df = pd.read_excel(input_path + name)
                df = df.drop(axis = 1, columns = "Unnamed: 0")
                a = 2
            else:
                df1 = pd.read_excel(input_path + name)
                df1 = df1.drop(axis = 1, columns = "Unnamed: 0")
                df = df.merge(df1, how = 'outer')

    df.fillna(value = 0, inplace = True)
    df = df.sort_values("Model")
    df.to_excel(input_path + "Merged.xlsx")

appendiser("/Users/arian/Documents/Programming/Price Scraper/Digi-Torob Merger/Archive/")
