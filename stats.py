# -*- coding:utf-8 -*-

import pandas as pd
import streamlit as st
from utils import load_data
from statsmodels.tsa.stattools import adfuller

def adfullerTest(data):
    st.markdown("### Augmented Dickey-Fuller Test(ADF) \n"
                "#### What is ADF? \n"
                "- The Augmented Dickey-Fuller test is a type of statistical test called a unit root test. In probability theory and statistics, a unit root is a feature of some stochastic processes (such as random walks) that can cause problems in statistical inference involving time series models. In simple terms, the unit root is non-stationary but does not always have a trend component. \n"
                "- ")



def run_stat():
    train, stores, oil, transactions, holidays_events = load_data()

    submenu = st.sidebar.selectbox("Submenu", ['Time Series', 'Two Means'])
    if submenu == 'Time Series':
        st.markdown("## Time Series Analysis")
        adfullerTest(train)
    elif submenu == 'Two Means':
        st.markdown("## Two Means")