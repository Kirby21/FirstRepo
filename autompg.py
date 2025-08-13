import pandas as pd
import streamlit as st
import plotly.express as px
from numpy.ma.extras import unique

st.set_page_config(layout='wide')

df = pd.read_csv('data/clean_auto_mpg.csv')

st.markdown('### AUTO MPG Tabulated Dashboard')
unique_origin = list(df['origin'].unique())
unique_origin.sort()

unique_origin_str = ['Origin: ' + str(origin) for origin in unique_origin]
print(unique_origin_str)

tab1, tab2, tab3 = st.tabs([unique_origin_str[0],
                           unique_origin_str[1],
                           unique_origin_str[2]])

with tab1:
    st.subheader('Origin1')
    df1 = df[df['origin'] == 1]
    col1,col2,col3,col4 = st.columns(4)
    col1.metric(label='Avg MPG',value=round(df1['mpg'].mean(),1))
    col2.metric(label='Avg Displacement',value=round(df1['displacement'].mean(),1))
    col3.metric(label='Avg Horsepower', value=round(df1['horsepower'].mean(), 1))
    col4.metric(label='Avg Weight', value=round(df1['weight'].mean(), 1))


    col5,col6 = st.columns([3,1])
    with col5:
        st.plotly_chart(px.scatter(data_frame=df1,
                                   x='weight',
                                   y='horsepower',
                                   size='displacement',
                                   color='cylinders',
                                   title='Weight vs HP for cars from '.format(unique_origin_str[0])))
    with col6:
        st.plotly_chart(px.histogram(data_frame=df1,
                                     x='mpg',
                                     title='MPG distribution'))
with tab2:
    st.subheader('Origin2')
    df2 = df[df['origin'] == 2]
    col1,col2,col3,col4 = st.columns(4)
    col1.metric(label='Avg MPG',value=round(df2['mpg'].mean(),1))
    col2.metric(label='Avg Displacement',value=round(df2['displacement'].mean(),1))
    col3.metric(label='Avg Horsepower', value=round(df2['horsepower'].mean(), 1))
    col4.metric(label='Avg Weight', value=round(df2['weight'].mean(), 1))


    col5,col6 = st.columns([3,1])
    with col5:
        st.plotly_chart(px.scatter(data_frame=df2,
                                   x='weight',
                                   y='horsepower',
                                   size='displacement',
                                   color='cylinders',
                                   title='Weight vs HP for cars from '.format(unique_origin_str[1])))
    with col6:
        st.plotly_chart(px.histogram(data_frame=df2,
                                     x='mpg',
                                     title='MPG distribution'))
with tab3:
    st.subheader('Origin2')
    df3 = df[df['origin'] == 3]
    col1,col2,col3,col4 = st.columns(4)
    col1.metric(label='Avg MPG',value=round(df3['mpg'].mean(),1))
    col2.metric(label='Avg Displacement',value=round(df3['displacement'].mean(),1))
    col3.metric(label='Avg Horsepower', value=round(df3['horsepower'].mean(), 1))
    col4.metric(label='Avg Weight', value=round(df3['weight'].mean(), 1))


    col5,col6 = st.columns([3,1])
    with col5:
        st.plotly_chart(px.scatter(data_frame=df3,
                                   x='weight',
                                   y='horsepower',
                                   size='displacement',
                                   color='cylinders',
                                   title='Weight vs HP for cars from '.format(unique_origin_str[2])))
    with col6:
        st.plotly_chart(px.histogram(data_frame=df3,
                                     x='mpg',
                                     title='MPG distribution'))