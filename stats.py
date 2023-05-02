# -*- coding:utf-8 -*-

import pandas as pd
import streamlit as st
from utils import load_data, date_select

from statsmodels.tsa.stattools import adfuller


def adfullerTest(oil):
    st.markdown("### Augmented Dickey-Fuller Test(ADF) \n"
                "#### What is ADF? \n"
                "- The Augmented Dickey-Fuller test is a type of statistical test called a unit root test. In probability theory and statistics, a unit root is a feature of some stochastic processes (such as random walks) that can cause problems in statistical inference involving time series models. In simple terms, the unit root is non-stationary but does not always have a trend component. \n"
                "- The unit root test is then carried out under the null hypothesis $\gamma = 0$.  Once a value for the test statistic")

    st.latex(r'''{\displaystyle \mathrm {DF} _{\tau }={\frac {\hat {\gamma }}{\operatorname {SE} ({\hat {\gamma }})}}}''')
    st.markdown(r"- is computed it can be compared to the relevant critical value for the Dickey–Fuller test. As this test is asymmetrical, we are only concerned with negative values of our test statistic ${\displaystyle \mathrm {DF} _{\tau }}$ If the calculated test statistic is less (more negative) than the critical value, then the null hypothesis of $\gamma = 0$ is rejected and no unit root is present.", unsafe_allow_html=True)
    st.markdown("#### Hypothesis \n"
                "- ADF test is conducted with the following assumptions: \n"
                "   + Null Hypothesis ($H_0$): Series is non-stationary, or series has a unit root. \n"
                "   + Alternate Hypothesis($H_A$): Series is stationary, or series has no unit root. \n"
                "- If Test statistic < Critical Value and $p-value < 0.05$\n"
                "   + Then, Reject Null Hypothesis($H_0$), i.e., time series does not have a unit root, meaning it is stationary. It does not have a time-dependent structure."
                )


    oil = date_select(oil, col='date')




def run_stat():
    train, stores, oil, transactions, holidays_events = load_data()

    submenu = st.sidebar.selectbox("Submenu", ['Time Series', 'Two Means'])
    if submenu == 'Time Series':
        st.markdown("## Time Series Analysis")
        adfullerTest(oil)
    elif submenu == 'Two Means':
        st.markdown("## Two Means")