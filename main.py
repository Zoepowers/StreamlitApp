import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


st.write("""Streamlit Application

This project is a Streamlit app that allows you to upload a CSV file, analyze its contents, and perform various statistical operations on the dataset. After uploading a CSV file, the app displays relevant statistics such as the number of rows, columns, and counts of categorical, numerical, and boolean variables. You can select a single column from the dataset using an input widget. If the selected column is numerical, a table presents the five-number summary, and a customized distribution plot is created using matplotlib and seaborn. For categorical columns, a table shows the proportions of each category level, and a customized bar plot visualizes the data.""")


st.write("Instructions:")
st.write("1> Clone the repository")
st.write("2> Install the packages listed in requirements.txt")
st.write("3> Run the app using streamlit run csv_analyzer.py")
st.write("4> Upload CSV 5> Change the different paramters in the webapp")


uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    rows = df.shape[0]
    columns = df.shape[1]
    cat = df.select_dtypes(include=['object']).shape[1]
    num = df.select_dtypes(include=['float', 'int']).shape[1]
    bool = df.select_dtypes(include=['bool']).shape[1]
    st.write("Number of rows:", rows)
    st.write("Number of columns:", columns)
    st.write("Number of categorical variables:", cat)
    st.write("Number of numerical variables:", num)
    st.write("Number of boolean variables:", bool)

    show_df = st.checkbox("Show Data Frame", key="disabled")
    
    if show_df:
      st.write(df)

    column = st.selectbox("Select a column", df.columns)

    if column is not None:
        if column is not None:
            st.write("Selected column:", column)

            if column in df.select_dtypes(include=['float', 'int']).columns:
                st.write("Five-Number Summary:")
                st.table(df[column].describe()[['min', '25%', '50%', '75%', 'max']])
                st.write("Distribution plot:")
                fig, ax = plt.subplots()
                sns.histplot(df[column], kde=True, ax=ax)
                ax.set_xlabel(column)
                ax.set_ylabel('Occurrence')
                st.pyplot(fig)
            elif column in df.select_dtypes(include=['object']).columns:
                st.write("Proportions of each category:")
                proportion = df[column].value_counts(normalize=True)
                st.table(proportion)
                st.write("Bar plot:")
                fig, ax = plt.subplots()
                sns.countplot(x=column, data=df, ax=ax)
                ax.set_xlabel(column)
                ax.set_ylabel('Total')
                st.pyplot(fig)

