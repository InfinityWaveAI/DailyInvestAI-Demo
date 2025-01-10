import streamlit as st
st.set_page_config('Home page', initial_sidebar_state='collapsed')


pg = st.navigation([st.Page("home.py"), st.Page("chat.py")])
pg.run()