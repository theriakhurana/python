import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name")

if name:
  st.write(f"Hello {name}!")
  
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You are {age} years old.")

options = ["Js", "Python", "C++"]
choice = st.selectbox('Choose your favorite programming language', options)
st.write(f"You selected: {choice}")

data = {
  "name": ["Alice", "Bob", "Charlie", "David"],
  "age": [25, 30, 35, 40],
  "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uplaoded_file = st.file_uploader("Uplaod a csv file", type="csv")

if uplaoded_file is not None:
  df = pd.read_csv(uplaoded_file)
  st.write(df)