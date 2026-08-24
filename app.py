# Import Libraries
import streamlit as st
import joblib
import pandas as pd
import os

# Page Title and Description

st.title("Diabetes Prediction App")

st.write("Currently, the app is under development.")
st.write("Enter the patient's information below.")

# User Information
st.subheader("User Information")
name = st.text_input("Name")
country = st.text_input("Country")

# Load Trained Machine Learning Model
model = joblib.load("model.pkl")

# Helper Function for Yes/No Questions
# Converts:
# "No"  -> 0
# "Yes" -> 1

def yes_no_input(label):
    answer = st.selectbox(label, ["No", "Yes"])
    return 1 if answer == "Yes" else 0

# Health Information
st.subheader("Health Information")

# High blood pressure
HighBP = yes_no_input("High Blood Pressure")

# High cholesterol
HighChol = yes_no_input("High Cholesterol")

# Cholesterol check in the last 5 years
CholCheck = yes_no_input(
    "Cholesterol Check in Last 5 Years"
)

# Body Mass Index
BMI = st.number_input(
    "BMI",
    min_value=0.0,
    max_value=100.0,
    value=25.0
)

# Smoker
Smoker = yes_no_input("Smoker")

# History of stroke
Stroke = yes_no_input("History of Stroke")

# History of heart disease or heart attack
HeartDiseaseorAttack = yes_no_input(
    "Heart Disease or Heart Attack"
)

# Physical activity
PhysActivity = yes_no_input(
    "Physical Activity"
)

# Fruit consumption
Fruits = yes_no_input(
    "Consumes Fruit"
)

# Vegetable consumption
Veggies = yes_no_input(
    "Consumes Vegetables"
)

# Heavy alcohol consumption
HvyAlcoholConsump = yes_no_input(
    "Heavy Alcohol Consumption"
)

# Healthcare coverage
AnyHealthcare = yes_no_input(
    "Has Healthcare Coverage"
)

# Could not see doctor because of cost
NoDocbcCost = yes_no_input(
    "Could Not See Doctor Due to Cost"
)

# Difficulty walking
DiffWalk = yes_no_input(
    "Difficulty Walking"
)

# Additional Information
st.subheader("Additional Information")

# General Health
# Dataset encoding:
# 1 = Excellent
# 2 = Very good
# 3 = Good
# 4 = Fair
# 5 = Poor

health_categories = {
    "Excellent": 1,
    "Very good": 2,
    "Good": 3,
    "Fair": 4,
    "Poor": 5
}

health_label = st.selectbox(
    "General Health",
    list(health_categories.keys())
)

# Convert selected label to numerical value
GenHlth = health_categories[health_label]

# Mental Health
# Number of days during the past 30 days
# when mental health was not good

MentHlth = st.slider(
    "Days of Poor Mental Health in the Last 30 Days",
    min_value=0,
    max_value=30,
    value=0
)

# Physical Health
# Number of days during the past 30 days
# when physical health was not good

PhysHlth = st.slider(
    "Days of Poor Physical Health in the Last 30 Days",
    min_value=0,
    max_value=30,
    value=0
)

# Sex
# Dataset encoding:
# 0 = Female
# 1 = Male

Sex = st.selectbox(
    "Sex",
    ["Female", "Male"]
)

# Convert selected value to numerical value
Sex = 0 if Sex == "Female" else 1

# Age Category
# The original dataset uses age categories from 1 to 13.

age_categories = {
    "18-24": 1,
    "25-29": 2,
    "30-34": 3,
    "35-39": 4,
    "40-44": 5,
    "45-49": 6,
    "50-54": 7,
    "55-59": 8,
    "60-64": 9,
    "65-69": 10,
    "70-74": 11,
    "75-79": 12,
    "80+": 13
}

age_label = st.selectbox(
    "Age",
    list(age_categories.keys())
)

# Convert age range to numerical dataset value
Age = age_categories[age_label]

# Education Level
# Dataset encoding:
# 1 = Never attended school
# 2 = Elementary school
# 3 = Some high school
# 4 = High school graduate
# 5 = Some college
# 6 = College graduate

education_categories = {
    "Never attended school": 1,
    "Elementary school": 2,
    "Some high school": 3,
    "High school graduate": 4,
    "Some college": 5,
    "College graduate": 6
}

education_label = st.selectbox(
    "Education Level",
    list(education_categories.keys())
)

# Convert selected education level to numerical value
Education = education_categories[education_label]

# Income Category
# Dataset encoding:
# 1 = Less than $10,000
# 2 = $10,000 - $14,999
# 3 = $15,000 - $19,999
# 4 = $20,000 - $24,999
# 5 = $25,000 - $34,999
# 6 = $35,000 - $49,999
# 7 = $50,000 - $74,999
# 8 = $75,000 or more

income_categories = {
    "Less than $10,000": 1,
    "$10,000 - $14,999": 2,
    "$15,000 - $19,999": 3,
    "$20,000 - $24,999": 4,
    "$25,000 - $34,999": 5,
    "$25,000 - $34,999": 5,
    "$35,000 - $49,999": 6,
    "$50,000 - $74,999": 7,
    "$75,000 or more": 8
}

income_label = st.selectbox(
    "Income Category",
    list(income_categories.keys())
)

# Convert selected income category to numerical value
Income = income_categories[income_label]

# Prediction

if st.button("Predict Diabetes"):

    # Create DataFrame with all 21 model features
    input_data = pd.DataFrame([{
        "HighBP": HighBP,
        "HighChol": HighChol,
        "CholCheck": CholCheck,
        "BMI": BMI,
        "Smoker": Smoker,
        "Stroke": Stroke,
        "HeartDiseaseorAttack": HeartDiseaseorAttack,
        "PhysActivity": PhysActivity,
        "Fruits": Fruits,
        "Veggies": Veggies,
        "HvyAlcoholConsump": HvyAlcoholConsump,
        "AnyHealthcare": AnyHealthcare,
        "NoDocbcCost": NoDocbcCost,
        "GenHlth": GenHlth,
        "MentHlth": MentHlth,
        "PhysHlth": PhysHlth,
        "DiffWalk": DiffWalk,
        "Sex": Sex,
        "Age": Age,
        "Education": Education,
        "Income": Income
    }])

    # Make Prediction
    prediction = model.predict(input_data)[0]

    # Display Prediction
    if prediction == 1:

        result = "Diabetes detected"

        st.error(result)

    else:

        result = "No diabetes detected"

        st.success(result)

    # Save Prediction to CSV

    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # CSV file location
    csv_file = "data/predictions.csv"

    # Create a copy of the model input
    new_record = input_data.copy()

    # Add user information
    new_record.insert(0, "Name", name)
    new_record.insert(1, "Country", country)

    # Add prediction
    new_record["Prediction"] = prediction

    # Add readable prediction result
    new_record["Prediction_Result"] = result

    # Add timestamp
    new_record["Timestamp"] = pd.Timestamp.now()

    # Append to Existing CSV or Create New CSV
    if os.path.exists(csv_file):

        # Append new record
        new_record.to_csv(
            csv_file,
            mode="a",
            header=False,
            index=False
        )

    else:

        # Create new CSV
        new_record.to_csv(
            csv_file,
            mode="w",
            header=True,
            index=False
        )


    # Confirm that the record was saved
    st.success("Prediction saved successfully.")