import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'https://raw.githubusercontent.com/LeBaoQuan/MAI391_Project_Stock_Trading/master/hvn30full.csv'
df = pd.read_csv(file_path)
df
## in column forefir, replace 0 with -1 for better visualization
## check if there's any null values
df.isnull().sum()

## extract all stock names into a dict
## split each stock in a df
df_stockName = {g: d for g, d in df.groupby('ticker')}
    #list all stock name
df_stockName.keys()


## The value of each key in df_dict, will be a DataFrame,
## which can be accessed in the standard way, df_stockName['key'].

# cach 2,
df_stockName2 = {f'df{i}': d for i, (g, d) in enumerate(df.groupby('ticker'))}
df_stockName2.keys()


#example
df_stockName2['df0']

## plot graphs
## create a list of df corresponding to each stock
df = [0 for i in range (0,30)]
for i in range (0,30):
    df[i] = df_stockName2[f'df{1}']
for i in range (0,30):
    df[i]

## create a list time[30] represent a list of column insec value of each df
time = [0 for i in range (0,30)]
for i in range (0,30):
    time[i] = df[i].iloc[:,8]

## foredir
foredir = [0 for i in range (0,30)]
for i in range (0,30):
    foredir[i] = df[i].iloc[:,1]

## create a list y_close[30] represent a list of column close value of each df
close = [0 for i in range (0,30)]
for i in range (0,30):
    close[i] = df[i].iloc[:,2]

## HL
hl = [0 for i in range (0,30)]
for i in range (0,30):
    hl[i] = df[i].iloc[:,3]

## lO
lo = [0 for i in range (0,30)]
for i in range (0,30):
    lo[i] = df[i].iloc[:,4]

## var
var = [0 for i in range (0,30)]
for i in range (0,30):
    var[i] = df[i].iloc[:,5]

## ma7
ma7 = [0 for i in range (0,30)]
for i in range (0,30):
    ma7[i] = df[i].iloc[:,9]

## ma14
ma14 = [0 for i in range (0,30)]
for i in range (0,30):
    ma14[i] = df[i].iloc[:,10]

## ma21
ma21 = [0 for i in range (0,30)]
for i in range (0,30):
    ma21[i] = df[i].iloc[:,11]

## sd7
sd = [0 for i in range (0,30)]
for i in range (0,30):
    sd[i] = df[i].iloc[:,12]

df[0].head()
plt.plot(time[0], close[0])
plt.plot(time[0], hl[0])
plt.plot(time[0], var[0])

plt.plot(close[0], foredir[0])
