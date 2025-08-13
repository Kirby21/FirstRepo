import pandas as pd
import plotly.express as px

df = pd.read_csv('data/iris.csv')


plot = px.histogram(data_frame=df,
                    x='sepal_length',
                    color='species',
                    facet_col='species',
                    title='Sepal Length Histogram',)
plot.show()