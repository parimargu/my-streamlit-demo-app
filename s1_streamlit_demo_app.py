import streamlit as st

st.title("My Streamlit Demo Application")

name = st.text_input("Enter a name")

st.success(f"Hello {name}! Good morning!")
st.balloons()
