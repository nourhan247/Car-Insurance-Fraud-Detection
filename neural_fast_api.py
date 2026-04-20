from fastapi import FastAPI
import joblib
import pandas as pd
from features import add_features
from tensorflow.keras.models import load_model

app = FastAPI()

model = load_model("model/fraud_nn.keras")
threshold = joblib.load("model/thresholdneural.pkl")
cat_encoder = joblib.load("model/cat_encoder.pkl")
ordinal_encoder = joblib.load("model/ordinal_encoder.pkl")
columns = joblib.load("model/columns.pkl")


@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    # 1. feature engineering
    df = add_features(df)

    # 2. CatBoost encoding
    df = cat_encoder.transform(df)

    # 3. Ordinal encoding
    ordinal_cols = ['insured_education_level','incident_severity']
    df[ordinal_cols] = ordinal_encoder.transform(df[ordinal_cols])

    # 4. One-hot encoding
    df = pd.get_dummies(df)

    # 5. Align columns EXACTLY like training
    df = df.reindex(columns=columns, fill_value=0)

    # 6. Predict
    prob = model.predict(df)[0][0]
    pred = int(prob >= threshold)

    return {
        "result": "Fraud" if pred else "Not Fraud",
        "fraud_probability": float(prob)
    }