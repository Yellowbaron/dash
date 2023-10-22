import pandas as pd
import base64
import io
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from auction import auction_form, sidebar, main_content2
from layout import layout
from components.header import header
from dash import dcc, ctx, no_update
# import price_estimator
from price_estimator import layout_pe
from dash.dependencies import Input, Output, State
from components.excel_upload_button import upload_button
from pages.page_404 import jumbotron
from algorithms import stratification_warehouse
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Мы будем добавлять камни построчно поэтому это список
# Всегда дешевле добавить к списку и создать DataFrame за один раз, чем создавать пустой DataFrame (или один из NaN) и добавлять к нему снова и снова.
#
# Списки также занимают меньше памяти и представляют собой гораздо более легкую структуру данных для работы , добавления и удаления (при необходимости).
#
# dtypes автоматически выводятся (вместо того, чтобы присваиваться object им всем).
#
# A RangeIndex автоматически создается для ваших данных , и вам не нужно заботиться о присвоении правильного индекса строке, которую вы добавляете на каждой итерации.
auction_df = []
CONTENT_STYLE = {
    "margin-left": "0rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Download(id="download"),
    # header,
    dbc.Container([
        dbc.Container(id="main-content", style=CONTENT_STYLE)
    ], className="text-center")
])

server = app.server


# Создайте колбек для кнопки подбора товаров со склада на аукцион
# @app.callback(
#     Output("main-content", "children"),
#     [Input("auction-selection-button", "n_clicks"),
#      Input("price-estimation-button", "n_clicks")],
#     [dash.dependencies.State("main-content", "children")],
# )
# Определите обратные вызовы для обновления страницы
@app.callback(Output('main-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/auction-selection':
        return [sidebar, main_content2]
    elif pathname == '/price-estimation':
        return layout_pe
    else:
        return jumbotron

# Загрузка файла Excel и сохранение его в датафрейм
@app.callback(
    Output("table", "rowData"),  # Обновить данные в DataTable
    Output("table", "columnDefs"),  # Обновить название колонок в DataTable
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
)
def upload_file(contents, filename):

    if ctx.triggered_id == "upload-data":
        content_type, content_string = contents.split(",")
        decoded = base64.b64decode(content_string)
        try:
            if "xlsx" in filename:
                df = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            return html.Div(["Ошибка при загрузке файла: {}".format(e)])

        df['id'] = df.index
        rowData = df.to_dict('records')
        columnDefs = [{"field": i} for i in df.columns]
        columnDefs[0].update({"checkboxSelection": True})

        return rowData, columnDefs



# Колбэк для ручного управления в таблице
@app.callback(
    Output("table", "rowTransaction"),
    Input("warehouse-remove", "n_clicks"),
    Input("warehouse-update", "n_clicks"),
    State("table", "selectedRows"),
)
def update_rowdata(n1, n2, selection):
    if ctx.triggered_id == "warehouse-remove":
        print('1')
        if selection is None:
            print('2')
            return no_update
        return {"remove": selection}

    if ctx.triggered_id == "warehouse-update":
        if selection is None:
            return no_update
        for row in selection:
            auction_df.append(row)
        print(auction_df)
        return {"remove": selection}

# Колбэк для сбора аукциона
@app.callback(
    Output("download", "data"),
    Input("submit-button", "n_clicks"),
    State("table", "rowData"),
    State("table", "columnDefs"),
    State("lot-count", "value"),
    # State("stock-percentage", "value"),
    State("ba-percentage", "value")
)
def generate_reports(n_clicks, rowData, columnDefs, lots_count, ba):
    if n_clicks:
        dfOut = pd.DataFrame(rowData)
        print(lots_count)
        print(ba)
        print(auction_df)
        dfOut = pd.concat([pd.DataFrame(auction_df), stratification_warehouse(dfOut, lots_count - len(auction_df), ba)], ignore_index=True)

        # dfOut = stratification_warehouse(dfOut, lots_count - len(auction_df), ba)
        dfOut.to_excel("app/data/output.xlsx", index=False)
        return dcc.send_file("app/data/output.xlsx")


if __name__ == "__main__":
    app.run_server(debug=True)
