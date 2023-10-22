import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

upload_button_cadas = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Button("Загрузить данные из Cadas", id="cadas-button", color="secondary"),
            ],
            width={"size": 12},
            style={'padding': 8},
        )
    ]
)