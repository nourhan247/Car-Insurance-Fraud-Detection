# 🚗 **Car Insurance Fraud Detection System**

This project is an end-to-end Machine Learning system designed to detect fraudulent car insurance claims using structured customer and accident data. It covers the full ML lifecycle from data preprocessing and feature engineering to model training, evaluation, and deployment using FastAPI and Streamlit.

# 🎯 Problem Statement

Insurance companies suffer significant financial losses due to fraudulent claims.

The objective of this project is to build a predictive system that can accurately classify whether a car insurance claim is:

🚨 Fraudulent
✅ Legitimate

# ⚙️ Project Pipeline

1️⃣ Data Preprocessing
Handled missing values (e.g., authorities_contacted)
Removed irrelevant columns (e.g., policy_id)
Encoded categorical variables
Scaled numerical features where needed

2️⃣ Feature Engineering
Created age groups from insured age
Extracted time-based features from incident date
Transformed binary and categorical variables
Generated new meaningful features using custom feature functions

3️⃣ Handling Imbalanced Data
Applied KMeansSMOTE to oversample minority class
Improved model sensitivity toward fraud cases

4️⃣ Encoding Techniques
One-Hot Encoding → nominal features (sex, incident type, etc.)
Ordinal Encoding → education level, incident severity
CatBoost Encoding → high-cardinality features (occupation, age group)

5️⃣ Model Training

*Multiple ML models were evaluated:*

Random Forest
Gradient Boosting
XGBoost
LightGBM
SVM
KNN
AdaBoost

6️⃣ Deep Learning Model (Neural Network)

A fully connected neural network was built using TensorFlow/Keras:

Input layer → feature vector
Hidden layers → Dense (ReLU activation)
Output layer → Sigmoid (binary classification)
HeNormal initialization for stable training
GlorotUniform for output layer

7️⃣ Evaluation Strategy

Model performance was evaluated using:

F1 Score (primary metric)
Precision & Recall
Confusion Matrix
Precision-Recall Curve
Optimal threshold tuning instead of default 0.5

8️⃣ Model Deployment

# 🔥 FastAPI Backend

A REST API was built using FastAPI to serve predictions in real time:

Accepts JSON input (customer + incident data)
Applies preprocessing pipeline
Returns:
Fraud probability score
Final prediction (Fraud / Not Fraud)

# 🎨 Streamlit Frontend

An interactive web application was built using Streamlit:

User-friendly interface
Input form for claim details
Real-time fraud prediction
Displays probability + decision
Clean dashboard for non-technical users

# 🚀 Tech Stack
Python
Pandas / NumPy
Scikit-learn
Imbalanced-learn (SMOTE, KMeansSMOTE)
TensorFlow / Keras
CatBoost Encoder
FastAPI
Streamlit
Joblib

# 📊 Model Output

The system returns:

📈 Fraud Probability Score (0 → 1)
🧠 Binary Classification:
🚨 Fraud
✅ Not Fraud

# 💾 Model Deployment Artifacts

Saved components:

Trained Neural Network → fraud_nn.keras
Encoders:
cat_encoder.pkl
ordinal_encoder.pkl
Feature columns → columns.pkl
Optimal threshold → thresholdneural.pkl

# 🌐 System Architecture

Streamlit UI → FastAPI Backend → Preprocessing Pipeline → ML/DL Model → Prediction Output
