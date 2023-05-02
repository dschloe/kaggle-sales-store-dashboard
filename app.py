# -*- coding:utf-8 -*-
import streamlit as st
from streamlit_option_menu import option_menu
from description import run_description
from eda import run_eda

def main():
    with st.sidebar:
        selected = option_menu("Main Menu", ['Home', 'Description', 'Data', 'EDA', 'STAT'],
                icons=['house', 'card-checklist', 'card-checklist', 'bar-chart', 'clipboard-data'],
                menu_icon="cast", default_index=1, orientation = 'vertical')

    if selected == 'Description':
        run_description()
    elif selected == 'Data':
        pass
    elif selected == 'EDA':
        run_eda()
    elif selected == 'STAT':
        pass
    else:
        print('error..')


if __name__ == "__main__":
    main()