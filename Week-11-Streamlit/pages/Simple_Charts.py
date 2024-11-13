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

################# PAGE LAYOUT #####################
###################################################

# Load the data
df = load_data()

# Display the data
display_df = df.sample(n=5)
st.dataframe(display_df)

# do a scatter chart
st.scatter_chart(df, x='price', y='elevation', color='city', size='sqft') 

col1, col2, col3 = st.columns(3)
with col1:
    # Make and new histo and display it
    fig, ax = plt.subplots(figsize = (13,8))
    _ = sns.histplot(df, x='elevation', hue='city', multiple='stack')
    st.pyplot(fig)


st.markdown('---')
st.header('Weather Data')
weather_df = pd.read_csv('data/seattle-weather.csv')
weather_df_display = weather_df.sample(n=5)

st.dataframe(weather_df_display)
st.bar_chart(weather_df, y='weather')
st.dataframe(weather_df.value_counts('weather'))
st.bar_chart(weather_df, y='temp_max')




