import streamlit as st
import datetime


st.write('sliders')

basic_slider = st.slider(label='basic slider',
                         min_value=1,
                         max_value=100,
                         value=50)

st.write('selected number: {}'.format(basic_slider))

range_slider = st.slider(label='range slider',
                         min_value=1,
                         max_value=100,
                         value=(50,80))

st.write('selected number: {}'.format(range_slider))

float_slider = st.slider(label='decimal slider',
                         min_value=1.0,
                         max_value=5.0,
                         value=2.5)

st.write('selected number: {}'.format(float_slider))

date_slider = st.slider(label='date slider',
                         min_value=datetime.date(1990, 1, 1),
                         max_value=datetime.date.today(),
                         value=datetime.date.today(),
                         format='MM/DD/YYYY')


st.write('selected number: {}'.format(date_slider))
