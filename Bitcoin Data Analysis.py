#!/usr/bin/env python
# coding: utf-8

# In[222]:


#Import libaries


# In[223]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[224]:


#Read the file


# In[225]:


pd.read_csv(r'C:\Users\User\Downloads\Data Projects\Bitcoin Data Analysis/bitcoin_price_Training - Training.csv')


# In[226]:


#Store the file in dataframe


# In[227]:


df = pd.read_csv(r'C:\Users\User\Downloads\Data Projects\Bitcoin Data Analysis/bitcoin_price_Training - Training.csv')


# In[228]:


df.head(3)


# In[229]:


df.columns


# In[230]:


df.shape


# In[231]:


df.info()


# In[232]:


df.describe().T


# In[233]:


df.dtypes


# In[234]:


df['Date'] = df['Date'].astype('datetime64[ns]')

## pd.to_datetime()


# In[235]:


df['Date'].min()


# In[236]:


df['Date'].max()


# In[237]:


df['Date']


# In[238]:


#Data Pre-Processing


# In[239]:


#Check for missing values


# In[240]:


df.isnull().sum()


# In[241]:


#Check for duplicate values


# In[242]:


df.duplicated().sum()


# In[243]:


#Check the first 3 rows


# In[244]:


df.head(3)


# In[245]:


#Check the last 5 rows


# In[246]:


df.tail(5)


# In[247]:


#Sort data


# In[248]:


data = df.sort_index(ascending=False).reset_index()


# In[249]:


data


# In[250]:


data.drop('index', axis=1, inplace=True)


# In[251]:


data


# In[252]:


#Analysing change in price of the Bitcoin Overtime


# In[253]:


data.columns


# In[254]:


plt.figure(figsize=(20,12))

for index, col in enumerate(['Open', 'High', 'Low', 'Close'] , 1) :
    plt.subplot(2,2,index)
    plt.plot(df['Date'] , df[col])
    plt.title(col)


# In[255]:


#Analysing open, high, low, close value of bitcoin using candle stick chart


# In[256]:


data.shape


# In[257]:


bitcoin_sample = data[0:50]


# In[258]:


#set up the plotly package


# In[259]:


get_ipython().system('pip install chart_studio')
get_ipython().system('pip install plotly')


# In[260]:


import chart_studio.plotly as py

import plotly.graph_objs as go

import plotly.express as px

from plotly.offline import download_plotlyjs, init_notebook_mode, plot , iplot


# In[261]:


init_notebook_mode(connected=True)


# In[262]:


trace = go.Candlestick(x=bitcoin_sample['Date'], 
               high = bitcoin_sample['High'],
               open = bitcoin_sample['Open'],
               close = bitcoin_sample['Close'],
               low = bitcoin_sample['Low'])
                  


# In[263]:


candle_data = [trace]

layout = {
    'title':'Bitcoin Historical Price',
    'xaxis':{'title':'Data'}
}


# In[264]:


fig = go.Figure(data = candle_data , layout=layout)

fig.update_layout(xaxis_rangeslider_visible = False)
fig.show()


# In[265]:


data['Close']


# In[ ]:





# In[266]:


data['Close'].plot()


# In[ ]:





# In[267]:


data.set_index('Date')


# In[268]:


data


# In[269]:


data['Close'].plot()


# In[270]:


plt.figure(figsize=(20,6))

plt.subplot(1,2,1)
data['Close'].plot()
plt.title('No Scaling')

plt.subplot(1,2,2)
np.log1p(data['Close']).plot()
plt.title('Log Scaling')
plt.yscale('log')


# In[271]:


#Do a data analysis on closing price on yearly, quarterly, montlhy basis.


# In[272]:


data.set_index('Date')


# In[273]:


data.set_index('Date', inplace=True)


# In[274]:


data


# In[275]:


data.head(5)


# In[276]:


data.tail(3)


# In[277]:


data['Close'].resample('Y').mean()


# In[278]:


data['Close'].resample('Y').mean().plot()


# In[279]:


data['Close'].resample('Q').mean().plot()


# In[280]:


data['Close'].resample('M').mean()


# In[281]:


data['Close'].resample('M').mean().plot()


# In[282]:


#Analysing Daily Change in Closing Price of Stocks


# In[283]:


data['Close']


# In[284]:


data['Close'].pct_change()*100


# In[285]:


data['Close_price_pct_change'] = data['Close'].pct_change()*100


# In[286]:


data['Close_price_pct_change']


# In[287]:


data['Close_price_pct_change'].plot()


# In[288]:


import chart_studio.plotly as py

import plotly.graph_objs as go

import plotly.express as px

from plotly.offline import download_plotlyjs, init_notebook_mode, plot , iplot
init_notebook_mode(connected=True)


# In[290]:


get_ipython().system('pip install cufflinks')


# In[291]:


import cufflinks as cf


# In[292]:


cf.go_offline()


# In[293]:


data['Close_price_pct_change']


# In[299]:


type(data['Close_price_pct_change'])


# In[300]:


data['Close_price_pct_change'].iplot()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




