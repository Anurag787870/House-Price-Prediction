import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/house_price.csv")

st.title("📈 Data Visualizations")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/house_price.csv")

st.title("House Price Visualizations")

st.subheader("House Area vs House Price")

fig, ax = plt.subplots()

ax.scatter(
    df["House_Area_sqft"],
    df["Price_INR"]
)

ax.set_xlabel("House Area (sq.ft)")
ax.set_ylabel("House Price (INR)")
ax.set_title("Area vs Price")

st.pyplot(fig)


st.subheader("Bedrooms vs House Price")

fig, ax = plt.subplots()

ax.scatter(
    df["Number_of_Bedrooms"],
    df["Price_INR"]
)

ax.set_xlabel("Bedrooms")
ax.set_ylabel("Price")

st.pyplot(fig)


st.subheader("Property Age vs Price")

fig, ax = plt.subplots()

ax.scatter(
    df["Property_Age_Years"],
    df["Price_INR"]
)

ax.set_xlabel("Property Age")
ax.set_ylabel("Price")

st.pyplot(fig)