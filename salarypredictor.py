import pickle
import numpy as np
import streamlit as st

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.markdown("<h1 style='text-align: center; font-size: 48px; font-weight: bold;'>Salary Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>A simple web app to predict annual salary</h3>", unsafe_allow_html=True)


first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
age = st.number_input("Your Age", 0, 100, 25, 1)
dob = st.date_input("Your Birthday")
marital_status = st.radio("Marital Status", ["Single", "Married"])


gen_list = ["Female", "Male"]
edu_list = ["Bachelor's", "Master's", "PhD"]
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"]
job_idx = [0, 1, 10, 11, 20]

gender = st.radio('Pick your gender', gen_list)
education = st.selectbox('Pick your education level', edu_list)
job = st.selectbox('Pick your job title', job_list)
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")

predict_btn = st.button('Predict Salary')

if(predict_btn):
    inp1 = int(age)
    inp2 = float(experience)
    inp3 = int(job_idx[job_list.index(job)])
    inp4 = int(edu_list.index(education))
    inp5 = int(gen_list.index(gender))
    X = [inp1, inp2, inp3, inp4, inp5]
    salary = model.predict([X])
    st.text(f"Estimated salary: ${int(salary[0])}")
