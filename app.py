import pandas as pd
import streamlit as st
from PIL import Image
import base64
import io
import os
import json
# Vykreslení tabulky s logy
st.markdown("<h1 style='text-align: center;'>Daily Invest AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>News</p>", unsafe_allow_html=True)
st.write("")

# Load the data
# def load_data():
#     df = pd.read_csv("final.csv")
#     return df

def load_news():
    with open("news.json", "r") as f:
        data = json.load(f)
    return data

# data = load_data().copy()
news = load_news().copy()

# Convert image to Base64
# def image_to_base64(img_path, output_size=(64, 64)):
#     # Check if the image path exists
#     if os.path.exists(img_path):
#         with Image.open(img_path) as img:
#             img = img.resize(output_size)
#             buffered = io.BytesIO()
#             img.save(buffered, format="PNG")
#             return f"data:image/png;base64,{base64.b64encode(buffered.getvalue()).decode()}"
#     return ""

# If 'Logo' column doesn't exist, create one with path to the logos
# if 'Logo' not in data.columns:
#     output_dir = 'downloaded_logos'
#     data['Logo'] = data['Name'].apply(lambda name: os.path.join(output_dir, f'{name}.png'))

# Convert image paths to Base64


# image_column = st.column_config.ImageColumn(label="")
nazev_column = st.column_config.TextColumn(label="Company Name")
market_cap_column = st.column_config.TextColumn(label="News 💬",help="📍**Latest news**")
# price_column = st.column_config.TextColumn(label="Stock Price", help="📍**Price in INR**")

# Adjust the index to start from 1 and display only the first 25 companies


temp = pd.DataFrame(news)
req_cols = ["company", "text"]
temp = temp[req_cols]
temp.index = temp.index + 1
temp.columns = ['Name', 'Market Cap']

# Display the dataframe
st.dataframe(temp, height=250, column_config={"Name":nazev_column,'Market Cap':market_cap_column})

import datetime

# Získání aktuálního data
dnesni_datum = datetime.date.today().strftime("%d.%m.%Y")  # Formátování data na formát DD.MM.YYYY

st.markdown(f'<span style="font-size: 14px">**Disclaimer:** Only for the demo purpose |</span>', unsafe_allow_html=True)
