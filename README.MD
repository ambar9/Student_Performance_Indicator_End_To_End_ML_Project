# STUDENT PERFORMANCE INDICATOR

### Introduction About the Data :

## Problem Statement
This project understand how the student's performance (test scores) is affected by the other variables such as Gender, Ethenicity, Parental Level of Education, Lunch and Test Preparation Course.

**The dataset** The goal is to predict `Marks` of given student (Regression Analysis).

There are 6 independent variables :

* `gender` : sex of students -> (Male/Female).
* `race/ethnicity` : ethnicity of students -> (Group A,B,C,D,E).
* `parental level of education` : parents' final education -> (bachelor's degree, some college, master's degree, associate's degree, high school).
* `lunch` : having lunch before test (standard or free/reduced).
* `reading score` : score of reading subject.
* `writing score` : score of writing subject.

Target variable:
* `math score`: score of math subject

Dataset Source Link :
[https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)

### It is observed that the categorical variables 'cut', 'color' and 'clarity' are ordinal in nature


# Screenshot of UI

![HomepageUI](/templates/Homepage.png)

# Approach for the project 

1. Data Ingestion : 
    * In Data Ingestion phase the data is first read as csv. 
    * Then the data is split into training and testing and saved as csv file.

2. Data Transformation : 
    * In this phase a ColumnTransformer Pipeline is created.
    * for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
    * for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
    * This preprocessor is saved as pickle file.

3. Model Training : 
    * In this phase base model is tested . The best model found was Linear Regression	.
    * After this hyperparameter tuning is performed.
    * This model is saved as pickle file.

4. Prediction Pipeline : 
    * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation : 
    * Flask app is created with User Interface to predict the gemstone prices inside a Web Application.

# Exploratory Data Analysis Notebook

Link : [EDA Notebook](/Notebook/EDA%20STUDENT%20PERFORMANCE.ipynb)

# Model Training Approach Notebook

Link : [Model Training Notebook](/Notebook/MODEL%20TRAINING.ipynb)
