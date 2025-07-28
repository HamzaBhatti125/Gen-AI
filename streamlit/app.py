import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("DataFrame Manipulation App")

# Display a simple text
st.write("This app allows you to manipulate a DataFrame using Streamlit.")

#create a simple DataFrame
df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40],
})

# Display the DataFrame
st.write("Here is a simple DataFrame:")
st.write(df)

#create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"],
)
st.line_chart(chart_data)