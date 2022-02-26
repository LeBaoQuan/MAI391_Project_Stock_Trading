import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'https://raw.githubusercontent.com/LeBaoQuan/MAI391_Project_Stock_Trading/master/hvn30full.csv'
df = pd.read_csv(file_path)
df

## check if there's any null values
df.isnull().sum()

## extract all stock names into a dict
## split each stock in a df
df_stockName = {g: d for g, d in df.groupby('ticker')}
df_stockName.keys()
df_stockName

## The value of each key in df_dict, will be a DataFrame,
## which can be accessed in the standard way, df_stockName['key'].

# cach 2,
df_stockName2 = {f'df{i}': d for i, (g, d) in enumerate(df.groupby('ticker'))}
df_stockName2.keys()

## plot graphs
df_stockName2['df0']
# x-axis represent the time
# y-axis represent other variables (foredir, close, HL, LO, var)

#df0: BID
df_stockName2['df0']

x_BID = df_stockName['BID']['insec']

y_BID = [0 for i in range (0,5)]
for i in range (0,5):
    y_BID[i] = df_stockName['BID'].iloc[:,i+1]
    plt.plot(x_BID,y_BID[i])


#df1: BVH
df_stockName2['df1']
x_BVH = df_stockName['BVH']['insec']
y_BVH = [0 for i in range (0,5)]
for i in range (0,5):
    y_BVH[i] = df_stockName['BVH'].iloc[:,i+1]
    plt.plot(x_BVH, y_BVH[i])

plt.plot(x_BID, y_BID[1])
plt.plot(x_BVH, y_BVH[1])


## create a list of df corresponding to each stock
df = [0 for i in range (0,30)]

for i in range (0,30):
    df[i] = df_stockName2[f'df{1}']

for i in range (0,30):
    df[i]

## create a list x[30] represent a list of column insec value of each df
x = [0 for i in range (0,30)]

for i in range (0,30):
    x[i] = df[i].iloc[:,8]
x[i]

|## create a list y[13][30] represent a list of each 13 column of each df
y = [[0]*13 for i in range (0,30)]
for i in range (0,30):
    for j in range (0,13):
        y[i][j] = df[i].iloc[:,j]

## plot out graphs, each present a change in time of each values (foredir, close, HL, LO, var, etc)


for i in in range (0,30):
        plt.plot(x[i],y[i][2])


plt.plot(x[0], y[0][2], color= 'red')
plt.plot(x[0], y[0][3], color= 'green')
