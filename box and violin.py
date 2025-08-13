import pandas as pd
import plotly.express as px

df = pd.read_csv('data/iris.csv')
print(df)


plot = px.box(data_frame=df,
              x='species',
              y='petal_width',
              title='petal width box',
              color='species',
              )

plot.show()

plot2 = px.violin(data_frame=df,
              x='species',
              y='petal_width',
              title='petal width box',
              color='species',
              )

plot2.show()