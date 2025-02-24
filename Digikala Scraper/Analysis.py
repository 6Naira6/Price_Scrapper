# import Append
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

input_path = "/Users/arian/Documents/Programming/Price Scraper/Digikala Scraper/Archive/"
# Append.appendiser(input_path)

df = pd.read_excel("Archive/Merged Per.xlsx")
df = df.drop(axis = 1, columns = "Unnamed: 0")
df.set_index("Model", inplace = True)
df = df.replace(0, np.nan)
df2 = pd.read_excel("Archive/Merged En.xlsx")
df2 = df2.drop(axis = 1, columns = "Unnamed: 0")
df2.set_index("Model", inplace = True)
df2 = df2.T
save_names = list(df2.columns)
x, y = df.shape
dates = list(df.columns)
df = df.T
names = list(df.columns)
df = df.T
for i in range(x):
    plt.figure(figsize=(30, 30))  # for monthly report
    plt.plot(df.iloc[i])
    plt.xticks(rotation=90)
    plt.title(get_display( arabic_reshaper.reshape(names[i])))
    plt.ylabel('Price')
    plt.xlabel('Date')
    #names[i] = names[i].replace(" ","_")
    s = ("Charts/" + save_names[i].replace("/"," R") + ".png")
    plt.savefig(s, bbox_inches="tight")
    plt.clf()
