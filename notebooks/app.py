import streamlit as st
import pandas as pd
import joblib

model = joblib.load("suspicious_traffic_model.pkl")

st.title("Suspicious Web Traffic Detector")

bytes_in = st.number_input("Bytes In", min_value=0)
bytes_out = st.number_input("Bytes Out", min_value=0)
duration = st.number_input("Duration (s)", min_value=0.0)
protocol = st.selectbox("Protocol", [0, 1, 2])  # replace with actual encoded values
country_code = st.selectbox("Source Country Code", [0, 1, 2])  # replace with actual encoded values

if st.button("Predict"):
    input_df = pd.DataFrame([{
        "bytes_in": bytes_in,
        "bytes_out": bytes_out,
        "duration": duration,
        "protocol_encoded": protocol,
        "src_ip_country_code_encoded": country_code
    }])
    prediction = model.predict(input_df)[0]
    st.success("Suspicious Traffic" if prediction == 1 else "Normal Traffic")

# streamlit run app.py
# streamlit run notebooks/app.py
