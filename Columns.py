import streamlit as st


col1, col2, col3 = st.columns(3,gap='medium',vertical_alignment='bottom')

with col1:
    col1.text('Col1')
with col2:
    col2.text('Col2')
with (col3):
    col3.text('Col3')