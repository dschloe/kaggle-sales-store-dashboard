# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from utils import load_data

import streamlit as st

def total_Sales(train, stores):
    st.title("Total Sales")
    # 데이터 타입 변환
    train.onpromotion = train.onpromotion.astype("float16")
    train.sales = train.sales.astype("float32")
    stores.cluster = stores.cluster.astype("int8")
    train['date'] = pd.to_datetime(train['date'])
    train = train.set_index('date')
    train = train.drop('id', axis=1)
    train[['store_nbr', 'family']] = train[['store_nbr', 'family']].astype('category')
    fig, ax = plt.subplots(figsize=(18, 7))
    ax.set(title="'Total Sales Across All Stores")
    total_sales = train.sales.groupby("date").sum()
    ax.plot(total_sales)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.axvline(x=pd.Timestamp('2016-04-16'), color='r', linestyle='--', linewidth=4, alpha=0.3)
    ax.text(pd.Timestamp('2016-04-20'), 1400000, 'The Earthquake', rotation=360, c='r')
    plt.xticks(rotation=70)
    st.pyplot(fig)
    st.markdown("설명 추가로 넣어주세요!")
    # 각 스토어의 일일 총 판매량 딕셔너리로 만들기
    daily_sale_dict = {}
    for i in train.store_nbr.unique():
        daily_sale = train[train['store_nbr'] == i]
        daily_sale_dict[i] = daily_sale
    # 위의 결과를 시각화하는데 지진 표시되게 함
    fig = plt.figure(figsize=(30, 30))
    for i in daily_sale_dict.keys():
        plt.subplot(8, 7, i)
        plt.title('Store {} sale'.format(i))
        plt.tight_layout(pad=5)
        sale = daily_sale_dict[i].sales
        sale.plot()
        plt.axvline(x=pd.Timestamp('2016-04-16'), color='r', linestyle='--', linewidth=2, alpha=0.3)  # mark the earthquake
    st.pyplot(fig)
    st.markdown("설명 추가로 넣어주세요")

    # 제품군별 매출 딕셔너리로 만들기
    by_fam_dic = {}
    fam_list = train.family.unique()

    for fam in fam_list:
        by_fam_dic[fam] = train[train['family'] == fam].sales

    # 위의 결과를 시각화하는데 지진 표시되게 함
    fig = plt.figure(figsize=(30, 50))

    for i, fam in enumerate(by_fam_dic.keys()):
        plt.subplot(11, 3, i + 1)
        plt.title('{} sale'.format(fam))
        plt.tight_layout(pad=5)
        sale = by_fam_dic[fam]
        sale.plot()
        plt.axvline(x=pd.Timestamp('2016-04-16'), color='r', linestyle='--', linewidth=2, alpha=0.3)  # mark the earthquake

    st.pyplot(fig)
    st.markdown("설명 추가로 넣어주세요")