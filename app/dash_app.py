import dash_core_components as dcc
import dash_html_components as html
from .flask_app import dash_app

layout = html.Div([
    html.H1("Функционал в разработке")
])

dash_app.layout = layout
