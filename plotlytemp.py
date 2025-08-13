import pandas as pd
import plotly.express as px


df = pd.read_csv('data/iris.csv')

print(df)

plot = px.scatter(data_frame=df,
                  x='petal_length',
                  size='sepal_width',
                  y='petal_width',
                  color='species',
                  title='petal vs sepal length',
                  template='plotly_dark'
                  )

plot.show()

