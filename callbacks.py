import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app

# Колбек для переключения между экранами
@app.callback(
    [
        Output("welcome-screen", "style"),
        Output("auction-selection-layout", "style"),
        Output("price-estimation-layout", "style"),
    ],
    [
        Input("auction-selection-button", "n_clicks"),
        Input("price-estimation-button", "n_clicks"),
    ],
)
def switch_screen(auction_clicks, price_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return {"display": "block"}, {"display": "none"}, {"display": "none"}
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "auction-selection-button":
        return {"display": "none"}, {"display": "block"}, {"display": "none"}
    elif button_id == "price-estimation-button":
        return {"display": "none"}, {"display": "none"}, {"display": "block"}

# Другие колбеки будут добавлены по мере разработки
