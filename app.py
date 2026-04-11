import streamlit as st
import base64
import requests

def set_bg_local(image_file):
    with open(image_file, "rb") as f:
        img = f.read()
    b64 = base64.b64encode(img).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{b64}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_local("car.jpg")

st.title("🚗 Fraud Detection")

payload = {
    "policy_deductible": st.number_input("Deductible"),
    "policy_annual_premium": st.number_input("Premium"),
    "insured_age": st.slider("Age", 18, 80),

    "insured_sex": st.selectbox("Sex", ["Male", "Female"]),
    "insured_education_level": st.selectbox("Education", ["High School","College","Masters","PhD"]),
    "insured_occupation": st.text_input("Occupation"),

    "incident_type": st.selectbox("Incident", ["Collision","Theft"]),
    "collision_type": st.selectbox("Collision", ["Front","Rear","Side"]),
    "incident_severity": st.selectbox("Severity", ["Minor Damage","Major Damage","Total Loss"]),
    "authorities_contacted": st.selectbox("Authorities", ["Police","Fire","None"]),

    "incident_hour_of_the_day": st.slider("Hour",0,23),
    "number_of_vehicles_involved": st.slider("Vehicles",1,5),
    "bodily_injuries": st.slider("Injuries",0,5),
    "witnesses": st.slider("Witnesses",0,5),

    "police_report_available": st.selectbox("Police Report", ["Yes","No"]),
    "claim_amount": st.number_input("Claim"),
    "total_claim_amount": st.number_input("Total Claim")
}

if st.button("Predict"):
    res = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if res.status_code == 200:
        r = res.json()
        st.success(r["result"])
        st.write("Probability:", r["fraud_probability"])
    else:
        st.error(res.text)