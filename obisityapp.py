import streamlit as st
import joblib
import numpy as np

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Obesity Level Predictor",
    page_icon="🏥",
    layout="centered"
)

# -------------------------------
# Load Model
# -------------------------------
model = joblib.load("obesity_rf_model.pkl")
label_encoder = joblib.load("obesity_label_encoder.pkl")

# -------------------------------
# App Title
# -------------------------------
st.title("🏥 Obesity Level Prediction App")
st.write(
    "This application predicts the **obesity level** based on physical and lifestyle attributes."
)

st.markdown("---")

# -------------------------------
# Input Section
# -------------------------------

st.subheader("Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    height = st.number_input("Height (meters)", min_value=1.0, max_value=2.5, value=1.70)
    weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, value=70.0)

with col2:
    family_history = st.selectbox(
        "Family History of Overweight",
        ["yes", "no"]
    )

    faf = st.slider(
        "Physical Activity Frequency (per week)",
        0, 3
    )

    favc = st.selectbox(
        "Frequent High Calorie Food Consumption",
        ["yes", "no"]
    )

# -------------------------------
# BMI Calculation
# -------------------------------
bmi = weight / (height ** 2)

st.info(f"📊 Your BMI is **{bmi:.2f}**")

st.markdown("---")

# -------------------------------
# Convert Inputs
# -------------------------------
family_history = 1 if family_history == "yes" else 0
favc = 1 if favc == "yes" else 0

input_data = np.array([[age, height, weight, family_history, faf, favc]])

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Obesity Level"):

    prediction = model.predict(input_data)

    result = label_encoder.inverse_transform(prediction)

    st.success(f"Predicted Obesity Level: **{result[0]}**")

    if result[0] == "Normal_Weight":
        st.success("✅ You are in a healthy weight range.")
    else:
        st.warning("⚠️ Consider improving lifestyle habits and consulting a healthcare professional.")

st.markdown("---")

st.caption("Machine Learning Model: Random Forest | Built with Streamlit")