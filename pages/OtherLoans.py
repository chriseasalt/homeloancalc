import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="About Us", page_icon="☎️")
st.markdown("# Enquiry on Other Loans")
st.sidebar.header("Contact Us")
st.write(
    """### Are you interested to find out more about other loans you can take on with our company?"""
)
st.write(
    """Fill in your details below and we'll reach out to you"""
)

container_1 = st.container()
container_1.empty() 


with container_1:
    with st.form('input_form'):
        query = st.text_area('Tell us more about yourself and the type of loan you are seeking')
        submitted_input = st.form_submit_button('Submit Enquiry')
        print(query) # works fine

    if submitted_input:
        with st.spinner(text='This may take a moment...'):
            st.text("Your submission has been received. We will get back to you in 2 working days") # simulated response