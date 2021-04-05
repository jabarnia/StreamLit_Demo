#from flask import Flask, render_template, request, redirect
import requests
import pandas as pd
import datetime
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt


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
month = st.selectbox('Month', range(1, 13))

yf_data = yf.Ticker(ticker)
# get stock info
st.write('Industry = ' + yf_data.info['industry'])
# get historical market data
start = str(year) + '-' + str(month) + '-01'
if month == 12:
    end = str(year + 1) + '-01-01'
else:
    end = str(year) + '-' + str(month + 1) + '-01'

if st.button('draw'):
    df = yf_data.history(start = start, end = end)
    df.reset_index(inplace = True)
    df['Date'] = df['Date'].dt.date
    df = df[['Date', 'Close']].set_index('Date')
    st.line_chart(df)
    

# app = Flask(__name__)
# # key = 93B6GO8P43HIO48E


# @app.route('/')
# def index():
#   return render_template('index.html')

# @app.route('/about')
# def about():
#   return render_template('about.html')

# if __name__ == '__main__':
#   app.run(port=33507)





