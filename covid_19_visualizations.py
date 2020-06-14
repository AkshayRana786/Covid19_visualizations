#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
matplotlib.rcParams["figure.figsize"] = (20,10)


# In[2]:


df = pd.read_csv("covid_19_data.csv",parse_dates=["ObservationDate","Last Update"])
df.head()


# In[3]:


new_df = df[["ObservationDate","Country/Region","Confirmed","Deaths","Recovered"]].values
df_new = pd.DataFrame(new_df,columns=["ObservationDate","Country/Region","Confirmed","Deaths","Recovered"])
df_new.head()
#df_new[df_new['ObservationDate'] == "2020-01-22"]


# In[4]:


date = df_new.groupby('ObservationDate')['ObservationDate'].agg('count')
date


# In[5]:


date = df_new.groupby('Country/Region')['Country/Region'].agg('count')
date


# In[6]:


date = df_new.groupby('ObservationDate')['Confirmed'].agg('count')
date


# In[7]:


data1 = df_new[['ObservationDate','Confirmed','Deaths','Recovered']].groupby(pd.Grouper(key = 'ObservationDate', freq = '1M')).sum()
data1


# In[8]:


data2 = data1.copy()
#data2.index = data2.index.strftime('%B')
data2['ObservationDate'] = data2.index
data2['Confirmed'] = data2['Confirmed'] / 1000
data2['Deaths'] = data2['Deaths'] / 1000
data2['Recovered'] = data2['Recovered'] / 1000
data2


# In[9]:


date = df_new.groupby('ObservationDate')
date


# In[10]:


ds = df_new[['ObservationDate','Confirmed','Deaths','Recovered']].groupby(pd.Grouper(key = 'ObservationDate')).sum()
ds['ObservationDate'] = ds.index
ds['Confirmed'] = ds['Confirmed'] / 1000
ds['Deaths'] = ds['Deaths'] / 1000
ds['Recovered'] = ds['Recovered'] / 1000
ds


# In[12]:


matplotlib.rcParams["figure.figsize"] = (15,10)
plt.scatter(ds['ObservationDate'], ds['Confirmed'], color='blue', label='Confirmed', s=50)
plt.scatter(ds['ObservationDate'], ds['Deaths'],marker='+', color='Red', label='Deaths', s=50)
plt.scatter(ds['ObservationDate'], ds['Recovered'],marker='*', color='Green', label='Recovered', s=50)
plt.xlabel("Time")
plt.ylabel("Case (1000)")
plt.title("Daily Data")
plt.legend()


# In[16]:


matplotlib.rcParams["figure.figsize"] = (15,10)
plt.plot(data2['ObservationDate'], data2['Confirmed'],marker=".", color='blue', label='Confirmed')
plt.plot(data2['ObservationDate'], data2['Deaths'],marker='+', color='Red', label='Deaths')
plt.plot(data2['ObservationDate'], data2['Recovered'],marker='*', color='Green', label='Recovered')
plt.xlabel("Time")
plt.ylabel("Case (1000)")
plt.title("Monthly Data (Observation Date)")
plt.legend()


# In[19]:


matplotlib.rcParams["figure.figsize"] = (15,10)
plt.plot(ds['ObservationDate'], ds['Confirmed'], color='blue', label='Confirmed',marker=".")
plt.plot(ds['ObservationDate'], ds['Deaths'], color='Red', label='Deaths',marker="+")
plt.plot(ds['ObservationDate'], ds['Recovered'], color='Green', label='Recovered',marker="*")
plt.xlabel("Time")
plt.ylabel("Case (1000)")
plt.title("Daily Data (Observation Date)")
plt.legend()


# In[46]:


matplotlib.rcParams["figure.figsize"] = (15,10)
plt.bar(data2['ObservationDate'], data2['Confirmed'], color='blue', label='Confirmed')
plt.bar(data2['ObservationDate'], data2['Deaths'], color='Red', label='Deaths')
plt.bar(data2['ObservationDate'], data2['Recovered'], color='Green', label='Recovered')
plt.xlabel("Time")
plt.ylabel("Case (1000)")
#plt.title(location)
plt.legend()


# In[28]:


data3 = df_new[['Country/Region','Confirmed','Deaths','Recovered']].groupby(pd.Grouper(key = 'Country/Region')).sum()
data4 = data3.sort_values(by ='Confirmed', ascending = 0).head(10)
data4


# In[29]:


ds4 = data4.copy()
ds4['Country'] = ds4.index
ds4['Confirmed'] = ds4['Confirmed'] / 1000
ds4['Deaths'] = ds4['Deaths'] / 1000
ds4['Recovered'] = ds4['Recovered'] / 1000
ds4


# In[35]:


matplotlib.rcParams["figure.figsize"] = (15,10)
plt.plot(ds4['Country'], ds4['Confirmed'],marker='.', color='blue', label='Confirmed')
plt.plot(ds4['Country'], ds4['Deaths'],marker='+', color='Red', label='Deaths')
plt.plot(ds4['Country'], ds4['Recovered'],marker='*', color='Green', label='Recovered')
plt.xlabel("Time")
plt.ylabel("Case (1000)")
plt.title("Top 10 Countrys")
plt.legend()

