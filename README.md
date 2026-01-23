# 🏠 Bengaluru House Price Prediction App

A machine learning web application that predicts house prices in Bengaluru based on user inputs such as location, total square feet, number of bathrooms, and BHK.<br>
The model is trained locally and deployed using Streamlit Cloud for real-time predictions.

# 🚀 Live Demo

👉 Streamlit App: (add your Streamlit URL here)<br>
👉 GitHub Repository: (this repo)

# 📌 Project Overview

Real estate pricing is influenced by many factors like location, size, and amenities.<br>
This project uses machine learning to estimate house prices in Bengaluru using historical data.<br>
### Key highlights:
- End-to-end ML pipeline (data → model → deployment)
- Clean feature engineering
- CPU-safe XGBoost model
- Cloud-ready Streamlit deployment

# 🧠 Machine Learning Approach
### 🔹 Dataset

- Bengaluru house price dataset
- Contains features like:
  - Location
  - Total square feet
  - Bathrooms
  - BHK
  - Price (target)

### 🔹 Feature Engineering

- Removed irrelevant columns (society, availability, etc.)
- Converted size → bhk
- Converted total_sqft ranges to numeric values
- Grouped rare locations into "other"
- Applied one-hot encoding to location
- Avoided data leakage by removing price_per_sqft

### 🔹 Models Trained

- Linear Regression (baseline)
- XGBoost Regressor (final model)

### 🔹 Final Model

- Production-safe file handling
- High R² score on test data
- Serialized using pickle

# 🖥️ Web App (Streamlit)

### Users can:
- Select a location
- Enter total square feet
- Choose number of bathrooms and BHK
- Get an estimated house price instantly
### The app:
- Loads a pre-trained model
- Builds feature-aligned input dynamically
- Runs inference safely on CPU-only cloud infrastructure

- 🗂️ Project Structure

### Deployment Notes
- Model trained locally with CPU-safe XGBoost
- Deployed on Streamlit Cloud using feature-aligned inference
