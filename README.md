# Student Academic Performance Prediction for CGPA

![GitHub repo size](https://img.shields.io/github/repo-size/your-username/student-academic-performance-prediction)
![GitHub stars](https://img.shields.io/github/stars/your-username/student-academic-performance-prediction?style=social)
![GitHub forks](https://img.shields.io/github/forks/your-username/student-academic-performance-prediction?style=social)
![GitHub](https://img.shields.io/github/license/your-username/student-academic-performance-prediction)

This repository contains a machine learning project that aims to predict a student's academic performance based on various factors to estimate their Cumulative Grade Point Average (CGPA). The project utilizes data analysis, feature engineering, and machine learning techniques to build an accurate predictive model.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Methods Used](#methods-used)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Predicting a student's academic performance is an essential task in the education system. This project aims to leverage machine learning techniques to predict a student's CGPA using various input features of courses of the semester scores. By predicting a student's CGPA, educators and academic advisors can identify students at risk of underperforming and provide timely interventions and support.

## Dataset
The dataset used for this project consists of historical student data, including features of previous semester scores. The dataset is not included in this repository, but you can find a similar dataset at: Pending: [example-dataset-link](https://example.com/dataset).

## Installation
To use the code in this repository, follow these steps:
1. Clone the repository: `git clone https://github.com/your-username/student-academic-performance-prediction.git`
2. Navigate to the project directory: `cd student-academic-performance-prediction`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage
1. Ensure you have installed the required dependencies.
2. Prepare your dataset in the appropriate format and save it in the project directory.
3. Modify the code to load and preprocess your dataset.
4. Run the main script: `python predict_cgpa.py`
5. View the predicted CGPA results.

## Methods Used
The following methods and techniques are employed in this project:
- Data preprocessing and cleaning
- Feature engineering
- Exploratory data analysis
- Machine learning algorithms (e.g., regression, ensemble methods)
- Model evaluation and validation

## Technologies
The project is implemented in Python and utilizes the following libraries:
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Computer Science Student Performance Predictor Streamlit App Deployment

This section is for the Streamlit application interface. 

### Overview

- The necessary libraries (`pickle`, `pandas`, `numpy`, `streamlit`, `sklearn`) are imported.
- The Extra Trees Regressor model (`ETR`) is loaded from the saved pickle file.
- The Streamlit application is defined within the `main()` function.
- The user interface is created using Streamlit's input components (`st.number_input`) to capture the scores for different courses.
- Upon clicking the "Click to Predict" button, the model predicts the student's performance based on the inputted scores.
- The predicted result is displayed along with a corresponding performance category (e.g., First Class, Second Class Upper, Second Class Lower, Third Class).

### Usage

To run the application, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Execute the `main()` function using `streamlit run <filename>.py` in your terminal, where `<filename>.py` corresponds to the filename containing the provided code.
3. Access the application through the provided local URL.

### Sample Data

The code assumes that the inputted course scores are provided for the following levels and courses:

- 100 Level Courses: BIO 101, CHM 101, GST 101, GST 103, GST 203, MTH 101, PHY 101, STA 101, CSC 102, MTH 102, CSC 104, PHY 102, CHM 102, GST 102, STA 112
- 200 Level Courses: CSC 201, CSC 203, CSC 205, GST 201, GST 301, MTH 245, STA 203, CSC 202, CSC 204, CSC 206, CSC 208, PHY 202, MTH 214, GST 204, GST 206

## License
This project is licensed under the [MIT License](LICENSE).
