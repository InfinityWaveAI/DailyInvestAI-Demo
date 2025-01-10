import streamlit as st
import json 
import pandas as pd

st.markdown("<h1 style='text-align: center;'>Chat with Company!</h1>", unsafe_allow_html=True)
st.write("")

# loading data :> 
def load_data():
    with open("final_demo_ready.json", "r", encoding='utf-8') as f:
        d = json.load(f)
    return d

full = load_data()
full_df = pd.DataFrame(full)

all_company_names = [""]
all_company_names.extend(list(full_df['COMPANY NAME'].values))

# Selecting company
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('')
with col2:
    company = st.selectbox(
            "Select the company ",
            all_company_names,
            )


with col3:
    st.markdown('')

if company != "":
    # st.write("You selected:", option)
    query = st.text_input("Please write you query!")
    if query != "":
        st.write("Yes. 52Week low for company TATA MOTORS is Rs. 717.7")

