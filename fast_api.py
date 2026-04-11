from fastapi import FastAPI
import joblib
import pandas as pd
from features import add_features

app = FastAPI()

model = joblib.load("model/fraud_model.pkl")
threshold = joblib.load("model/threshold.pkl")

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prob = model.predict_proba(df)[:,1][0]
    pred = int(prob >= threshold)

    return {
        "result": "Fraud" if pred else "Not Fraud",
        "fraud_probability": float(prob)
    }