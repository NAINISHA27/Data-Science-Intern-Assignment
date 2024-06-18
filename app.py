import streamlit as st
import pandas as pd

st.title("Tasks Output Representation")

# Task 1 - Read Jupyter Notebook file
st.header("Task 1 Output")
with open("C:/Users/naini/OneDrive/Desktop/INTERSHIP/first output.ipynb", "r") as file:
    nb_content = file.read()
st.code(nb_content, language="python")

# Task 2 - Read CSV files
st.header("Task 2 Output")

# Read the CSV files for Task 2
rf_clf_predictions = pd.read_csv("C:/Users/naini/OneDrive/Desktop/INTERSHIP/rf_clf_predictions.csv")
log_reg_predictions = pd.read_csv("C:/Users/naini/OneDrive/Desktop/INTERSHIP/log_reg_predictions.csv")

# Display the data for Task 2
st.subheader("Random Forest Classifier Predictions")
st.write(rf_clf_predictions)

st.subheader("Logistic Regression Predictions")
st.write(log_reg_predictions)

# Task 3 - Read Excel file
st.header("Task 3 Output")
output_summary = pd.read_excel("C:/Users/naini/OneDrive/Desktop/INTERSHIP/output_summary.xlsx", engine='openpyxl')
st.write(output_summary)
