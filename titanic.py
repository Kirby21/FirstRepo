import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('Data/titanic_data.csv')

df['Embarked'] = df['Embarked'].fillna('unknown')

embarked = list(df['Embarked'].unique())
gender = list(df['sex'].unique())

col1, col2 = st.columns(2)

col1.selectbox(label='Select Port', options=embarked)
col2.selectbox(label='Select Gender', options=gender)