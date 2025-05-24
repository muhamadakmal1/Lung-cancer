import streamlit as st
import pandas as pd
from model import load_model

st.set_page_config(page_title="Lung Cancer Prediction", layout="centered")
st.title("🩺 Lung Cancer Prediction App")
st.markdown("This app predicts the likelihood of lung cancer based on survey responses.")

# Get model and expected feature order
@st.cache_resource
def get_model():
    return load_model()

model, expected_features = get_model()

# User inputs
st.header("Enter Survey Details")
age = st.slider("Age", 15, 100, 45)
gender = st.selectbox("Gender", ["MALE", "FEMALE"])
smoking = st.selectbox("Do you smoke?", ["YES", "NO"])
yellow_fingers = st.selectbox("Do you have yellow fingers?", ["YES", "NO"])
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

# Encode mapping
mapping = {'YES': 1, 'NO': 0, 'MALE': 1, 'FEMALE': 0}
def encode(x): return mapping.get(x, x)

# Construct input dictionary
user_input = {
    'AGE': age,
    'GENDER': encode(gender),
    'SMOKING': encode(smoking),
    'YELLOW_FINGERS': encode(yellow_fingers),
    'ANXIETY': encode(anxiety),
    'PEER_PRESSURE': encode(peer_pressure),
    'CHRONIC DISEASE': encode(chronic_disease),
    'FATIGUE': encode(fatigue),
    'ALLERGY': encode(allergy),
    'WHEEZING': encode(wheezing),
    'ALCOHOL CONSUMING': encode(alcohol),
    'COUGHING': encode(coughing),
    'SHORTNESS OF BREATH': encode(shortness_of_breath),
    'SWALLOWING DIFFICULTY': encode(swallowing_difficulty),
    'CHEST PAIN': encode(chest_pain)
}

# Convert to DataFrame
input_data = pd.DataFrame([user_input])

# Reorder and align columns to match training
for col in expected_features:
    if col not in input_data.columns:
        input_data[col] = 0
input_data = input_data[expected_features]

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][prediction]
    if prediction == 1:
        st.error(f"⚠️ High risk of Lung Cancer (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Low risk of Lung Cancer (Probability: {probability:.2f})")
