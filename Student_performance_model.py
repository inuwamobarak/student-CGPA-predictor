'''

* The necessary libraries (pickle, pandas, numpy, streamlit, sklearn) are imported.

* The Extra Trees Regressor model (ETR) is loaded from the saved pickle file.

* The Streamlit application is defined within the main() function.

* The user interface is created using Streamlit's input components (st.number_input) to capture the scores for different courses.
Upon clicking the "Click to Predict" button, the model predicts the student's performance based on the inputted scores.

* The predicted result is displayed along with a corresponding performance category (e.g., First Class, Second Class Upper, Second Class Lower, Third Class).

* To run the Streamlit application, you need to execute the main() function using streamlit run <filename>.py in your terminal, where <filename>.py corresponds to the filename containing the provided code.

'''

# Importing Dependencies
import pickle
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.ensemble import ExtraTreesRegressor

# Load the Extra Trees Regressor model from the pickle file
with open('Student_performance_model.pickle','rb') as f:
    ETR = pickle.load(f)

def main():
    st.title('Computer Science Student Performance Predictor')
    st.subheader('(Please fill in your 100 level and 200 level courses.)')
    
    # Input fields for 100 level courses
    BIO101 = st.number_input('BIO 101')
    CHM101 = st.number_input('CHM 101')
    GST101 = st.number_input('GST 101')
    GST103 = st.number_input('GST 103')
    GST203 = st.number_input('GST 203')
    MTH101 = st.number_input('MTH 101')
    PHY101 = st.number_input('PHY 101')
    STA101 = st.number_input('STA 101')
    CSC102 = st.number_input('CSC 102')
    MTH102 = st.number_input('MTH 102')
    CSC104 = st.number_input('CSC 104')
    PHY102 = st.number_input('PHY 102')
    CHM102 = st.number_input('CHM 102')
    GST102 = st.number_input('GST 102')
    STA112 = st.number_input('STA 112')

    # Input fields for 200 level courses
    CSC201 = st.number_input('CSC 201')
    CSC203 = st.number_input('CSC 203')
    CSC205 = st.number_input('CSC 205')
    GST201 = st.number_input('GST 201')
    GST301 = st.number_input('GST 301')
    MTH245 = st.number_input('MTH 245')
    STA203 = st.number_input('STA 203')
    CSC202 = st.number_input('CSC 202')
    CSC204 = st.number_input('CSC 204')
    CSC206 = st.number_input('CSC 206')
    CSC208 = st.number_input('CSC 208')
    PHY202 = st.number_input('PHY 202')
    MTH214 = st.number_input('MTH 214')
    GST204 = st.number_input('GST 204')
    GST206 = st.number_input('GST 206')
    
    if st.button('Click to Predict'):
        # Perform prediction using the Extra Trees Regressor model
        result = ETR.predict([[BIO101,CHM101,GST101,GST103,GST203,MTH101,PHY101,STA101,CSC102,MTH102,CSC104,PHY102,CHM102,GST102,STA112,CSC201,CSC203,CSC205,GST201,GST301,MTH245,STA203,CSC202,CSC204,CSC206,CSC208,PHY202,MTH214,GST204,GST206]])
        
        # Display the predicted result and performance category
        if result > 4.49:
            st.success(result)
            st.success('First Class')
        elif result >= 3.50 and result < 4.49:
            st.success(result)
            st.success('Second Class Upper')
        elif result >= 2.40 and result < 3.50:
            st.warning(result)
            st.success('Second Class Lower')
        else:
            st.warning(result)
            st.warning('Third Class')
            

if __name__=='__main__':
    main()

