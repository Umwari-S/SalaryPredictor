import pickle #pickle a built-in python library that saves and loads machine learning models saved in files
import numpy as np #is used for working with numbers, arrays and math
import streamlit as st #streamlit helps us build interactive web apps using python code
import datetime #helps us get more option for date and be specific with our bounds

with open('model.pkl', 'rb') as f:#here we are telling our interpreter to open the file title 'model.pkl' in binary(br) mode and call it f
    model = pickle.load(f) #we use the library 'pickle' to read model data from the file and load it into the variable 'model'
#the following two lines of code are for web page headings
st.markdown("<h1 style='text-align: center; font-size: 48px; font-weight: bold;'>Salary Predictor</h1>", unsafe_allow_html=True)
#shows a big bold title in the center of the web page which in this case is the name of our web app 
st.markdown("<h3 style='text-align: center; color: gray;'>A simple web app to predict annual salary</h3>", unsafe_allow_html=True)
#this creates a sub-heading in grey which is explaining what our web page does

#here we collect the person's data, the name, age, date of birth and marital status. They are not used for prediction(except for age) but are helpful for identification and just to be stored
first_name = st.text_input("First Name") 
last_name = st.text_input("Last Name")
age = st.number_input("Your Age", 0, 100, 25, 1)# sets the range of ages to between 0-100, displays 25 at first, and goes on increasing/decreasing 1 value at a time
dob = st.date_input(
    "Your Birthday",
    min_value=datetime.date(1950, 1, 1),#sets the years to start from 1950
    max_value=datetime.date.today()) #makes sure the user doesn't select a year above the current one for their dob
marital_status = st.radio("Marital Status", ["Single", "Married"])#user choses their marital status

#The following are list options that the user will select from for gender, education and job title(they are important in predicting the salary)
gen_list = ["Female", "Male"]
edu_list = ["Bachelor's", "Master's", "PhD"]
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"]
job_idx = [0, 1, 10, 11, 20]#this gives each job a number(value) for the model(which will compute the salary prediction)

#now here the user selects their gender, educationa and job from the available options
gender = st.radio('Pick your gender', gen_list)
education = st.selectbox('Pick your education level', edu_list)
job = st.selectbox('Pick your job title', job_list)
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")#user picks their years of experience and the option are between 0 and 25 and increase by 0.5

predict_btn = st.button('Predict Salary')#this is a button that when clicked shows the predicted salary and internally executes the next block of code

if(predict_btn):#if the predict button is clicked then our interpreter begins computing
    #the followind lines of code convert ucer inputs into numbers the model can understand and use to compute
    inp1 = int(age)
    inp2 = float(experience)
    inp3 = int(job_idx[job_list.index(job)])#finds the job's index from job_list and gets its numeric value from job_idx
    inp4 = int(edu_list.index(education))# education as a number
    inp5 = int(gen_list.index(gender))# gender as a number
    X = [inp1, inp2, inp3, inp4, inp5]# groups all the inputs into a list called X
    salary = model.predict([X])#used the model to predict the salary based on the inputs
    st.text(f"Estimated salary: ${int(salary[0])}")# displays the predicted salaru
