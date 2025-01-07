# Streamlit demo for DailyInvest AI

# libraries
import pandas as pd
import streamlit as st
from PIL import Image
import base64
import io
import os
import json

# Headers
st.markdown("<h1 style='text-align: center;'>Daily Invest AI</h1>", unsafe_allow_html=True)
st.write("")


# Loading the data
def load_data():
    with open("final.json", "r", encoding='utf-8') as f:
        d = json.load(f)
    df = pd.DataFrame(d)
    return df

full = load_data()
full['company name'] = full['company name'].apply(lambda x:x.upper())



col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('')
with col2:
    option = st.selectbox(
        "Select the language",
        ("Hindi", "Telugu"),
    )

    st.write("You selected:", option)
with col3:
    st.markdown('')
# Lanuage selection

# Cleaning the data
# Adjust the index to start from 1 
data = full.copy()
data.reset_index(drop=True, inplace=True)
data.index = data.index + 1

## Changing the data: based on selection
# only required collumns 
another_col = option.lower()

req_cols = ['company name', 'price', another_col, 'text' ]
data = data[req_cols]

new_cols = ['Name',  'Price', another_col, 'News']
data.columns = new_cols


# Search bar :> 
text_search = st.text_input("Search a company name", value="")

filtered_data = data[data['Name'].str.contains(text_search.upper(), na=False)]

# defining columns for the dataframe
company_name_column =  st.column_config.TextColumn(label="Company Name")
price_column = st.column_config.TextColumn(label="Stock Price", help="📍**Price in INR**")
news_lang_column = st.column_config.TextColumn(label="News {}💬".format(option.lower()),help="📍**Latest news in your language**")
news_column = st.column_config.TextColumn(label="News 💬",help="📍**Latest news**")



# Display the dataframe
event = st.dataframe(filtered_data, use_container_width=True,
              hide_index=True,
              on_select="rerun",
              selection_mode=["single-row", "single-column"],
            )

i = event.selection.rows


if i:
    name = filtered_data['Name'].values[i][0]
    sym = full[full['company name'] == name]['symbol'].values[0]
    url = str("graphs/"+ sym +".svg")
    st.image(url, caption=name, width=600)

