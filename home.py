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
    with open("final_demo_ready.json", "r", encoding='utf-8') as f:
        d = json.load(f)
    return d

full = load_data()
full_df = pd.DataFrame(full)


news_data = []
for r in full:
    if r['NEWS'] != None:
        obj = r.copy()
        temp = obj['NEWS_TRANSLATED'][0]
        for key,val in temp.items():
            obj[key.upper()]=val
        news_data.append(obj)

news_df = pd.DataFrame(news_data)



col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('')
with col2:
    option = st.selectbox(
        "Select the language",
        ("ENGLISH", "HINDI", "BENGALI","TELUGU", 'TAMIL'),
    )

    st.write("You selected:", option)
with col3:
    st.markdown('')
# Lanuage selection

# Cleaning the data
# Adjust the index to start from 1 
data = news_df.copy()

data.reset_index(drop=True, inplace=True)
data.index = data.index + 1

## Changing the data: based on selection
# only required collumns 
language_col = option

req_cols = ["COMPANY NAME", "CLOSE_PRICE", language_col]
data = data[req_cols]


# Search bar :> 

# all_company_names = [""]
# all_company_names.extend(list(full_df['COMPANY NAME'].values))

# company = st.selectbox(
#         "Search for a company heere",
#         all_company_names,
#         )
# if company in data['COMPANY NAME'].values:
#     filtered_data = data[data["COMPANY NAME"].str.contains(company.upper(), na=False)]
# else:
#     pass

filtered_data = data

# defining columns for the dataframe
company_name_column =  st.column_config.TextColumn(label="COMPANY NAME")
price_column = st.column_config.TextColumn(label="Stock Price", help="📍**Price in INR**")
news_lang_column = st.column_config.TextColumn(label="News {}💬".format(language_col),help="📍**Latest news in your language**")


# Display the dataframe
event = st.dataframe(filtered_data, use_container_width=True,
              hide_index=True
            )

# i = event.selection.rows


# if i:
#     name = filtered_data['Name'].values[i][0]
#     sym = full[full['company name'] == name]['symbol'].values[0]
#     url = str("graphs/"+ sym +".svg")
#     st.image(url, caption=name, width=600)


# Search bar :> 

all_company_names = [""]
all_company_names.extend(list(full_df['COMPANY NAME'].values))

company = st.selectbox(
        "Search for a company for complete information",
        all_company_names,
        )

# company = "Tata Motors Ltd."
if company != "":
    sym = full_df[full_df['COMPANY NAME'] == company]['SYMBOL'].values[0]

    ## Selected Company :> Complete info 
    st.markdown("<h3 style='text-align: center;'>{}</h3>".format(company), unsafe_allow_html=True)


    # selected company full details :> 
    details = full_df[full_df['COMPANY NAME'] == company].to_dict("records")[0]
    # st.write(details)

    # st.write(details["CLOSE_PRICE"])

    ## Chart and price 
    col1, col2 = st.columns(2)
    with col1:
        # url = str("graphs/"+ sym +".svg")
        url = str("https://nsearchives.nseindia.com/today/{}EQN.svg".format(sym))
        # url = str("https://nsearchives.nseindia.com/today/INFYEQN.svg")
        st.image(url, caption=sym, use_container_width =True)

    with col2:
        change = float(details["CLOSE_PRICE"]) - float(details["OPEN_PRICE"]) 
        change_perc = change / float(details["OPEN_PRICE"])

        change_perc = round(change_perc,2)
        change = round(change,2)

        st.metric(label="Current Price", value="{} INR".format(details["CLOSE_PRICE"]), delta="{} ({}%)".format(change,change_perc))
        # For live chart link:>
        # st.markdown("[Click here for live chart](https://charting.nseindia.com/?symbol=TATAMOTORS-EQ)")

    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='text-align: center;'>Technical Analysis</h3>", unsafe_allow_html=True)
        st.write("Volume-Weighted Average Price (VWAP)")
        st.write("Explanation:")
        st.write("The recent contract win from Survey of India for 2D/3D urban mapping is a significant milestone for Drone Destination Limited")

    with col2:
        st.image("data/algo.png", caption="Technical Analysis")
    
    # col1, col2, col3 = st.columns(3)
    # with col2:
    #     st.markdown("<h3 style='text-align: center;'>All Updates</h5>", unsafe_allow_html=True)

    # # sub heading 
    col1, col2 = st.columns(2)
    with col1:
        # st.markdown("<h3 style='text-align: center;'>All Updates</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>Update</h5>", unsafe_allow_html=True)
        

    with col2:
        st.markdown("<h5 style='text-align: center;'>Summary and Impact</h5>", unsafe_allow_html=True)

    with open("company_data.json","r") as f:
        all_updates_data = json.load(f)

    all_updates = all_updates_data["TATAMOTORS"]
    for update in all_updates:
        col1, col2 = st.columns(2)
        with col1:
            st.write(update["update"])
            st.markdown("[Reference]({})".format(update['reference']))
        with col2:
            st.write(update["impact"])

# # loading all updates :> 
# with open("company_data.json","r") as f:
#     all_updates_data = json.load(f)
# all_updates = all_updates_data[sym]

# # heading
# col1, col2, col3 = st.columns(3)
# with col2:
#     st.markdown("<h3 style='text-align: center;'>All Updates</h5>", unsafe_allow_html=True)

# # sub heading 
# col1, col2 = st.columns(2)
# with col1:
#     st.markdown("<h5 style='text-align: center;'>Update</h5>", unsafe_allow_html=True)
    

# with col2:
#     st.markdown("<h5 style='text-align: center;'>Summary and Impact</h5>", unsafe_allow_html=True)

# for update in all_updates:
#     col1, col2 = st.columns(2)
#     with col1:
#         st.write(update["update"])
#         st.markdown("[Reference]({})".format(update['reference']))
#     with col2:
#         st.write(update["impact"])
## Live News :> Summary and Impact
