import pandas as pd
import numpy as np
import joblib
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Water Pollutants Predictor", layout="wide")

st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #cce5ff;
    }
    </style>
    """, unsafe_allow_html=True)

model = joblib.load(r"E:\\water-quality-prediction\\pollution_model.pkl")
model_cols = joblib.load(r"E:\\water-quality-prediction\\model_columns.pkl")

safe_limits = {
    'NH4': lambda x: x < 0.5,
    'BSK5': lambda x: x < 3,
    'Suspended': lambda x: x < 25,
    'O2': lambda x: x > 5,
    'NO3': lambda x: x < 10,
    'NO2': lambda x: x < 0.1,
    'SO4': lambda x: x < 250,
    'PO4': lambda x: x < 0.1,
    'CL': lambda x: x < 250
}
pollutants = list(safe_limits.keys())

st.sidebar.title("💧 Input Parameters")
year_input = st.sidebar.number_input("Enter Year", min_value=2000, max_value=2100, value=2022)
month_input = st.sidebar.selectbox("Select Month (optional)", options=["None"] + list(range(1, 13)))
month_input = None if month_input == "None" else int(month_input)
station_id = st.sidebar.selectbox("Select Station ID", options=[str(i) for i in range(1, 23)])
predict_button = st.sidebar.button("Predict")

st.title("💧 Water Quality Prediction Dashboard")

if predict_button:
    if not station_id:
        st.sidebar.warning('⚠️ Please enter the station ID')
    else:
        input_dict = {'year': [year_input], 'id': [station_id]}
        if month_input is not None:
            input_dict['month'] = [month_input]
        input_df = pd.DataFrame(input_dict)
        input_encoded = pd.get_dummies(input_df, columns=['id'], drop_first=True)

        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]

        predicted_pollutants = model.predict(input_encoded)[0]

        col1, col2 = st.columns([1.1, 1.2])  

        with col1:
            st.subheader(f"📍 Station: '{station_id}' | Year: {year_input}" + (f" | Month: {month_input}" if month_input else ""))
            safe_count = 0
            for p, val in zip(pollutants, predicted_pollutants):
                status = "✅ Safe" if safe_limits[p](val) else "❌ Polluted"
                if status == "✅ Safe":
                   safe_count += 1
                st.markdown(f"**{p}**: {val:.2f} mg/L → {status}")

        if safe_count == len(pollutants):
            st.success("✅ Overall Water Quality:  Safe")
        else:
            st.error("❌ Overall Water Quality:  Polluted")

        with col2:
           import matplotlib.pyplot as plt
           fig, ax = plt.subplots(figsize=(4.5, 3.5))  
           colors = ['#90ee90' if safe_limits[p](val) else '#ff9999' for p, val in zip(pollutants, predicted_pollutants)]
           ax.bar(pollutants, predicted_pollutants, color=colors)
           ax.set_ylabel("mg/L")
           ax.set_xticklabels(pollutants, rotation=45, ha='right')
           ax.set_title("")  
           ax.spines[['top', 'right']].set_visible(False)
           st.pyplot(fig)

