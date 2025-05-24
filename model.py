import joblib

def load_model():
    data = joblib.load("lung_cancer_real_model.pkl")
    return data["model"], data["features"]
