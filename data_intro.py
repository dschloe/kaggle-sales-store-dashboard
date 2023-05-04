# -*- coding:utf-8 -*-
import streamlit as st

def run_dataIntro():
    st.markdown("## Data Description 	:open_file_folder: \n")
    st.markdown("- :point_right: In this competition, you will predict sales for the thousands of product families sold at Favorita stores located in Ecuador. The training data includes dates, store and product information, whether that item was being promoted, as well as the sales numbers. Additional files include supplementary information that may be useful in building your models. \n"
                "###  🗃️ File Descriptions and Data Field Information \n"
                "#### :clipboard: train.csv \n"
                "- 	The training data, comprising time series of features **store_nbr**, **family**, and **onpromotion** as well as the target **sales.** \n"
                "- 	**store_nbr** identifies the store at which the products are sold. \n"
                "- **family** identifies the type of product sold. \n"
                "- **sales** gives the total sales for a product family at a particular store at a given date. Fractional values are possible since products can be sold in fractional units (1.5 kg of cheese, for instance, as opposed to 1 bag of chips). \n"
                "- **onpromotion** gives the total number of items in a product family that were being promoted at a store at a given date. \n"
                "#### :clipboard: stores.csv \n"
                "- 	Store metadata, including **city**, **state**, **type**, and **cluster**. \n"
                "- **cluster** is a grouping of similar stores \n"
                "#### :clipboard: oil.csv \n"
                "- 	Daily oil price. Includes values during both the train and test data timeframes. (Ecuador is an oil-dependent country and it's economical health is highly vulnerable to shocks in oil prices.) \n"
                "#### :clipboard: holidays_events.csv \n"
                "- 	NOTE: Pay special attention to the **transferred** column. A holiday that is transferred officially falls on that calendar day, but was moved to another date by the government. A transferred day is more like a normal day than a holiday. To find the day that it was actually celebrated, look for the corresponding row where type is Transfer. For example, the holiday Independencia de Guayaquil was transferred from 2012-10-09 to 2012-10-12, which means it was celebrated on 2012-10-12. Days that are type Bridge are extra days that are added to a holiday (e.g., to extend the break across a long weekend). These are frequently made up by the type Work Day which is a day not normally scheduled for work (e.g., Saturday) that is meant to payback the Bridge. \n"
                "- Additional holidays are days added a regular calendar holiday, for example, as typically happens around Christmas (making Christmas Eve a holiday). \n"
                "###  :exclamation: Additional Notes \n"
                "- Wages in the public sector are paid every two weeks on the 15 th and on the last day of the month. Supermarket sales could be affected by this."
                "- A magnitude 7.8 earthquake struck Ecuador on April 16, 2016. People rallied in relief efforts donating water and other first need products which greatly affected supermarket sales for several weeks after the earthquake."
                )
    st.caption('**Site:** [Store Sales - Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data)')
