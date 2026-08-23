import streamlit as st
import joblib
import pandas as pd

# Page title and description
st.title("Diabetes Prediction App")

st.write("Currently, The app is under development.")
st.write("Enter the patient's information below.")


# Load the trained machine learning model
model = joblib.load("model.pkl")

# Helper function for Yes/No questions
# Converts: "No"  -> 0 and "Yes" -> 1

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
CholCheck = yes_no_input("Cholesterol Check in Last 5 Years")
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
PhysActivity = yes_no_input("Physical Activity")
# Fruit consumption
Fruits = yes_no_input("Consumes Fruit")
# Vegetable consumption
Veggies = yes_no_input("Consumes Vegetables")
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


# ---------------------------------------------------------
# Other Information
# ---------------------------------------------------------

st.subheader("Additional Information")


# General health:
# 1 = Excellent
# 2 = Very Good
# 3 = Good
# 4 = Fair
# 5 = Poor

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

# Convert the selected label to the numeric value
# expected by the machine learning model
GenHlth = health_categories[health_label]

# Number of days during the past 30 days
# when mental health was not good

MentHlth = st.slider(
    "Days of Poor Mental Health in the Last 30 Days",
    min_value=0,
    max_value=30,
    value=0
)

# Number of days during the past 30 days
# when physical health was not good

PhysHlth = st.slider(
    "Days of Poor Physical Health in the Last 30 Days",
    min_value=0,
    max_value=30,
    value=0
)

# Sex:
# 0 = Female
# 1 = Male

Sex = st.selectbox(
    "Sex",
    ["Female", "Male"]
)
# Convert the selected label to the value expected by the model
Sex = 0 if Sex == "Female" else 1


# Age category used by the original dataset

# Age Category
# ---------------------------------------------------------
# The dataset uses age categories from 1 to 13.
# We display meaningful age ranges to the user.

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

# Convert the selected age range to the dataset's numeric value
Age = age_categories[age_label]

# Education level:
# 1 = Never attended school
# 2 = Elementary
# 3 = Some high school
# 4 = High school graduate
# 5 = Some college
# 6 = College graduate

# ---------------------------------------------------------
# Education Level
# ---------------------------------------------------------
# Dataset encoding:
# 1 = Never attended school
# 2 = Elementary
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

# Convert the selected label to the dataset's numeric value
Education = education_categories[education_label]


# Income category used by the original dataset

# Dataset income categories:
# 1 = Less than $10,000
# 2 = $10,000-$14,999
# 3 = $15,000-$19,999
# 4 = $20,000-$24,999
# 5 = $25,000-$34,999
# 6 = $35,000-$49,999
# 7 = $50,000-$74,999
# 8 = $75,000+

income_categories = {
    "Less than $10,000": 1,
    "$10,000 - $14,999": 2,
    "$15,000 - $19,999": 3,
    "$20,000 - $24,999": 4,
    "$25,000 - $34,999": 5,
    "$35,000 - $49,999": 6,
    "$50,000 - $74,999": 7,
    "$75,000 or more": 8
}

income_label = st.selectbox(
    "Income Category",
    list(income_categories.keys())
)

# Convert the selected label to the dataset's numeric value
Income = income_categories[income_label]

# Create prediction button
if st.button("Predict Diabetes"):

    # Create a DataFrame containing all 21 features
    # in the exact order expected by the trained model

    input_data = pd.DataFrame([[
        HighBP,
        HighChol,
        CholCheck,
        BMI,
        Smoker,
        Stroke,
        HeartDiseaseorAttack,
        PhysActivity,
        Fruits,
        Veggies,
        HvyAlcoholConsump,
        AnyHealthcare,
        NoDocbcCost,
        GenHlth,
        MentHlth,
        PhysHlth,
        DiffWalk,
        Sex,
        Age,
        Education,
        Income
    ]], columns=[
        "HighBP",
        "HighChol",
        "CholCheck",
        "BMI",
        "Smoker",
        "Stroke",
        "HeartDiseaseorAttack",
        "PhysActivity",
        "Fruits",
        "Veggies",
        "HvyAlcoholConsump",
        "AnyHealthcare",
        "NoDocbcCost",
        "GenHlth",
        "MentHlth",
        "PhysHlth",
        "DiffWalk",
        "Sex",
        "Age",
        "Education",
        "Income"
    ])

    # Make the prediction
    prediction = model.predict(input_data)

    # Display the prediction
    if prediction[0] == 1:
        st.error("Diabetes detected")
    else:
        st.success("No diabetes detected")