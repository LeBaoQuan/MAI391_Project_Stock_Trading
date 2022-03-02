import os
cwd = os.getcwd()
os.chdir('D:\ml_project\mai391\stock_trading')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'https://raw.githubusercontent.com/LeBaoQuan/MAI391_Project_Stock_Trading/master/hvn30full.csv'
df = pd.read_csv(file_path)
df
#create list of column name
w=df.columns.tolist()
w

df_vnindex = pd.read_csv('vnindex30.csv')

# in column foredir, replace 0 with -1 for better visualization
df['foredir'].replace(0, -1, inplace = True)
df['foredir']

## split each stock into a df
df_stockName = {g: d for g, d in df.groupby('ticker')}
#example
df_stockName['BID']

## The value of each key in df_stockName, will be a DataFrame,
## which can be accessed as in df_stockName['key'].

# cach 2, for ease of use when iterating through many df
df_stockName2 = {f'df{i}': d for i, (g, d) in enumerate(df.groupby('ticker'))}
#example of BID stock
df_stockName2['df0']


## create a list of df corresponding to each stock
df = [0 for i in range (0,30)]
for i in range (0,30):
    df[i] = df_stockName2[f'df{i}']


df[0]
#change 'insec' in column name list to 'time'
w[w.index('insec')]='time'
df

## create lists of columns value (foredir, close, HL, LO, var, etc) of each df (size[30])
x = 0
for v in w:
  if v!='ticker':
    exec(v+'= [0 for i in range (0,30)]')
    #iterate x after every step
    x+=1
    for i in range(0,30):
      exec(v+'[i] = df[i].iloc[:,x]')

## plot some example graphs

plt.plot(time[0], close[0])
plt.title("Close value of "+df_stockName2[f'df{0}'].iloc[0].iloc[0])
plt.show()

## using bar chart to plot foredir
c = []
for i in foredir[0]:
    if i > 0:
        c.append('green')
    else:
        c.append('red')
plt.bar(time[0], foredir[0], color = c)
plt.title("Foredir value of "+df_stockName2[f'df{0}'].iloc[0].iloc[0])
plt.show()

#biểu đồ đường kết hợp:
  #tạo 2 cột Y
fig = plt.figure(figsize=(20,4))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
  #cột 1
ax1.bar(time[0], vnic[0], 0.5, color='blue', label='vnic')
ax1.set_ylabel('VNIC', color='blue')
  #cột 2
ax2.bar(time[0]+0.5, vnipc[0], 0.5, color='orange', label='vnipc')
ax2.set_ylabel('VNIPC', color='orange')
  #set lim 2 cái tỉ lệ nhau để điểm 0 trùng nhau
ax1.set_ylim(-75,55)
ax2.set_ylim(-7.5,5.5)
plt.legend(loc='upper left')
plt.title("VNIPC and VNIC value of "+df_stockName2[f'df{0}'].iloc[0].iloc[0])
plt.show()

## plot all graphs, trying to find patterns
fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot(111)
for i in range (0, 30):
    color = (np.random.rand(), np.random.rand(), np.random.rand())
    ax.plot(time[i], close[i], c=color, label = df_stockName2[f'df{i}'].iloc[0].iloc[0])
    plt.legend(loc = 'upper right', ncol=6, prop={'size': 15})
plt.title("Close value of all stocks")
ax.set_ylabel('CLOSE')

plt.plot(time[0],close[0])
plt.plot(time[0],vnic[0])
plt.plot(time[0],vnipc[0])
plt.show()


#vẽ vnindex, vn30index
df1 = pd.read_csv('https://raw.githubusercontent.com/LeBaoQuan/MAI391_Project_Stock_Trading/master/vnindex30.csv')
df1 = df1.iloc[::-1].reset_index(drop=True)
plt.figure(figsize=(20,4))
#tạo để sau
vn=df1['vnindex'].tolist()
vn30=df1['vn30index'].tolist()

df1['vn30index']= (df1['vn30index']-df1['vn30index'].min())/(df1['vn30index'].max()-df1['vn30index'].min())
df1['vnindex']= (df1['vnindex']-df1['vnindex'].min())/(df1['vnindex'].max()-df1['vnindex'].min())
df1.dropna()
df1.dropna(inplace =True)
day = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in df1['days']]
plt.plot(day, df1['vn30index'], label='vn30index')
plt.plot(day, df1['vnindex'], label='vnindex')
plt.legend()
plt.show()

#trung bình tăng giảm so với đứa trước theo %
for i in range(3015,0,-1):
  vn[i]=(vn[i]/vn[i-1])*100-100
  vn30[i]=(vn30[i]/vn30[i-1])*100-100
vn[0]=0
vn30[0]=0
#chuyển thành anda series
vn=pd.Series(vn)
vn30=pd.Series(vn30)

#vẽ graph
c=[]
for i in vn30:
  if i>0:
    c.append('tab:blue')
  else:
    c.append('red')
plt.figure(figsize=(20,2))
plt.bar(day,vn30,1,label='vn30index', color=c)
plt.title("Daily fluctuation of vn30index (%)")
plt.show()
c=[]
for i in vn:
  if i>0:
    c.append('green')
  else:
    c.append('tab:orange')
plt.figure(figsize=(20,2))
plt.bar(day,vn,1,label='vnindex',color=c)
plt.title("Daily fluctuation of vnindex (%)")
plt.show()

#so sánh BID BVH vnindex vn30index ở dạng normalised
plt.figure(figsize=(20,4))
plt.plot((ma7[1]-ma7[1].min())/(ma7[1].max()-ma7[1].min()),label='BVH')
plt.plot((ma7[0]-ma7[0].min())/(ma7[0].max()-ma7[0].min()),label='BID')
plt.plot((df1['vn30index']-df1['vn30index'].min())/(df1['vn30index'].max()-df1['vn30index'].min()),label='vn30index')
plt.plot((df1['vnindex']-df1['vnindex'].min())/(df1['vnindex'].max()-df1['vnindex'].min()),label='vnindex')
plt.legend()
plt.title('so sánh BID BVH vnindex vn30index')
plt.show()
