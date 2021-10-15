# from urllib.request import urlopen
# import json
# import plotly.graph_objects as go
# import geopandas as gpd
# import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.express as px
# fn = "fhszs1sn/fhszs06_3_1.shp"
# shapefile = gpd.read_file(fn)
# shapefile.plot()
# plt.show()
#
# shapefile['id'] = shapefile.index
# json_f = json.loads(shapefile.to_json())
#
# # df = pd.DataFrame(shapefile)
# #
# # fig = px.choropleth_mapbox(df, geojson=json_f, locations='id', color='HAZ_CODE',
# #                            color_continuous_scale="Viridis",
# #                            range_color=(min(df.HAZ_CODE), max(df.HAZ_CODE)),
# #                            mapbox_style="carto-positron",
# #                            zoom=5, center={"lat": 37, "lon": -119},
# #                            opacity=0.5,
# #                            labels={'HAZ_CODE': 'HAZ_CLASS'}
# #                           )
# # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# # fig.show()

########
# SAMPLE
########
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

import plotly.express as px

fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()