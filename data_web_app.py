# Data Analysis Web Application

# import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

# 1. Title and Subheader
st.title("Data Analysis Web Application")
st.subheader("Perform preliminary data analysis in a few minutes")

# 2. Upload Dataset
upload = st.file_uploader("Upload Your Dataset (in CSV format)")

if upload is not None:
    data = pd.read_csv(upload)
    
# 3. Data Preview Option
if upload is not None:
    if st.checkbox("Click here to preview your dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            
# 4. Check Datatype of Each Column
if upload is not None:
    if st.checkbox("Click here if you want to view datatype of columns"):
        st.text("Datatypes are as followings:")
        dtypes_df = pd.DataFrame(data.dtypes).reset_index()
        dtypes_df.columns = ['Column Name', 'Data Type']
        st.dataframe(dtypes_df.astype(str))
        
# 5. Shape of Dataset
if upload is not None:
    dataset_shape = st.radio("Which dimension would you like to check?", ('Rows','Columns'))
    
    if dataset_shape == 'Rows':
        st.text("Number of rows")
        st.write(data.shape[0])
    if dataset_shape == 'Columns':
        st.text("Number of columns")
        st.write(data.shape[1])
        
# 6. Find null values in dataset
if upload is not None:
    null_check = data.isnull().values.any()
    if null_check == True:
        if st.checkbox("Null values in the dataset, click the checkbox to see heatmap"):
            st.set_option('deprecation.showPyplotGlobalUse', False) # to disable the notification that pops up when running heatmap codeline
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("No missing  value in your dataset!")
    
            
# 7. Find duplicates
if upload is not None:
    null_check = data.duplicated().any()
    if null_check == True:
        st.warning("Your dataset contains some duplicate values")
        dup = st.selectbox("Do you want to remove duplicates?",
                           ("Select one","Yes","No"))
        
        if dup == "Yes":
            data=data.drop_duplicates()
            st.text("Duplicates are removed")
        if dup == "No":
            st.text("Duplicates will be kept")
    else:
        st.success("Your dataset has NO duplicates!")

# 8. Get Overall Statistics
if upload is not None:
    if st.checkbox("Click to get dataset summary"):
        st.write(data.describe(include=[np.number]))
        
        
# 9. About App Section
if st.button("How This App Built?"):
    st.text("Built via Streamlit library of Python")
    st.text("Prepared by Türkan Aliyeva")
    
    
