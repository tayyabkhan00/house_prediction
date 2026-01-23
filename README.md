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

# 🗂️ Project Structure
```
house_prediction/
│
├── app.py                  # Streamlit application
├── train_model.py          # Model training script (local only)
│
├── data/
│   └── bengaluru_house_data.csv
│
├── model/
│   ├── house_price_model.pkl
│   └── columns.json
│
├── requirements.txt        # Dependencies
├── runtime.txt             # Python version
└── README.md
```
# ⚙️ How to Run Locally
1️⃣ Clone the repository<br>
git clone https://github.com/your-username/house_prediction.git<br>
cd house_prediction<br>
2️⃣ Create a virtual environment (recommended)<br>
python -m venv venv<br>
source venv/bin/activate   # macOS/Linux<br>
venv\Scripts\activate      # Windows<br>
3️⃣ Install dependencies<br>
pip install -r requirements.txt<br>
4️⃣ Train the model (local only)<br>
python train_model.py<br>
This generates:<br>
- model/house_price_model.pkl
- model/columns.json<br>
5️⃣ Run the Streamlit app<br>
streamlit run app.py

# ☁️ Deployment (Streamlit Cloud)

- Steps followed:
- Trained model locally
- Pushed model artifacts (.pkl, .json) to GitHub
- Connected repository to Streamlit Cloud
- Used relative paths and CPU-safe configuration
- App auto-redeploys on every GitHub push

# 🛡️ Deployment & Engineering Notes

✅ Uses relative paths (__file__) for portability
✅ Model trained with CPU-safe XGBoost
✅ XGBoost version aligned across local & cloud
✅ Feature names preserved using columns.json
✅ Predictions done using pandas DataFrame (feature-safe)
❌ No training happens on the cloud (best practice)

# 📦 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Git & GitHub

# 📊 Sample Prediction

Input:
Location: Whitefield
Total Sqft: 1200
Bathrooms: 2
BHK: 2

Output:
💰 Estimated Price: ₹ XX Lakhs

# 🎯 Future Improvements

- Add model explainability (SHAP)
- Add price range instead of point estimate
- Improve UI/UX
- Add input validation and error messages
- Integrate ML pipelines (sklearn Pipeline)

# 🙌 Acknowledgements

- Dataset inspired by public Bengaluru housing data
- Built as part of hands-on learning in AI & Data Science

# 👤 Author

Tayyab Khan<br>
BTech in AI & Data Science<br>
Aspiring Data Scientist / ML Engineer

📫 Feel free to connect or review the project!

### Deployment Notes
- Model trained locally with CPU-safe XGBoost
- Deployed on Streamlit Cloud using feature-aligned inference
