import pandas as pd
import plotly.express as px

df = pd.read_csv('data/us-cities-top-1k.csv')

print(df)

plot = px.scatter_mapbox(data_frame=df,
                  lat='lat',
                  lon='lon',
                  size='Population',
                  zoom=3,
                  title='Population of US cities',
                  mapbox_style='open-street-map'
                  )
plot.show()