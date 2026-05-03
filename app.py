import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Telecom Churn Predictor",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1a1a2e;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #6c757d;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
    }
    .risk-high {
        background: #ff4b4b;
        color: white;
        padding: 1rem 2rem;
        border-radius: 10px;
        font-size: 1.2rem;
        font-weight: 700;
        text-align: center;
    }
    .risk-low {
        background: #00b894;
        color: white;
        padding: 1rem 2rem;
        border-radius: 10px;
        font-size: 1.2rem;
        font-weight: 700;
        text-align: center;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 2.5rem;
        width: 100%;
        margin-top: 1rem;
    }
    .stButton > button:hover {
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)


# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    model_path = os.path.join("models", "random_forest_model.pkl")
    with open(model_path, "rb") as f:
        return pickle.load(f)

@st.cache_resource
def load_train_test_data():
    data_path = os.path.join("models", "train_test_data.pkl")
    with open(data_path, "rb") as f:
        return pickle.load(f)

try:
    model = load_model()
    model_loaded = True
except Exception as e:
    model_loaded = False
    st.error(f"⚠️ Could not load model: {e}")


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<p class="main-header">📡 Telecom Churn Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Predict whether a customer is likely to leave — powered by a Random Forest model with 82% accuracy.</p>', unsafe_allow_html=True)

st.divider()

# ── Sidebar — Customer Inputs ─────────────────────────────────────────────────
st.sidebar.header("🧑 Customer Profile")
st.sidebar.markdown("Fill in the customer details below to generate a prediction.")

# Demographics
st.sidebar.subheader("Demographics")
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.sidebar.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.sidebar.selectbox("Has Partner", ["Yes", "No"])
dependents = st.sidebar.selectbox("Has Dependents", ["Yes", "No"])

# Services
st.sidebar.subheader("Services")
phone_service = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.sidebar.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.sidebar.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.sidebar.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.sidebar.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.sidebar.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.sidebar.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

# Account Info
st.sidebar.subheader("Account Information")
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.sidebar.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.sidebar.slider("Monthly Charges ($)", 18.0, 120.0, 65.0, step=0.5)
total_charges = monthly_charges * tenure  # derived


# ── Encoding ──────────────────────────────────────────────────────────────────
def encode_inputs():
    binary = {"Yes": 1, "No": 0, "Male": 1, "Female": 0}
    internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}
    tri_map = {"Yes": 1, "No": 0, "No internet service": 2, "No phone service": 2}
    contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
    payment_map = {
        "Electronic check": 0,
        "Mailed check": 1,
        "Bank transfer (automatic)": 2,
        "Credit card (automatic)": 3,
    }

    features = {
        "gender": binary[gender],
        "SeniorCitizen": binary[senior_citizen],
        "Partner": binary[partner],
        "Dependents": binary[dependents],
        "tenure": tenure,
        "PhoneService": binary[phone_service],
        "MultipleLines": tri_map[multiple_lines],
        "InternetService": internet_map[internet_service],
        "OnlineSecurity": tri_map[online_security],
        "OnlineBackup": tri_map[online_backup],
        "DeviceProtection": tri_map[device_protection],
        "TechSupport": tri_map[tech_support],
        "StreamingTV": tri_map[streaming_tv],
        "StreamingMovies": tri_map[streaming_movies],
        "Contract": contract_map[contract],
        "PaperlessBilling": binary[paperless_billing],
        "PaymentMethod": payment_map[payment_method],
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
    }
    return np.array(list(features.values())).reshape(1, -1)


# ── Main Panel ────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("🎯 Model Accuracy", "82%", "Random Forest")
col2.metric("📊 Dataset Size", "7,043", "Customers")
col3.metric("⚠️ Baseline Churn", "26.5%", "Before model")

st.markdown("### 🔮 Prediction")

predict_btn = st.button("Predict Churn Risk", disabled=not model_loaded)

if predict_btn and model_loaded:
    input_data = encode_inputs()

    try:
        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0]
        churn_prob = prob[1] * 100
        retain_prob = prob[0] * 100

        c1, c2 = st.columns(2)

        with c1:
            if prediction == 1:
                st.markdown(f'<div class="risk-high">⚠️ HIGH CHURN RISK<br>{churn_prob:.1f}% probability</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="risk-low">✅ LOW CHURN RISK<br>{churn_prob:.1f}% churn probability</div>', unsafe_allow_html=True)

        with c2:
            st.markdown("**Probability Breakdown**")
            st.progress(int(churn_prob), text=f"Churn: {churn_prob:.1f}%")
            st.progress(int(retain_prob), text=f"Retain: {retain_prob:.1f}%")

        # Risk factors
        st.markdown("### 💡 Key Risk Signals")
        tips = []
        if contract == "Month-to-month":
            tips.append("📋 **Month-to-month contract** — 43% average churn rate. Consider offering an annual plan discount.")
        if tenure < 12:
            tips.append("⏱️ **New customer (< 1 year)** — First year has the highest churn risk (50%). Recommend onboarding support.")
        if internet_service == "Fiber optic":
            tips.append("🌐 **Fiber optic service** — 41.9% churn rate vs 18.9% for DSL. Quality may need review.")
        if tech_support in ["No", "No internet service"]:
            tips.append("🛠️ **No tech support** — Customers without support churn at 41.6% vs 15.2% with support.")
        if monthly_charges > 70:
            tips.append(f"💰 **High monthly charges (${monthly_charges:.0f})** — Churned customers average $74.44/month.")

        if tips:
            for tip in tips:
                st.warning(tip)
        else:
            st.success("✅ No major risk signals detected for this customer profile.")

    except Exception as e:
        st.error(f"Prediction error: {e}. Check that model features match training data.")

elif predict_btn and not model_loaded:
    st.error("Model not loaded. Please ensure `models/random_forest_model.pkl` exists.")

# ── About section ─────────────────────────────────────────────────────────────
with st.expander("ℹ️ About this project"):
    st.markdown("""
    **Customer Churn Prediction** | End-to-end ML project built on the Telco Customer Churn dataset (Kaggle).

    - **Model:** Random Forest (82% accuracy, 0.85 ROC-AUC)
    - **Dataset:** 7,043 customers, 21 features
    - **Key finding:** Contract type and tenure are the strongest predictors of churn
    - **GitHub:** [teekshansalgotra-a11y/churn-prediction-project](https://github.com/teekshansalgotra-a11y/churn-prediction-project)
    """)
