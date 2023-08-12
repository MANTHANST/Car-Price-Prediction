import streamlit as st
import pickle
import pandas as pd
import numpy as np

def get_models(company):
    car_models = []
    l = list(cars["name"].str.split().drop_duplicates())
    for i in range(len(l)):
        if (l[i][0] == company):
            car_models.append(" ".join(l[i]))
    return car_models

def predict_price():

    prediction = model.predict(pd.DataFrame([[mod, com, yop, kt, ft]], columns=["name", "company", "year", "kms_driven", "fuel_type"]))
    return "{:,}".format(np.round(prediction[0], 0))

model = pickle.load(open("LinearRegreessionModel.pkl", "rb"))

cars = pd.read_csv("Cleaned Car.csv")

st.title("Car Price Prediction")

com = st.selectbox("Select Company", options = ["Select Company"] + sorted(cars["company"].drop_duplicates()))
mod = st.selectbox("Select Model", options = ["Select Model"] + get_models(com))

col1, col2, col3 = st.columns(3)
with col1:
    yop = st.selectbox("Select Year of Purchase", options=["Select Year"] + [i for i in range(2023, 1849, -1)])
with col2:
    ft = st.selectbox("Select Fuel Type", options=["Select Fuel Type"] + list(cars["fuel_type"].drop_duplicates()))
with col3:
    kt = st.number_input("Enter Number of Kilometers Travelled", min_value = 0.0, step = 0.1)

if st.button("Predict", use_container_width = True):

    try:
        label = "Predicted Price : ₹ " + predict_price()
        centered_bold_label = f"<h3 style='text-align: center;'><b>{label}</b></h3>"
        st.write(centered_bold_label, unsafe_allow_html=True)
        # st.write("Prediction : ₹", predict_price())
    except:
        st.write("Please Select From Every Option")
