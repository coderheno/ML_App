import streamlit as st
import joblib

# Load model
model = joblib.load("loan_model.pkl")

st.title("Loan Approval Prediction")

age = st.number_input("Enter Age", min_value=18, max_value=100)

income = st.number_input("Enter Annual Income", min_value=0)

loan = st.number_input("Enter Loan Amount", min_value=0)

if st.button("Predict"):

    input_data = [[age, income, loan]]

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Not Approved")