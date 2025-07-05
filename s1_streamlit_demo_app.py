import streamlit as st
import time

st.title("My Streamlit Demo Application")

name = st.text_input("Enter a name")

if name:
    st.success(f"Hello {name}! Good morning!")
    for i in range(10):
        time.sleep(0.5)  # Simulate a delay
        st.balloons()    

