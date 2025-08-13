import pandas as pd
import plotly.express as px


df = pd.read_csv('data/tips.csv')

print(df)

plot = px.pie(data_frame=df,
              values='tip',
              names='sex',
              hole=0.5,
              title='Pie',
              facet_col='day')

plot.show()
