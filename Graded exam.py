#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance==0.2.4')
get_ipython().system('mamba install bs4==4.10.0 -y')
get_ipython().system('pip install lxml==4.6.4')
get_ipython().system('mamba install html5lib==1.1 -y')


# In[2]:


import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd

Question 1 - Extracting Tesla Stock Data Using yfinance - 2 Points
# In[3]:


tesla = yf.Ticker("TSLA")
tesla.history(period='max')

Question 2 - Extracting Tesla Revenue Data Using Webscraping - 1 Points
# In[6]:


url = ("https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue")
data = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")
tables = soup.find_all('table')


# In[7]:


tesla2 = pd.DataFrame(columns=["Year", "Revenue"])
for row in tables[0].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        year = col[0].text
        revenue = col[1].text
        tesla2 = tesla2.append({"Year":year, "Revenue":revenue}, ignore_index=True)

tesla2

Question 3 - Extracting GameStop Stock Data Using yfinance - 2 Points
# In[8]:


gamestop = yf.Ticker("GME")
gamestop.history(period='max')

Question 4 - Extracting GameStop Revenue Data Using Webscraping - 1 Points
# In[11]:


url = ("https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue")
data = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")
tables = soup.find_all('table')


# In[12]:


gamestop2 = pd.DataFrame(columns=["Year", "Revenue"])
for row in tables[0].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        year = col[0].text
        revenue = col[1].text
        gamestop2 = gamestop2.append({"Year":year, "Revenue":revenue}, ignore_index=True)

gamestop2

Question 5 - Tesla Stock and Revenue Dashboard - 2 Points
# In[13]:


url = ("https://www.macrotrends.net/stocks/charts/TSLA/tesla/stock-price-history")
data = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")
tables = soup.find_all('table')


# In[14]:


#print(tables[0].prettify())

tesla1 = pd.DataFrame(columns=["Year", "Stock_Price"])
for row in tables[0].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        year = col[0].text
        stock = col[1].text
        tesla1 = tesla1.append({"Year":year, "Stock_Price":stock}, ignore_index=True)


# In[15]:


url = ("https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue")
data = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")
tables = soup.find_all('table')


# In[16]:


tesla2 = pd.DataFrame(columns=["Year", "Revenue"])
for row in tables[0].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        year = col[0].text
        revenue = col[1].text
        tesla2 = tesla2.append({"Year":year, "Revenue":revenue}, ignore_index=True)


# In[17]:


Tesla_Revenue_Stock = tesla1.merge(tesla2,how='left', on='Year')

Tesla_Revenue_Stock

Question 6 - GameStop Stock and Revenue Dashboard- 2 Points
# In[18]:


url = ("https://www.macrotrends.net/stocks/charts/GME/gamestop/stock-price-history")
data = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")
tables = soup.find_all('table')


# In[19]:


#print(tables[0].prettify())

gamestop1 = pd.DataFrame(columns=["Year", "Stock_Price"])
for row in tables[0].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        year = col[0].text
        stock = col[1].text
        gamestop1 = gamestop1.append({"Year":year, "Stock_Price":stock}, ignore_index=True)


# In[20]:


url = ("https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue")
data = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")
tables = soup.find_all('table')


# In[ ]:


gamestop2 = pd.DataFrame(columns=["Year", "Revenue"])
for row in tables[0].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        year = col[0].text
        revenue = col[1].text
        gamestop2 = gamestop2.append({"Year":year, "Revenue":revenue}, ignore_index=True)


# In[21]:


Gamestop_Revenue_Stock = gamestop1.merge(gamestop2,how='left', on='Year')

Gamestop_Revenue_Stock

