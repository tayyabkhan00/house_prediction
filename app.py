import streamlit as st

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.pexels.com/photos/4119830/pexels-photo-4119830.jpeg?_gl=1*1nuo4qg*_ga*MTU5Mjk0MjQwLjE3NjkwOTA1NTE.*_ga_8JE65Q40S6*czE3NjkwOTQ1MzkkbzIkZzEkdDE3NjkwOTQ5NjQkajU5JGwwJGgw");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(
            rgba(0,0,0,0.5),
            rgba(0,0,0,0.5)
        ),
        url("https://images.pexels.com/photos/4119830/pexels-photo-4119830.jpeg?_gl=1*1nuo4qg*_ga*MTU5Mjk0MjQwLjE3NjkwOTA1NTE.*_ga_8JE65Q40S6*czE3NjkwOTQ1MzkkbzIkZzEkdDE3NjkwOTQ5NjQkajU5JGwwJGgw");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
h1 {
    color: white;
    text-align: center;
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 8px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)


import streamlit as st
import pickle
import json
import numpy as np

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(
    open(os.path.join(BASE_DIR, "model/house_price_model.pkl"), "rb")
)

columns = json.load(
    open(os.path.join(BASE_DIR, "model/columns.json"), "r")
)

columns = json.load(open("model/columns.json"))

st.title("🏠 Bengaluru House Price Predictor")

# FIX-4: Correct location columns
exclude = ['total_sqft', 'bath', 'bhk']
locations = [c for c in columns if c not in exclude]

location = st.selectbox("Location", sorted()
sqft = st.number_input("Total Sqft")
bath = st.number_input("Bathrooms", step=1)
bhk = st.number_input("BHK", step=1)

if st.button("Predict Price"):
    x = np.zeros(len(columns))
    x[columns.index('total_sqft')] = sqft
    x[columns.index('bath')] = bath
    x[columns.index('bhk')] = bhk
    
    if location in columns:
        x[columns.index(location)] = 1

    # FIX #5 goes EXACTLY here
    try:
        price = model.predict([x])[0]
        st.success(f"Estimated Price: ₹ {round(price,2)} Lakhs")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
