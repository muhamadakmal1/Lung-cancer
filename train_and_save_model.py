import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load and clean dataset
df = pd.read_csv("survey lung cancer.csv")
df.columns = df.columns.str.strip()

# Encode labels
df["GENDER"] = df["GENDER"].map({"M": 1, "F": 0})
df["LUNG_CANCER"] = df["LUNG_CANCER"].map({"YES": 1, "NO": 0})

# Replace 2s with 1s in binary features
binary_columns = df.columns.drop("AGE")
df[binary_columns] = df[binary_columns].replace(2, 1)

# Split features and target
X = df.drop("LUNG_CANCER", axis=1)
y = df["LUNG_CANCER"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model and feature list
joblib.dump({
    "model": model,
    "features": list(X.columns)
}, "lung_cancer_real_model.pkl")

print("✅ Model and features saved successfully.")
