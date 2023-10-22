import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
# from app import app

variant_options = [
    {"label": "Вариант из файла от компании 'БА'", "value": "ba_file"},
    {"label": "Вариант из файла Excel", "value": "excel_file"},
    {"label": "Вариант на основе ручного ввода атрибутов", "value": "manual_input"}
]

layout_pe = dbc.Container([
    html.H1("Оценка стоимости товара на основе истории продаж"),
    dcc.RadioItems(
        id="variant_selection",
        options=variant_options,
        value="ba_file",
        labelStyle={'display': 'inline-block', 'margin-right': '10px'}
    ),
    # html.Div(id="variant_options"),
    # остальной код компонентов и колбеков для этой страницы
])

# @app.callback(
#     Output("variant_components", "children"),
#     Input("variant_selection", "value")
# )
def update_variant_components(variant):
    if variant == "ba_file":
        return [
            # Компоненты для варианта из файла от компании "БА"
        ]
    elif variant == "excel_file":
        return [
            # Компоненты для варианта из файла Excel
        ]
    else:  # variant == "manual_input"
        return [
            # Компоненты для варианта на основе ручного ввода атрибутов
        ]