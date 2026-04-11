# **Car-Insurance-Fraud-Detection**

This project is an end-to-end Machine Learning system that detects fraudulent car insurance claims using structured customer and accident data. It includes full data preprocessing, feature engineering, model training with ensemble learning, and deployment using FastAPI + Streamlit.

# 🎯 Problem Statement

Insurance companies face significant financial losses due to fraudulent claims.
The goal of this project is to build a predictive system that can accurately classify whether an insurance claim is fraudulent or legitimate.

# ⚙️ Project Pipeline
1️⃣ Data Preprocessing
Handling missing values
Encoding categorical variables
Feature scaling
Removing unnecessary columns

2️⃣ Feature Engineering
Creating age groups from insured age
Extracting date-based features (year, month, day)
Transforming binary features (e.g., police report availability)

3️⃣ Handling Imbalanced Data
Applied Random UnderSampling to balance dataset
Improved model performance on minority (fraud) class

4️⃣ Encoding Techniques
One-Hot Encoding for nominal features
Ordinal Encoding for severity & education level
Target Encoding for high-cardinality features

5️⃣ Model Training
Multiple machine learning models were trained and evaluated:

Random Forest
Gradient Boosting
XGBoost
LightGBM
SVM
KNN
AdaBoost
6️⃣ Ensemble Learning

A Stacking Classifier was built using:
Random Forest
Gradient Boosting
LightGBM
as base models
Final meta-model:
XGBoost

7️⃣ Evaluation Metrics
F1 Score (primary metric)
Precision / Recall
Confusion Matrix
Precision-Recall Curve (threshold tuning)

8️⃣ Model Deployment
# 🔥 FastAPI Backend
REST API for real-time predictions
Accepts JSON input
Returns fraud probability + prediction

# 🎨 Streamlit Frontend
Interactive UI for users
Real-time fraud detection
Clean and simple dashboard

🚀 Tech Stack
Python
Pandas / NumPy
Scikit-learn
Ensemble Models
Imbalanced-learn
FastAPI
Streamlit
Joblib

# 📊 Model Output
Fraud probability score
Binary classification:
Fraud 🚨
Not Fraud ✅
