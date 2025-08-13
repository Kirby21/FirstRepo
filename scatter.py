import pandas as pd
import plotly.express as px


df = pd.read_csv('data/iris.csv')
print(df)


plot = px.scatter(data_frame=df,
                  x='sepal_length',
                  # size='sepal_width',
                  color='species',
                  facet_col='species',
                  y='petal_width',
                  title='Sepal Length vs. Petal Width')

plot.show()