# Diabetes Prediction App

An end-to-end machine learning application for predicting diabetes-related outcomes from health, demographic, and lifestyle indicators.

This project demonstrates the complete workflow of taking an open-source healthcare dataset, performing data analysis and preprocessing, training a machine learning model, integrating the trained model into a Streamlit application, containerizing the application with Docker, and automating testing and deployment through GitHub Actions.

The application also records prediction submissions locally in CSV format, including user identification, input features, prediction results, and timestamps.

---

## Project Overview

The project follows this machine learning and deployment pipeline:

```text
Open-Source Dataset
        |
        v
Data Analysis and Preprocessing
        |
        v
Feature Engineering / Preparation
        |
        v
Model Training
        |
        v
AdaBoost Classifier
        |
        v
Saved Model (model.pkl)
        |
        v
Streamlit Application
        |
        v
Docker Container
        |
        v
GitHub Repository
        |
        v
GitHub Actions CI/CD
        |
        +-------------------+
        |                   |
        v                   v
Application Testing     Docker Image Build
                            |
                            v
                       Docker Hub
```

---

## Features

### Machine Learning

* Uses an open-source diabetes health indicators dataset.
* Performs data analysis and preprocessing in a Jupyter Notebook.
* Trains a machine learning classification model.
* Uses an AdaBoost Classifier for prediction.
* Saves the trained model as `model.pkl`.
* Uses the same feature structure during training and inference.

### Streamlit Application

The application provides an interactive interface where users can enter:

#### User Information

* Name
* Country

#### Health Information

* High blood pressure
* High cholesterol
* Cholesterol check
* BMI
* Smoking status
* History of stroke
* Heart disease or heart attack
* Physical activity
* Fruit consumption
* Vegetable consumption
* Heavy alcohol consumption
* Healthcare coverage
* Difficulty accessing healthcare due to cost
* Difficulty walking

#### Additional Information

* General health
* Days of poor mental health
* Days of poor physical health
* Sex
* Age category
* Education level
* Income category

The application converts the user-friendly selections into the numerical values expected by the trained model.

---

## Prediction

After entering the required information, the user can click:

```text
Predict Diabetes
```

The trained model processes the input and returns a prediction.

The application displays either:

```text
Diabetes detected
```

or:

```text
No diabetes detected
```

The prediction is then recorded locally in a CSV file.

---

## Prediction Data Storage

The application automatically creates:

```text
data/predictions.csv
```

when the first prediction is submitted.

Each prediction record contains:

* Name
* Country
* HighBP
* HighChol
* CholCheck
* BMI
* Smoker
* Stroke
* HeartDiseaseorAttack
* PhysActivity
* Fruits
* Veggies
* HvyAlcoholConsump
* AnyHealthcare
* NoDocbcCost
* GenHlth
* MentHlth
* PhysHlth
* DiffWalk
* Sex
* Age
* Education
* Income
* Prediction
* Prediction_Result
* Timestamp

New predictions are appended to the existing CSV rather than replacing previous records.

### Privacy

`predictions.csv` is excluded from Git using `.gitignore`.

This prevents locally collected prediction records and user-provided information from being accidentally committed to the public GitHub repository.

The original open-source dataset remains available in:

```text
data/diabetes_012_health_indicators_BRFSS2015.csv
```

---

# Project Structure

