# Diabetes Prediction App

An end-to-end machine learning application that predicts diabetes-related outcomes from health and lifestyle indicators.

The project combines a trained machine learning model with an interactive Streamlit web application and Docker containerization. GitHub Actions is used to automatically test the application, build the Docker image, and publish the image to Docker Hub whenever changes are pushed to the `main` branch.

## Project Overview

This project demonstrates a complete machine learning application deployment workflow:

```text
Open-Source Dataset
        |
        v
Data Analysis and Preprocessing
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
GitHub Actions CI/CD
        |
        v
Docker Hub
