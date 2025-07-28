import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Text Input Example")
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is: {age}")

options = ["Python", "Java", "C++"]
choice = st.selectbox("Choose a programming language:", options)
st.write(f"You selected: {choice}")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)
st.write("Here is a sample DataFrame:")
st.dataframe(df)


uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Here is the uploaded DataFrame:")
    st.dataframe(df)