```text
Diabetes-Prediction-App/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── data/
│   ├── diabetes_012_health_indicators_BRFSS2015.csv
│   └── predictions.csv
│
├── notebooks/
│   └── Diabetes.ipynb
│
├── app.py
├── model.pkl
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

# File Descriptions

## `app.py`

The main Streamlit application.

It:

1. Loads the trained model.
2. Displays the user interface.
3. Collects user information.
4. Collects health and lifestyle information.
5. Converts categorical inputs into numerical values.
6. Creates a Pandas DataFrame.
7. Sends the data to the trained model.
8. Displays the prediction.
9. Saves the prediction to `data/predictions.csv`.

---

## `model.pkl`

The serialized trained machine learning model.

The application loads it using:

```python
model = joblib.load("model.pkl")
```

The model is then used to generate predictions from the information submitted through the Streamlit interface.

---

## `notebooks/Diabetes.ipynb`

The machine learning development notebook.

It contains the model-development workflow, including:

* Dataset loading
* Exploratory data analysis
* Data preprocessing
* Feature preparation
* Model training
* Model evaluation
* Model selection
* Model serialization

The trained model generated from the notebook is saved as:

```text
model.pkl
```

---

## `data/diabetes_012_health_indicators_BRFSS2015.csv`

The original open-source dataset used for developing the machine learning model.

The dataset contains health and lifestyle indicators associated with diabetes-related outcomes.

---

## `data/predictions.csv`

Local application-generated data containing prediction submissions.

This file is intentionally ignored by Git because it may contain user-provided information.

---

## `Dockerfile`

Defines how the application is packaged into a Docker image.

The Docker image contains the application and its required Python dependencies, allowing the application to run consistently across different environments.

---

## `requirements.txt`

Contains the Python packages required to run the application.

Examples include:

```text
streamlit
pandas
scikit-learn
joblib
```

The exact dependencies are defined in the project's `requirements.txt`.

---

## `.github/workflows/ci-cd.yml`

Defines the GitHub Actions CI/CD pipeline.

The workflow automatically runs when changes are pushed to the `main` branch.

---

# Machine Learning Workflow

## 1. Dataset

The project uses an open-source dataset containing health and lifestyle indicators.

The dataset provides features such as:

* Blood pressure
* Cholesterol
* BMI
* Smoking
* Physical activity
* General health
* Mental health
* Physical health
* Age
* Education
* Income

These variables are used as input features for the machine learning model.

---

## 2. Data Analysis

The dataset is explored and analyzed in:

```text
notebooks/Diabetes.ipynb
```

The analysis helps understand:

* Dataset structure
* Feature distributions
* Missing values
* Relationships between variables
* Target distribution
* Feature characteristics

---

## 3. Data Preprocessing

The features are prepared for machine learning.

The application maintains the same feature representation used during model training.

For example, the Streamlit application converts:

```text
Yes → 1
No  → 0
```

and categorical variables such as age and education into the numerical categories expected by the trained model.

---

## 4. Model Training

The project uses an:

```text
AdaBoost Classifier
```

AdaBoost is an ensemble learning method that combines multiple weak learners to create a stronger predictive model.

The final trained model is serialized using Joblib and stored as:

```text
model.pkl
```

---

# Application Architecture

The deployed application can be represented as:

```text
                    User
                     |
                     v
             Streamlit Interface
                     |
                     v
             User Input Processing
                     |
                     v
             Pandas DataFrame
                     |
                     v
                model.pkl
                     |
                     v
              AdaBoost Model
                     |
                     v
                Prediction
                  /     \
                 /       \
                v         v
       Diabetes detected   No diabetes detected
                 \         /
                  \       /
                   v     v
                CSV Storage
                     |
                     v
             predictions.csv
```

---

# Docker Deployment

The application is containerized using Docker.

Building the Docker image allows the application to run independently of the local Python environment.

## Build Docker Image

From the project directory:

```powershell
docker build -t diabetes-app .
```

## Run the Application

```powershell
docker run -p 8501:8501 diabetes-app
```

The application can then be accessed at:

```text
http://localhost:8501
```

---

# Docker Hub

The Docker image is published to Docker Hub through the CI/CD pipeline.

The repository uses the Docker image:

```text
faaizantarkan/diabetes-app:latest
```

The image can be run with:

```powershell
docker run -p 8501:8501 faaizantarkan/diabetes-app:latest
```

Then open:

```text
http://localhost:8501
```

---

# CI/CD Pipeline

GitHub Actions is used to automate the application deployment workflow.

Whenever code is pushed to the `main` branch, the pipeline automatically performs the following stages:

```text
Git Push
   |
   v
GitHub Actions
   |
   v
Test Application
   |
   v
Build Docker Image
   |
   v
Push Image to Docker Hub
```

## Stage 1: Test Application

The pipeline installs the required dependencies and tests whether the application can run successfully.

This helps identify problems before creating and publishing a Docker image.

---

## Stage 2: Build Docker Image

After the application test succeeds, GitHub Actions builds the Docker image using the project's `Dockerfile`.

Conceptually:

```text
Dockerfile
    +
