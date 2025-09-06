import streamlit as st
import numpy as np
import pandas as pd

## title of the application
st.title("Hello Streamlit")

## display a simple text
st.write("This is a simple text")

## create a simple dataframe
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})

## display the dataframe
st.write('Here is the dataframe')
st.write(df)

## creata a line chart
chart_data = pd.DataFrame(
  np.random.randn(20, 3),
  columns=['a', 'b', 'c']
)

st.line_chart(chart_data)