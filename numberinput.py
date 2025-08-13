import streamlit as st


number_input = st.number_input(
    label='Enter a number',
    min_value=0,
    max_value=100,
    value=0,
    step=5,
    help='Enter a number'

)

sbnumber = st.sidebar.number_input(
    label='Enter a number',
    min_value=0,
    max_value=100,
    value=0,
    step=5,
    help='Enter a number'
)

st.write(sbnumber)