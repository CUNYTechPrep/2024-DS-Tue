import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


############### PAGE SETUP ########################
###################################################

st.set_page_config(layout="wide")
st.header("Smiple Charts")


############ HELPER FUNCTIONS #####################
###################################################

@st.cache_data
def load_data():
    df = pd.read_csv('data/ny-vs-sf-houses.csv')
    return df

def display_data(n=5):
    #Randomize the data
    display_df = df.sample(n=n)
    st.dataframe(display_df)

def plot_streamlit_scatter_chart():
    st.scatter_chart(df, x='price', y='elevation', color='city', size='sqft') 

def plot_static_seaborn_chart():
    fig, ax = plt.subplots(figsize = (50,30))
    _ = sns.histplot(df, x='elevation', hue='city', multiple='stack')
    st.pyplot(fig)


################## PAGE LAYOUT  ###################
###################################################

df = load_data()
col1, col2 = st.columns([1, 3])

## COL1 WILL HOLD OUR FILTERS
with col1:
    ## FILTERS
    selected_cities = st.multiselect(
        'Select which states to compare.',
        ['SF', 'NY'],
        default=['SF', 'NY'] )

    # Use selected cities to filter the dataframe
    df = df[df['city'].isin(selected_cities)]

    # Create a price filter
    price_filter = st.slider(
        "Filter for only prices above",
        min_value = df.price.min(),
        max_value = df.price.max(),
        step=100000
    )
    # filter for only prices greater than price_filter value. 
    df = df[df['price'] >= price_filter]


## COL2 WILL HOLD OUR CHARTS 
with col2:
    display_data()
    plot_streamlit_scatter_chart()
    plot_static_seaborn_chart()



