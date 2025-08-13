import pandas as pd
import plotly.express as px

df = pd.read_csv('data/iris.csv')
print(df)

dfmean = df.groupby(['species']).mean().reset_index()
print(dfmean)

plot = px.bar(data_frame=dfmean,
              x='species',
              y='petal_width',
              color='species',
              title='petal width average')


plot.show()