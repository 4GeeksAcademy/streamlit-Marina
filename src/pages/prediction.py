import streamlit as st
import random

result = random.randint(0,2)

if result == 0:
    st.title("You're not hired! You suck!")
else:
    st.title('You are hired! My, my, Mr. Gates!')


with st.form('my_form'):
    st.write('Please enter your email')
    text = st.text_input('Email')

    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write(text)