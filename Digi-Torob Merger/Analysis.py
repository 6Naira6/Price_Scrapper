import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display


df = pd.read_excel("Archive/Merged.xlsx")
df = df.drop(axis = 1, columns = "Unnamed: 0")
df = df.replace(0, np.nan)
df.set_index("Model", inplace = True)
x, y = df.shape
dates = list(df.columns)
df = df.T
names = list(df.columns)
df = df.T
al = 0
for i in range(int(x)):
    plt.figure(figsize=(30, 30))  # for monthly report

    if al == 5:
        al = 0
        continue

    if ((names[i].replace(" Digi", "")) == (names[i + 1].replace(" Torob", ""))):
        plt.plot(df.iloc[i], label = "Digi")
        plt.plot(df.iloc[i + 1], label = "Torob")
        plt.legend()
        plt.xticks(rotation=90)
        plt.title(get_display( arabic_reshaper.reshape(names[i])))
        plt.ylabel('Price')
        plt.xlabel('Date')
        names[i] = names[i].replace("/"," R")
        s = ("Charts/" + names[i].replace(" Digi", "") + ".png")
        plt.savefig(s, bbox_inches="tight")
        plt.clf()
        al = 5
