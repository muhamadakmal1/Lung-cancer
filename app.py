import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Set the page title
st.set_page_config(page_title="Lung Cancer Prediction", layout="centered")

# App title
st.title("🩺 Lung Cancer Prediction App")
st.markdown("This app predicts the likelihood of lung cancer based on survey responses.")

# --- User Input Form ---
st.header("Enter Survey Details")

age = st.slider("Age", 15, 100, 45)
gender = st.selectbox("Gender", ["MALE", "FEMALE"])
smoking = st.selectbox("Do you smoke?", ["YES", "NO"])
anxiety = st.selectbox("Do you suffer from anxiety?", ["YES", "NO"])
peer_pressure = st.selectbox("Do you experience peer pressure?", ["YES", "NO"])
chronic_disease = st.selectbox("Do you have a chronic disease?", ["YES", "NO"])
fatigue = st.selectbox("Do you experience fatigue?", ["YES", "NO"])
allergy = st.selectbox("Do you have allergies?", ["YES", "NO"])
wheezing = st.selectbox("Do you wheeze?", ["YES", "NO"])
alcohol = st.selectbox("Do you consume alcohol?", ["YES", "NO"])
coughing = st.selectbox("Do you cough frequently?", ["YES", "NO"])
shortness_of_breath = st.selectbox("Shortness of breath?", ["YES", "NO"])
swallowing_difficulty = st.selectbox("Difficulty swallowing?", ["YES", "NO"])
chest_pain = st.selectbox("Do you have chest pain?", ["YES", "NO"])

# Convert input to DataFrame
input_data = pd.DataFrame({
    'AGE': [age],
    'GENDER': [gender],
    'SMOKING': [smoking],
    'ANXIETY': [anxiety],
    'PEER_PRESSURE': [peer_pressure],
    'CHRONIC DISEASE': [chronic_disease],
    'FATIGUE ': [fatigue],
    'ALLERGY ': [allergy],
    'WHEEZING': [wheezing],
    'ALCOHOL CONSUMING': [alcohol],
    'COUGHING': [coughing],
    'SHORTNESS OF BREATH': [shortness_of_breath],
    'SWALLOWING DIFFICULTY': [swallowing_difficulty],
    'CHEST PAIN': [chest_pain]
})

# Encode input (YES/NO and MALE/FEMALE)
mapping = {'YES': 1, 'NO': 0, 'MALE': 1, 'FEMALE': 0}
input_data = input_data.applymap(lambda x: mapping.get(x, x))

# --- Dummy Model for Demo (Replace with your trained model) ---
@st.cache_resource
def train_dummy_model():
    # You should load your real training data and model instead of this dummy one
    from sklearn.datasets import make_classification
    X_dummy, y_dummy = make_classification(n_samples=200, n_features=14, random_state=42)
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_dummy, y_dummy)
    return clf

model = train_dummy_model()

# --- Prediction ---
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][prediction]

    if prediction == 1:
        st.error(f"⚠️ High risk of Lung Cancer (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Low risk of Lung Cancer (Probability: {probability:.2f})")
