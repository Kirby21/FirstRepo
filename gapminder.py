import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
st.markdown('### Gapminder Dashboard')
df = pd.read_csv('data/gapminder_data_graphs.csv')
years = df['year'].unique()

selected_year = st.selectbox(label='Select year:', options=years)


dfplot = df[df['year'] == selected_year]


avedfplot = dfplot.groupby(['country','continent']).mean().reset_index()

print(avedfplot.columns)

avegdp = round(avedfplot['gdp'].mean(),2)
avelifeex = round(avedfplot['life_exp'].mean(),2)
avehdi = round(avedfplot['hdi_index'].mean(),2)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label='Average GDP',value=avegdp)
with col2:
    st.metric(label='Average Life Expectancy',value=avelifeex)
with col3:
    st.metric(label='Average HDI', value=avehdi)

title = 'plot of GDP vs Life expectancy {}'.format(selected_year)
plot = px.scatter(data_frame=dfplot,
                  x='gdp',
                  y='life_exp',
                  color='country',
                  title=title,
                  )

st.plotly_chart(plot)

col4, col5= st.columns(2)
with col4:
    box1  = px.box(data_frame=dfplot, x='continent', y='gdp',title='Distribution of GDP across the different continents in'.format(selected_year))
    st.plotly_chart(box1)
with col5:
    hist1 = px.histogram(data_frame=dfplot, x='gdp',title='Distribution of GDP across the different continents in'.format(selected_year))
    st.plotly_chart(hist1)
col6, col7 = st.columns(2)
with col6:
    box2  = px.box(data_frame=dfplot, x='continent', y='hdi_index',title='Distribution of GDP across the different continents in'.format(selected_year))
    st.plotly_chart(box2)
with col7:
    hist2 = px.histogram(data_frame=dfplot, x='life_exp',title='Distribution of GDP across the different continents in'.format(selected_year))
    st.plotly_chart(hist2)