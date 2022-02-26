import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'https://raw.githubusercontent.com/LeBaoQuan/MAI391_Project_Stock_Trading/master/hvn30full.csv'
df = pd.read_csv(file_path)
df
#create list of column name
w=df.columns.tolist()

## in column forefir, replace 0 with -1 for better visualization
## check if there's any null values

## extract all stock names into a dict
## split each stock in a df
df_stockName = {g: d for g, d in df.groupby('ticker')}
   



## The value of each key in df_dict, will be a DataFrame,
## which can be accessed in the standard way, df_stockName['key'].

# cach 2,
df_stockName2 = {f'df{i}': d for i, (g, d) in enumerate(df.groupby('ticker'))}



#example
df_stockName2['df0']


## plot graphs
## create a list of df corresponding to each stock
df = [0 for i in range (0,30)]
for i in range (0,30):
    df[i] = df_stockName2[f'df{1}']


#change 'insec' in column name list to 'time'
w[w.index('insec')]='time'
## create lists of columns value of each df (size[30])
x = 0
for v in w:  
  if v!='ticker':
    exec(v+'= [0 for i in range (0,30)]')
    #iterate x after every step
    x+=1
    for i in range(0,30):
      exec(v+'[i] = df[i].iloc[:,x]')
    

df[0].head()
for i in range(0,30):
  plt.plot(time[i], close[i])
plt.show()
