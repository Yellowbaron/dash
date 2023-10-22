import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

upload_button = dbc.Row(
    [
        dbc.Col(
            [
                dcc.Upload(
                    id="upload-data",
                    children=dbc.Button("Загрузить данные из Excel", id="upload-button", color="secondary"),
                    multiple=False,
                ),
                html.Div(id='output-data-upload')  # New Div for output data
            ],
            width={"size": 12},
        )
    ]
)
