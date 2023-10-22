import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

header = dbc.Navbar(
    [
        dbc.Col(html.H2("ESO Data Portal"), width="auto"),
        dbc.ButtonGroup(
            [
                dbc.Button("Подбор на аукцион", id="auction-selection-button", n_clicks=0),
                dbc.Button("Оценка стоимости алмазов", id="price-estimation-button", n_clicks=0),
            ],
            className="ml-auto",
            size="lg",
        ),
    ],
    color="#007bc2",
    dark=True,
    sticky="top",
)

welcome_screen = html.Div(
    [
        html.H1("Добро пожаловать на портал!"),
        html.P("Здесь вы можете подобрать товары со склада на аукцион и оценить стоимость товара на основе истории продаж."),
    ],
    id="welcome-screen",
    style={"text-align": "center"},
)

auction_selection_layout = html.Div(
    [
        # Здесь будет размещен макет для подбора товаров со склада на аукцион
    ],
    id="auction-selection-layout",
    style={"display": "none"},
)

price_estimation_layout = html.Div(
    [
        # Здесь будет размещен макет для оценки стоимости товара на основе истории продаж
    ],
    id="price-estimation-layout",
    style={"display": "none"},
)

layout = dbc.Container(
    [
        header,
        html.Br(),
        welcome_screen,
        auction_selection_layout,
        price_estimation_layout,
    ],
    fluid=True,
)
