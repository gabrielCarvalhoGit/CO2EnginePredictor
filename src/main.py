import joblib
import streamlit as st


model = joblib.load('../models/model.pkl')

st.title("CO2 Emission Predictor")
engine_size = st.number_input("Enter engine size (diameter)", min_value=0.0, step=0.1, format="%.2f")

if st.button("Predict"):
    if engine_size > 0:
        predict = model.predict([[engine_size]])[0][0]
        
        st.write(f"Predicted CO2 emission for engine size {engine_size}: {predict:.2f}")
    else:
        st.error("Plase enter a valid engine size.")