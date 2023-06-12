# StreamlitApp
Streamlit Application

This project is a Streamlit app that allows you to upload a CSV file, analyze its contents, and perform various statistical operations on the dataset. After uploading a CSV file, the app displays relevant statistics such as the number of rows, columns, and counts of categorical, numerical, and boolean variables. You can select a single column from the dataset using an input widget. If the selected column is numerical, a table presents the five-number summary, and a customized distribution plot is created using matplotlib and seaborn. For categorical columns, a table shows the proportions of each category level, and a customized bar plot visualizes the data.

Instructions:
1> Clone the repository
2> Install the packages listed in requirements.txt
3> Run the app using `streamlit run csv_analyzer.py`
4> Upload CSV
5> Change the different paramters in the webapp
