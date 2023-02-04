import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", 'rb'))

def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return prediction

st.header("Iris Flower Prediction App")
st.subheader("This app predicts the Iris flower type")


sepal_length = st.sidebar.slider("Sepal Length", 4.3,7.9,5.4)
sepal_width = st.sidebar.slider("Sepal Width", 2.0,4.4,3.4)
petal_length = st.sidebar.slider("Petal Length", 1.0,6.9,1.3)
petal_width = st.sidebar.slider("Petal Width", 0.1,2.5,0.2)

if st.button("Classify"):
    result = predict_iris(sepal_length, sepal_width, petal_length, petal_width)
    st.success('The output is {}'.format(result))