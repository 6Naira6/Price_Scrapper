import pandas as pd
import numpy as np
import os

def appendiser(input_path):
    excel_file_list = os.listdir(input_path)
    excel_file_list.sort()
    df = pd.DataFrame()
    a = 1
    for name in excel_file_list:
        if name.endswith("ana.xlsx"):
            if a == 1:
                df2 = pd.read_excel(input_path + name)
                df2 = df2.rename(columns = {"Unnamed: 0": "Model"})
                df = df2.T
                df.columns = [0,1,2,3,4,5,6]
                df = df.rename(columns = {0: name.replace(" ana.xlsx", "")})
                df = df.drop(axis = 1, columns = 1)
                df = df.drop(axis = 1, columns = 2)
                df = df.drop(axis = 1, columns = 3)
                df = df.drop(axis = 1, columns = 4)
                df = df.drop(axis = 1, columns = 5)
                df = df.drop(axis = 1, columns = 6)
                df.columns = df.iloc[0]
                df = df.rename(columns = {"mean": name.replace(" ana.xlsx", "")})
                df = df.drop(axis = 0, index = "Model")
                df.reset_index(inplace = True, drop = False)
                df = df.rename(columns = {"index": "Model"})
                a = 2
            else:
                df2 = pd.read_excel(input_path + name)
                df2 = df2.rename(columns = {"Unnamed: 0": "Model"})
                df1 = df2.T
                df1 = df1.rename(columns = {0: name.replace(" ana.xlsx", "")})
                df1 = df1.drop(axis = 1, columns = 1)
                df1 = df1.drop(axis = 1, columns = 2)
                df1 = df1.drop(axis = 1, columns = 3)
                df1 = df1.drop(axis = 1, columns = 4)
                df1 = df1.drop(axis = 1, columns = 5)
                df1 = df1.drop(axis = 1, columns = 6)
                df1.columns = df1.iloc[0]
                df1 = df1.rename(columns = {"mean": name.replace(" ana.xlsx", "")})
                df1 = df1.drop(axis = 0, index = "Model")
                df1.reset_index(inplace = True, drop = False)
                df1 = df1.rename(columns = {"index": "Model"})
                df = df.merge(df1, how = 'left')

    df.fillna(value = 0, inplace = True)
    df.to_excel(input_path + "Merged.xlsx")

appendiser("Archive/")
