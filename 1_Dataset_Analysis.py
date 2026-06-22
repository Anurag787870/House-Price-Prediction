import streamlit as st
import pandas as pd

df = pd.read_csv("dataset/house_price.csv")

st.title("📊 Dataset Analysis")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Shape")
st.write(df.shape)

st.subheader("Missing Values")
st.write(df.isnull().sum())

st.subheader("Statistical Summary")
st.write(df.describe())