import pandas as pd
import streamlit as st
import plotly.express as px


Tab1, Tab2, Tab3, Tab4, Tab5 = st.tabs(['Tab1','Tab2','Tab3','Tab4','Tab5'])

with Tab1:
    st.header('Per Brand')
with Tab2:
    st.header('Per Area')
with Tab3:
    st.header('Per Channel')
with Tab4:
    st.header('Per Sales Person')
with Tab5:
    st.header('Per Category')