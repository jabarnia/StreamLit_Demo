#from flask import Flask, render_template, request, redirect
import requests
import pandas as pd
import datetime
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource


##########

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
ticker_df = table[0]['Symbol']
ticker_list = ticker_df.sort_values().to_list()

##########

st.title('TDI 12 day milestone project')
st.write('April 2021 - Shiva Jabarnia')

##########

ticker = st.selectbox('Ticker', ticker_list)
year = st.selectbox('Year', range(2021,1990, -1))
month_text = st.selectbox('Month', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

month_num = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
month = month_num[month_text]

yf_data = yf.Ticker(ticker)
start = str(year) + '-' + str(month) + '-01'
if month == 12:
    end = str(year + 1) + '-01-01'
else:
    end = str(year) + '-' + str(month + 1) + '-01'

if st.button('show chart'):
    st.write('Industry: ' + yf_data.info['industry'])
    df = yf_data.history(start = start, end = end)
    df.reset_index(inplace = True)
    df['Date'] = df['Date'].dt.date
    df = df[['Date', 'Close']]
    #st.line_chart(df)
    
    source = ColumnDataSource(df)

    p = figure(title = ticker + ' stock Close price during ' + month_text + ' of year ' + str(year), x_axis_label = 'x' , y_axis_label = 'y')
    p.line(x = 'Date', y = 'Close', source = source , line_width = 2)
    st.bokeh_chart(p, use_container_width = True)