# import Append
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
from matplotlib.pyplot import figure

input_path = "/Users/arian/Documents/Programming/Price Scraper/Torob Scraper/Archive/"
#Append.appendiser(input_path)

df = pd.read_excel("Archive/Merged.xlsx")
df = df.drop(axis = 1, columns = "Unnamed: 0")
df = df.replace(0, np.nan)
df.set_index("Model", inplace = True)
x, y = df.shape
dates = list(df.columns)
df = df.T
names = list(df.columns)
df = df.T
for i in range(x):
    fig, ax = plt.subplots()
    plt.figure(figsize=(30, 30))  # for monthly report
    plt.plot(df.iloc[i])
    plt.xticks(rotation=90)
    plt.title(get_display( arabic_reshaper.reshape(names[i])))
    plt.ylabel('Price')
    plt.xlabel('Date')
    names[i] = names[i].replace("/"," R")
    s = ("Charts/" + names[i] + ".png")
    plt.savefig(s, bbox_inches="tight")
    plt.clf()
