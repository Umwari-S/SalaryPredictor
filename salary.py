import streamlit as st

st.title("Title: Bio Data")
st.write("This is a sample web app")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
age = st.number_input("Your Age", 0, 100, 25, 1)
gender = st.radio("Gender", ["Male", "Female"])
dob = st.date_input("Your Birthday")
marital_status = st.radio("Marital Status", ["Single", "Married"])
years_of_experience = st.slider("Years of experience", 0, 40)



