# model.py
import joblib

def load_model():
    return joblib.load("lung_cancer_real_model.pkl")
