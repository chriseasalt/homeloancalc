import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="About Us", page_icon="☎️")
st.markdown("# About Us")
st.sidebar.header("About Us")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)