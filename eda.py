import pandas as pd
import plotly
import streamlit as st
from pathlib import Path

@st.cache_data
def load_data():
    comp_dir = Path('data/store-sales-time-series-forecasting')
    train = pd.read_csv(comp_dir / 'train_sample_201516.csv')
    stores = pd.read_csv(comp_dir / 'stores.csv')
    oil = pd.read_csv(comp_dir / 'oil.csv')
    transactions = pd.read_csv(comp_dir / 'transactions.csv')
    holidays_events = pd.read_csv(comp_dir / 'holidays_events.csv')

    return train, stores, oil, transactions, holidays_events

def show_data(train, stores, oil, transactions, holidays_events):
    st.markdown("## Train 데이터")
    st.dataframe(train, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## Stores 데이터")
    st.dataframe(stores, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## Oil 데이터")
    st.dataframe(oil, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## Transactions 데이터")
    st.dataframe(transactions, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## Holiday Events 데이터")
    st.dataframe(holidays_events, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

def run_eda():
    train, stores, oil, transactions, holidays_events = load_data()

    submenu = st.sidebar.selectbox("Submenu", ['Show Data', 'Charts'])
    if submenu == 'Show Data':
        show_data(train, stores, oil, transactions, holidays_events)
    elif submenu == 'Charts':
        pass

