from pathlib import Path
 
import joblib
import pandas as pd
import streamlit as st
 
MODEL_PATH = Path("results/best_heart_model.joblib")
 
st.set_page_config(page_title="Heart Disease Risk Predictor", page_icon="❤️", layout="centered")
 
 
@st.cache_resource
def load_model():
    bundle = joblib.load(MODEL_PATH)
    return bundle["model"], bundle["features"]
 
 
def build_row(p, features):
    """Turn the form answers into the exact columns the model was trained on."""
    row = {
        "age": p["age"],
        "sex": 1 if p["sex"] == "Male" else 0,
        "trestbps": p["trestbps"],
        "chol": p["chol"],
        "fbs": 1 if p["fbs"] == "Yes" else 0,
        "exang": 1 if p["exang"] == "Yes" else 0,
        "oldpeak": p["oldpeak"],
        # chest pain type (baseline = asymptomatic, so all zeros)
        "cp_typical_angina": int(p["cp"] == "Typical angina"),
        "cp_atypical_angina": int(p["cp"] == "Atypical angina"),
        "cp_non_anginal": int(p["cp"] == "Non-anginal pain"),
        # resting ECG (baseline = normal)
        "restecg_lv_hypertrophy": int(p["restecg"] == "LV hypertrophy"),
        "restecg_st_t_abnormality": int(p["restecg"] == "ST-T wave abnormality"),
        # ST slope
        "slope_upsloping": int(p["slope"] == "Upsloping"),
        "slope_flat": int(p["slope"] == "Flat"),
        "slope_downsloping": int(p["slope"] == "Downsloping"),
        # engineered features (same formulas as in the training script)
        "hr_pct_of_max": p["thalach"] / (220 - p["age"]),
        "high_bp": int(p["trestbps"] >= 140),
        "high_chol": int(p["chol"] >= 240),
        "age_over_55": int(p["age"] > 55),
    }
    return pd.DataFrame([row])[features]
 
 
st.title("❤️ Heart Disease Risk Predictor")
st.write("Enter the patient's details and the model estimates the chance of heart disease.")
st.warning("Educational project only. This is **not** a medical diagnosis. "
           "Always consult a doctor for health decisions.")
 
if not MODEL_PATH.exists():
    st.error("Model file not found. Run `python heart_disease_full_pipeline.py archive.zip` "
             "first so that `results/best_heart_model.joblib` is created, "
             "then keep it in a `results` folder next to this file.")
    st.stop()
 
model, features = load_model()
 
with st.sidebar:
    st.header("Settings")
    threshold = st.slider(
        "Alert threshold (%)", 20, 80, 50, 5,
        help="The patient is flagged as high risk when the predicted risk is at or above this. "
             "A lower value catches more sick patients but gives more false alarms.") / 100
    st.caption("Default 50% matches how the model was tested.")
 
with st.form("patient_form"):
    st.subheader("Patient information")
    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input("Age (years)", 18, 100, 55)
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.selectbox("Chest pain type",
                          ["Asymptomatic", "Typical angina", "Atypical angina", "Non-anginal pain"])
        trestbps = st.number_input("Resting blood pressure (mm Hg)", 80, 220, 130)
        chol = st.number_input("Cholesterol (mg/dl)", 100, 600, 240)
        fbs = st.selectbox("Fasting blood sugar above 120 mg/dl?", ["No", "Yes"])
    with c2:
        restecg = st.selectbox("Resting ECG result",
                               ["Normal", "ST-T wave abnormality", "LV hypertrophy"])
        thalach = st.number_input("Maximum heart rate achieved (bpm)", 60, 220, 150)
        exang = st.selectbox("Exercise-induced chest pain?", ["No", "Yes"])
        oldpeak = st.number_input("ST depression during exercise (oldpeak)",
                                  -3.0, 7.0, 1.0, step=0.1)
        slope = st.selectbox("Slope of peak exercise ST segment",
                             ["Upsloping", "Flat", "Downsloping"])
    submitted = st.form_submit_button("Predict", type="primary", use_container_width=True)
 
if submitted:
    answers = dict(age=age, sex=sex, cp=cp, trestbps=trestbps, chol=chol, fbs=fbs,
                   restecg=restecg, thalach=thalach, exang=exang, oldpeak=oldpeak, slope=slope)
    risk = float(model.predict_proba(build_row(answers, features))[0][1])
 
    st.subheader("Result")
    st.metric("Estimated risk of heart disease", f"{risk:.0%}")
    st.progress(min(max(risk, 0.0), 1.0))
 
    if risk >= threshold:
        st.error("**Higher risk.** The model flags this patient. "
                 "A medical check-up is recommended.")
    else:
        st.success("**Lower risk.** The model does not flag this patient. "
                   "This does not rule out heart disease; follow up with a doctor if symptoms exist.")
 
    if oldpeak < 0:
        st.caption("Note: a negative ST depression value is unusual; double-check the entry.")
    if thalach > 220 - age + 20:
        st.caption("Note: this heart rate is well above the usual maximum for this age; "
                   "double-check the entry.")

from pathlib import Path

print(Path.cwd())

from pathlib import Path

print(Path("app.ipynb").exists())

