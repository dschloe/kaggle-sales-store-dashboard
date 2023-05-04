# -*- coding:utf-8 -*-
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import streamlit as st
from pathlib import Path

from utils import date_select, load_data

import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

@st.cache_data
def load_data():
    comp_dir = Path('data/store-sales-time-series-forecasting')
    train = pd.read_csv(comp_dir / 'train_sample_201516.csv')
    stores = pd.read_csv(comp_dir / 'stores.csv')
    oil = pd.read_csv(comp_dir / 'oil.csv')
    transactions = pd.read_csv(comp_dir / 'transactions.csv')
    holidays_events = pd.read_csv(comp_dir / 'holidays_events.csv')

    return train, stores, oil, transactions, holidays_events

@st.cache_resource(experimental_allow_widgets=True)
def show_data(train, stores, oil, transactions, holidays_events):
    st.markdown("## Data Preview")
    sample_ratio = st.sidebar.slider('Sample Ratio (0~1)', min_value=0.1, max_value=1.0, step=0.1)
    tab1, tab2, tab3, tab4 = st.tabs(['train', 'stores', 'oil', 'transactions'])

    with tab1:
        with st.expander("Train Data"):
            train_sample = train.sample(frac=sample_ratio)
            pr = train_sample.profile_report()
            st_profile_report(pr)
    with tab2:
        with st.expander("Stores Data"):
            stores_sample = stores.sample(frac=0.1)
            pr = stores_sample.profile_report()
            st_profile_report(pr)

    with tab3:
        with st.expander("Oil Data"):
            oil_sample = oil.sample(frac=0.1)
            pr = oil_sample.profile_report()
            st_profile_report(pr)

    with tab4:
        with st.expander("Transactions Data"):
            transactions_sample = transactions.sample(frac=0.1)
            pr = transactions_sample.profile_report()
            st_profile_report(pr)


def show_chart(train, stores, oil, transactions, holidays_events):

    oil = date_select(oil, col='date')
    oil = oil.set_index(['date'])
    moving_average_oil = oil.rolling(
        window=365,  # 365-day window
        center=True,  # puts the average at the center of the window
        min_periods=183,  # choose about half the window size
    ).median()  # compute the mean (could also do median, std, min, max, ...)

    oil = oil.reset_index()
    moving_average_oil = moving_average_oil.reset_index()

    moving_average_oil.loc[[0, 1], 'dcoilwtico'] = moving_average_oil.loc[2, 'dcoilwtico']
    moving_average_oil.date = pd.to_datetime(moving_average_oil.date)

    df_yr_oil = oil[['date', 'dcoilwtico']]
    fig = make_subplots(rows=1, cols=1, vertical_spacing=0.08,
                        subplot_titles=("Oil price during time"))
    fig.add_trace(
        go.Scatter(x=df_yr_oil['date'], y=df_yr_oil['dcoilwtico'], mode='lines', fill='tozeroy', fillcolor='#c6ccd8',
                   marker=dict(color='#496595'), name='Oil price'),
        row=1, col=1)
    fig.add_trace(go.Scatter(x=moving_average_oil.date, y=moving_average_oil.dcoilwtico, mode='lines', name='Trend'))
    fig.update_layout(height=350, bargap=0.15,
                      margin=dict(b=0, r=20, l=20),
                      title_text="Oil price trend during time",
                      template="plotly_white",
                      title_font=dict(size=25, color='#8a8d93', family="Lato, sans-serif"),
                      font=dict(color='#8a8d93'),
                      hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"),
                      showlegend=False)
    st.plotly_chart(fig)
    st.markdown(":pencil: **Interpret:**\n" 
    "- As can be seen in the graph above, we can divide the oil price trend into **<span style='color:#F1C40F'>three phases</span>**. The first and last of these, Jan2013-Jul2014 and Jan2015-Jul2107 respectively, show stabilised trends with ups and downs. However, in the second phase, Jul2014-Jan2015, oil prices decrease considerably. \n"
                "- Now, taking into account the issue of missing values for oil price, we are going to fill them by **<span style='color:#F1C40F'>backward fill technique</span>**. That means filling missing values with next data point (Forward filling means fill missing values with previous data", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

def run_eda():
    train, stores, oil, transactions, holidays_events = load_data()

    submenu = st.sidebar.selectbox("Submenu", ['Show Data', 'Charts'])
    if submenu == 'Show Data':
        show_data(train, stores, oil, transactions, holidays_events)
    elif submenu == 'Charts':
        show_chart(train, stores, oil, transactions, holidays_events)
    else:
        pass
