import streamlit as st
import pickle
import pandas as pd

st.title('AKI Prediction')

mod_dict = {
    "CABG":pickle.load(open("cabg_mod.pkl","rb")),
    "Aortic":pickle.load(open("aortic_mod.pkl", "rb")),
    "Valve":pickle.load(open("valve_mod.pkl", "rb"))
}

models = st.selectbox("Select Model", list(mod_dict.keys()))

# preop factors
gender = st.selectbox("Gender", ("M","F"))
bmi = st.slider("BMI", 0,80, step=1)
dm = st.radio("Diabetes", ("Yes","No"))
base_hgb = st.slider("Base Hgb", 3, 20, 8, step=0.5)