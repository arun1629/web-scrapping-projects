# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:20:59 2023

@author: Arun
"""

#1. import html file to python

#2. price of stock 

#3 closing price of the stock

#4 52 week range (lower, upper)

#5 analyst rating

import requests 
from bs4 import BeautifulSoup
import pandas as pd

#importing html to python

url = 'https://www.marketwatch.com/investing/stock/msft?mod=search_symbol'

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')

#stock price
stock_price = soup.find('bg-quote',class_ = 'value' )
print("stock price: ", stock_price.text)

#closing price

closing_price = soup.find('td',class_ = 'table__cell u-semi')
print("closing price: ",closing_price.text)

#52 week range (lower , upper)

nested = soup.find('mw-rangebar', class_ = 'element element--range range--yearly')

lower = nested.findAll('span', class_ = 'primary')[0]

print("lower: ",lower.text)

upper = nested.findAll('span',class_ = 'primary')[1]
print("upper: ",upper.text)

#analyst rating

rating_ = soup.find('li', class_ = 'analyst__option active' )

print("rating",rating_.text)




















