import pandas as pd
import plotly.express as px
import streamlit as st

st.header('drop down')

spells = ['hex','quas','wex']

selected_spell = st.selectbox(label='select spell',
                              options=spells,
                              key='u1')
