import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("models/model.pkl")

# Load dataset
dataset = pd.read_csv("dataset/house_price.csv")

st.title("🏡 House Price Prediction")

# ======================
# User Inputs
# ======================

area = st.number_input(
    "House Area (sq.ft)",
    min_value=100
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1
)

bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1
)

floors = st.number_input(
    "Number of Floors",
    min_value=1
)

parking = st.number_input(
    "Parking Spaces",
    min_value=0
)

age = st.number_input(
    "Property Age (Years)",
    min_value=0
)

distance = st.number_input(
    "Distance to City Center (km)",
    min_value=0.0
)

schools = st.number_input(
    "Nearby Schools Count",
    min_value=0
)

hospitals = st.number_input(
    "Nearby Hospitals Count",
    min_value=0
)

# ======================
# Prediction Button
# ======================

if st.button("Predict House Price"):

    input_data = pd.DataFrame([[
        area,
        bedrooms,
        bathrooms,
        floors,
        parking,
        age,
        distance,
        schools,
        hospitals
    ]], columns=[
        "House_Area_sqft",
        "Number_of_Bedrooms",
        "Number_of_Bathrooms",
        "Number_of_Floors",
        "Parking_Spaces",
        "Property_Age_Years",
        "Distance_to_City_Center_km",
        "Nearby_Schools_Count",
        "Nearby_Hospitals_Count"
    ])

    prediction = model.predict(input_data)

    # Show Prediction
    st.success(
        f"Predicted House Price: ₹{prediction[0]:,.0f}"
    )

    # ======================
    # Feature Importance Graph
    # ======================

    st.subheader("Feature Importance")

    features = [
        "Area",
        "Bedrooms",
        "Bathrooms",
        "Floors",
        "Parking",
        "Age",
        "Distance",
        "Schools",
        "Hospitals"
    ]

    importance = model.feature_importances_

    fig, ax = plt.subplots()

    ax.barh(features, importance)

    ax.set_title("Factors Affecting House Price")

    st.pyplot(fig)

    # ======================
    # User House vs Average
    # ======================

    st.subheader("Your House vs Average House")

    avg_area = dataset["House_Area_sqft"].mean()

    comparison = {
        "Your House": area,
        "Average House": avg_area
    }

    fig, ax = plt.subplots()

    ax.bar(
        list(comparison.keys()),
        list(comparison.values())
    )

    ax.set_title(
        "House Area Comparison"
    )

    st.pyplot(fig)