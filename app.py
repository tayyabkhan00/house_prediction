import streamlit as st
import pickle
import json
import numpy as np
import os

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(page_title="Bengaluru House Price Predictor", layout="centered")

# -------------------------------
# Background styling
# -------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(
            rgba(0,0,0,0.55),
            rgba(0,0,0,0.55)
        ),
        url("https://images.pexels.com/photos/4119830/pexels-photo-4119830.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    h1, label {
        color: white !important;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Load model & columns safely
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(
    open(os.path.join(BASE_DIR, "model/house_price_model.pkl"), "rb")
)

columns = json.load(
    open(os.path.join(BASE_DIR, "model/columns.json"), "r")
)

# -------------------------------
# UI
# -------------------------------
st.title("🏠 Bengaluru House Price Predictor")

exclude = ['total_sqft', 'bath', 'bhk']
locations = sorted([c for c in columns if c not in exclude])

location = st.selectbox("Location", locations)
sqft = st.number_input("Total Sqft", min_value=300.0)
bath = st.number_input("Bathrooms", min_value=1, step=1)
bhk = st.number_input("BHK", min_value=1, step=1)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Price"):
    try:
        x = np.zeros(len(columns))

        x[columns.index('total_sqft')] = sqft
        x[columns.index('bath')] = bath
        x[columns.index('bhk')] = bhk

        if location in columns:
            x[columns.index(location)] = 1

        price = model.predict([x])[0]

        st.success(f"Estimated Price: ₹ {round(price, 2)} Lakhs")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
