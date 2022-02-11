

from urllib.parse import urlencode
from geopy.geocoders import Nominatim

import plotly.graph_objects as go


def latitu(lugar):
    geolocator = Nominatim(user_agent="sinatxe")
    location = geolocator.geocode(lugar)
    return location.latitude

def longi(lugar):
    geolocator = Nominatim(user_agent="sinatxe")
    location = geolocator.geocode(lugar)
    return location.longitude





def config_map(locations,locationmode,z,colorscale,colorbar_title):
    """
    Esta función genera el mapa base y establece los valores para configurar.
    Args: locations: columna de lugares en mi df (columna df)
          locationmode( enumerated : ("ISO-3" | "USA-states" | "country names" ))
          z: qué estoy representando en el mapa (columna df)
          text:columna de lugares en mi df (columna df)
          paleta de colores('viridis','magma', etc.)
          colorbar_title: Título de leyenda de la escala de colores. (string)
    Return: fig (configuración mapa)
    """
    fig = go.Figure(go.Choropleth(
        locations = locations,
        locationmode = locationmode,
        z = z,
        text = locations,
        colorscale = colorscale,
        autocolorscale=False,
        reversescale=True,
        marker_line_color='#efefef',
        marker_line_width=0.5,
        colorbar_ticksuffix = '%',
        colorbar_title = colorbar_title,
        ))
    
    return fig

def customizar_map(locations,locationmode,z,colorscale,colorbar_title,tittle,scope):
    """
    Esta función establece las características del título y la apariencia del mapa base.
    Args: argumentos de la función "config_map".
          tittle: Título del mapa.
          scope:'world', 'usa', 'europe', 'asia', 'africa', 'north america', 'south america' (string).
    Return: mapa.
    """
    fig=config_map(locations,locationmode,z,colorscale,colorbar_title)
    fig.update_layout(
        title_text = tittle,
        showlegend = False,
        geo = dict(
            scope=scope,
            resolution=50,
            projection_type='miller',
            showcoastlines=True,
            showocean=True,
            showcountries=True,
            oceancolor='#eaeaea',
            lakecolor='#eaeaea',
            coastlinecolor='#dadada'
        )
    )

    return fig.show()