import dash_bootstrap_components as dbc
import dash_core_components as dcc
from components.excel_upload_button import upload_button
from components.cadas_data_loader import upload_button_cadas
import dash_html_components as html
import dash_table
import dash_ag_grid as dag

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "height": '100%'
}
CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Создайте форму для ввода параметров аукциона
auction_form = dbc.Form(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Алгоритм подбора товаров:", html_for="algorithm-selection"),
                        dcc.Dropdown(
                            id="algorithm-selection",
                            options=[
                                {"label": "Стратификация состава склада", "value": "algo1"},
                                # {"label": "Подбор по торговым ЗТК", "value": "algo2"},
                                # {"label": "Подбор для конкуренции", "value": "algo3"},
                                # {"label": "Накопление статистики", "value": "algo4"},
                                # {"label": "Многорукий бандит", "value": "algo5 "},
                                # Добавьте другие алгоритмы, если требуется
                            ],
                            placeholder="Выберите алгоритм",
                        ),
                    ],
                    width={"size": "auto"},
                ),
            ],
            justify="center",
            className='mb-3'
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Количество лотов:", html_for="lot-count"),
                        dbc.Input(id="lot-count", type="number", placeholder="Введите количество лотов", style={"textAlign": "center"}),
                    ],
                    width={"size": "auto"},
                ),
            ],
            justify="center",
            className='mb-3'
        ),

        # TODO: Сначала нужно придумать как внедрить в текущий алгоритм регулирование процента стока

        # dbc.Row(
        #     [
        #         dbc.Col(
        #             [
        #                 dbc.Label("Процент Stock:", html_for="stock-percentage"),
        #                 dbc.Input(id="stock-percentage", type="number", placeholder="Введите процент Stock", style={"textAlign": "center"}),
        #             ],
        #             width={"size": "auto"},
        #         ),
        #     ],
        #     justify="center",
        #     className='mb-3'
        # ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Процент BA:", html_for="ba-percentage"),
                        dbc.Input(id="ba-percentage", type="number", placeholder="Введите процент BA", style={"textAlign": "center"}),
                    ],
                    width={"size": "auto"},
                ),
            ],
            justify="center",
            className='mb-3'
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Button("Запустить алгоритм", id="submit-button", color="primary", type="submit"),
                    width={"size": 12},
                )
            ],
            justify="center",
            className='mb-3'
        ),
    ]
)

# Боковая панель
sidebar = dbc.Container(
    [
        dbc.Label("Источник данных:"),
        # html.Div([
        #     dbc.RadioItems(
        #         id="data-source",
        #         options=[
        #             {"label": "Из CADAS", "value": "cadas"},
        #             {"label": "Из Excel", "value": "excel"},
        #         ],
        #         inline=True,
        #     ),
        #html.Div(id='source-container'),
        #]),
        html.Hr(),
        upload_button_cadas,
        upload_button,
        html.Hr(),
        auction_form
    ],
    fluid=True,
    className="sidebar",
    style=SIDEBAR_STYLE
)

# Основное содержимое в виде таблицы
main_content2 = dbc.Container(
    [
        html.Div(id="selections-multiple-output"),
        html.Div(
            [
                dbc.Button("Добавить выбранные камни в аукцион", id="warehouse-update", color="primary", className="me-1"),
                dbc.Button("Исключить выбранные камни из подбора", id="warehouse-remove", color="danger", className="me-1"),
            ],
            className="mb-3"  # margin-bottom for spacing
        ),
        dag.AgGrid(
            id='table',
            defaultColDef={"flex": 1, "filter": True},
            dashGridOptions={"rowSelection":"multiple"},
            getRowId="params.data.id"
        ),
    ],
    fluid=True,
    className="main-content",
    style=CONTENT_STYLE
)
