import pandas as pd
import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# Function for sidebar launch selection dates
# Source: https://github.com/korenkaplan/Admin-dashboard/blob/main/sidebar.py
def init_sidebar_dates_pickers(data_frame_datetime, start_default=None, end_default=None):
    # Convert the order_date column to datetime for manipulation and find the min and max value
    min_date = data_frame_datetime.min()
    max_date = data_frame_datetime.max()

    # Set default values for start_date and end_date if none is provided
    if start_default is None:
        start_date = min_date
    else:
        start_date = start_default
        
    if end_default is None:
        end_date = max_date
    else:
        end_date = end_default
    
    # Initialize the sidebar date pickers and define the min and max value to choose from 
    #    Make sure that start_date is less than end_date
    start_date = st.slider('First Order', min_value=min_date, max_value=max_date, value=start_date)
    end_date = st.slider('Last Order', min_value=min_date, max_value=max_date, value=end_date)
    
    # Check if the start_date is greater than the end_date
    if start_date > end_date:
        st.error('The First Order cannot be greater than the Last Order. Please select a valid date range!')
        st.stop()
    
    # Return the values
    return start_date, end_date


# Function to create a custom HTML card
def create_card(col, icon_name, color, color_text, title, value):
    htmlstr = f"""
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">
    <p style="background-color: rgb({color[0]}, {color[1]}, {color[2]});
            color: rgb({color_text[0]}, {color_text[1]}, {color_text[2]});
            font-weight: 700;
            font-size: 30px;
            border-radius: 7px;
            padding-left: 20px; 
            padding-top: 18px; 
            padding-bottom: 18px;
            line-height: 25px;">
        <i class='{icon_name} fa-xs' style='margin-right: 5px;'></i>{value}</style>
        <br>
        <span style='font-size: 18px; margin-top: 0; font-weight: 100;margin-left: 30px;'>{title}</style></span></p>
    """
    col.markdown(htmlstr, unsafe_allow_html=True)