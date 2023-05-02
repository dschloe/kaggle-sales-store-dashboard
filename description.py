# -*- coding:utf-8 -*-

import streamlit as st

def run_description():
    st.markdown("## Goal of the Competition \n"
                "- In this “getting started” competition, you’ll use time-series forecasting to forecast store sales on data from Corporación Favorita, a large Ecuadorian-based grocery retailer. \n"
                "- Specifically, you'll build a model that more accurately predicts the unit sales for thousands of items sold at different Favorita stores. You'll practice your machine learning skills with an approachable training dataset of dates, store, and item information, promotions, and unit sales. \n")

    st.markdown("## Evaluation \n"
                "- The evaluation metric for this competition is Root Mean Squared Logarithmic Error. \n")
    st.latex(r'''
    {RMSLE} = \sqrt{\frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{n}}
    ''')
    st.markdown("where: \n"
                "- $n$ is the total number of instances \n"
                "- $\hat{y}_i$ is the predicted value of the target for instance (i) \n"
                "- $y_i$ is the actual value of the target for instance (i), and, \n"
                "- $\log$ is the natural logarithm \n"
                )

    st.markdown("### Competition Info \n"
                "More Detailed : [Store Sales - Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting)")
