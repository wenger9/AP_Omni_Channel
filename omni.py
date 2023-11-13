# import streamlit as st
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.decomposition import PCA
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt

# # Set page config
# st.set_page_config(page_title="Sales Data Analysis", page_icon=":bar_chart:", layout="wide")

# # Title
# st.title("Sales Data Analysis App")

# # Introduction
# st.write("""
# This app analyzes sales transactions, consumer data, and retailer data.
# """)

# # Sidebar - Collects user input features into dataframe
# with st.sidebar.header('1. Upload your CSV data'):
#     uploaded_files = st.sidebar.file_uploader("Upload your input CSV files", type=["csv"], accept_multiple_files=True)

# # Sidebar - Specify parameter settings
# # You can add any parameter settings here that are relevant to your analysis

# # Main panel
# st.header('Uploaded Data')

# if uploaded_files is not None:
#     for uploaded_file in uploaded_files:
#         df = pd.read_csv(uploaded_file)
#         st.write(f"Data from: {uploaded_file.name}")
#         st.dataframe(df)
#         # Here, you can add specific processing for each file
#         # For example, if you want to build models or perform EDA for each file:
#         # build_model(df) or perform_eda(df)
# else:
#     st.info('Awaiting for CSV files to be uploaded.')
#     # You can add a button to load example datasets if you have them


# # Footer
# st.write("""
# Note: The ML model used in this app is for demo purposes only and should not be used for prescriptive insights.
# """)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Sales Data Analysis", page_icon=":bar_chart:", layout="wide")

# Title
st.title("Sales Data Analysis App")

# Introduction
st.write("""
This app analyzes sales transactions, consumer data, and retailer data.
""")

# Sidebar - Collects user input features into dataframe
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

# Sidebar - Specify parameter settings
# You can add any parameter settings here that are relevant to your analysis

# Main panel
st.header('Uploaded Data')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(f"Data from: {uploaded_file.name}")
    st.dataframe(df)

    # Visualization
    st.header('Data Visualizations')

    # Setting up columns for side-by-side visualizations
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Total Sales by Category")
        # Replace 'Category' and 'TotalSales' with your actual column names
        sns.barplot(x=df['Category'], y=df['TotalSales'])
        plt.xticks(rotation=45)
        st.pyplot(plt)

    with col2:
        st.subheader("Budget Distribution by Channel")
        # Replace 'Channel' and 'Budget' with your actual column names
        sns.boxplot(x=df['Channel'], y=df['Budget'])
        plt.xticks(rotation=45)
        st.pyplot(plt)

    # Add more visualizations as needed

else:
    st.info('Awaiting for CSV file to be uploaded.')

# Footer
st.write("""
Note: The ML model used in this app is for demo purposes only and should not be used for prescriptive insights.
""")
