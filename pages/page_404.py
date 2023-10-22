import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Ошибка 404 - такой страницы не существует", className="display-3"),
            html.P(
                "Use Containers to create a jumbotron to call attention to "
                "featured content or information.",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Use utility classes for typography and spacing to suit the "
                "larger container."
            ),
            html.P(
                dbc.Button("Вернуться на главную страницу", href="/auction-selection", color="primary"), className="lead"
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)

