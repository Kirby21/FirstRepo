from tkinter.ttk import Label

import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('data/iris.csv')
st.set_page_config(layout='wide')
st.markdown('### Iris Dashboard')

species = df['species'].unique()
col5,col6 = st.columns(2)
with col5:
    selected_species = st.selectbox(label='Select Species',label_visibility='collapsed', options=species)
with col6:
    check = st.checkbox(label='show')

filtered_df = df[df['species'] == selected_species]

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label='Sepal length Average',
              value=round(filtered_df['sepal_length'].mean(),2))
with col2:
    st.metric(label='Sepal width Average',value=round(filtered_df['sepal_width'].mean(),2))
with col3:
    st.metric(label='Petal length Average',value=round(filtered_df['petal_length'].mean(),2))
with col4:
    st.metric(label='Petal width Average',value=round(filtered_df['petal_width'].mean(),2))


colormap = {'setosa':'gray',
            'virginica':'gray',
            'versicolor':'gray',}

colormap[selected_species] = 'blue'
scatterplot = px.scatter(data_frame=df,
                         color_discrete_map=colormap,
                         x='sepal_length',
                         y='petal_width',
                         color='species',
                         size='petal_length',
                         title='sepal_length vs petal_width for ' + selected_species)

st.plotly_chart(scatterplot)

if check :
    col7, col8, col9, col10 = st.columns(4)

    def create_histogram(x,title):

        hist = px.histogram(data_frame=filtered_df,
                            color_discrete_map=colormap,
                            x=x,
                            title=title,)

        return hist
    hist1 = create_histogram(filtered_df['sepal_length'],'distribution of sepal length')
    hist2 = create_histogram(filtered_df['sepal_width'],'distribution of sepal width')
    hist3 = create_histogram(filtered_df['petal_length'],'distribution of petal length')
    hist4 = create_histogram(filtered_df['petal_width'],'distribution of petal width')
    col7.plotly_chart(hist1)
    col8.plotly_chart(hist2)
    col9.plotly_chart(hist3)
    col10.plotly_chart(hist4)