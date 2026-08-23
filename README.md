# Diabetes Prediction App

A machine learning web application that predicts the likelihood of diabetes using health and lifestyle indicators.

The application uses an **AdaBoost Classifier** trained on the **CDC BRFSS 2015 Diabetes Health Indicators dataset** and provides an interactive interface built with **Streamlit**.

The project is also containerized using **Docker** and includes a **GitHub Actions CI/CD pipeline** for automated testing and Docker image building.

---

## 🚀 Project Overview

This project demonstrates an end-to-end machine learning deployment workflow:

```text
Open-source Dataset
        ↓
Data Analysis & Preprocessing
        ↓
Model Training
        ↓
AdaBoost Classifier
        ↓
Model Serialization
        ↓
Streamlit Application
        ↓
Docker Container
        ↓
GitHub Actions CI/CD
