import streamlit as st
from click import option

st.sidebar.subheader('Streamlit')

st.sidebar.selectbox(label='choose options:', options=['option1','option2','option3','option4'])