Application
    +
Dependencies
    |
    v
Docker Image
```

---

## Stage 3: Push Image to Docker Hub

After the Docker image is successfully built, GitHub Actions authenticates with Docker Hub using GitHub repository secrets and pushes the image.

The image is published as:

```text
faaizantarkan/diabetes-app:latest
```

This means a successful code push can automatically result in a new Docker image being available on Docker Hub.

---

# GitHub Actions Workflow

The current pipeline provides:

```text
Continuous Integration
        |
        +--> Test Application
        |
        +--> Validate Application
        |
        v
Continuous Deployment
        |
        +--> Build Docker Image
        |
        +--> Push Docker Image
        |
        v
Docker Hub
```

The current pipeline **does not automatically retrain the machine learning model**.

# Technologies Used

## Programming

* Python

## Data Science

* Pandas
* NumPy
* Scikit-learn

## Machine Learning

* AdaBoost
* Joblib

## Application

* Streamlit

## Containerization

* Docker

## Version Control

* Git
* GitHub

## CI/CD

* GitHub Actions

## Container Registry

* Docker Hub

## Development

* Jupyter Notebook

---

# Key Learning Outcomes

This project demonstrates practical experience with:

* Machine learning model development
* Data preprocessing
* Classification
* Ensemble learning
* Model serialization
* Streamlit application development
* Docker containerization
* Git version control
* GitHub repository management
* GitHub Actions
* Continuous Integration
* Continuous Deployment
* Docker Hub deployment
* Basic application data persistence
* Separation of application data from source-controlled data

---

# Future Improvements

Potential future improvements include:

## 1. Duplicate User Detection

The application can be extended to identify returning users using a unique identifier rather than simply appending every prediction.

For example:

```text
User Identification
        |
        v
Check Existing Records
        |
    +---+---+
    |       |
 Existing   New
    |       |
    v       v
Update    Create
Record    Record
```

---

## 2. Automated Model Retraining

Prediction data could eventually be incorporated into a controlled model-training pipeline.

A more advanced MLOps architecture could be:

```text
Prediction Data
       |
       v
Data Validation
       |
       v
Data Preprocessing
       |
       v
Model Training
       |
       v
Model Evaluation
       |
       v
Model Registry
       |
       v
Model Deployment
```

This should only be implemented after establishing proper data validation and labeling procedures.

---

## 3. Database Integration

Instead of storing application records in CSV, a database could be introduced.

Potential architecture:

```text
Streamlit
    |
    v
Application Backend
    |
    v
Database
```

This would be more suitable for handling larger numbers of users and prediction records.

---

## 4. Model Monitoring

Future versions could monitor:

* Prediction distributions
* Data drift
* Feature drift
* Model performance
* Prediction volume
* Model version

---

## 5. Model Versioning

Future versions could maintain multiple model versions:

```text
model_v1.pkl
model_v2.pkl
model_v3.pkl
```

and track which model generated each prediction.

---

## 6. Cloud Deployment

The Dockerized application could eventually be deployed to a cloud platform rather than only running locally or through Docker.

---

# Important Note

This application is a **machine learning demonstration project** and should not be treated as a medical diagnostic system.

The model's output is a prediction based on the data and model used in this project. It should not be used as a substitute for professional medical evaluation or diagnosis.

---

# License

This project is distributed under the license included in the repository.

See:

```text
LICENSE
```

for the complete license terms.

---

# Project Status

Current implementation:

```text
Data Analysis                    Complete
Model Training                   Complete
AdaBoost Model                   Complete
Model Serialization              Complete
Streamlit Application             Complete
Docker Containerization            Complete
GitHub Repository                 Complete
GitHub Actions Testing             Complete
Docker Image Build                Complete
Docker Hub Deployment              Complete
Local Prediction Storage           Complete
Duplicate User Detection           Planned
Automated Model Retraining         Planned
Model Monitoring                   Planned
```

---

# Author
**Faizan Faisal**

This project was developed as part of a self-directed machine learning and MLOps portfolio, focusing on building an end-to-end machine learning application from dataset and model development through containerization and automated deployment.
