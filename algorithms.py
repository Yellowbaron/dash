import pandas as pd
import numpy as np

# TO-DO доработать как отдельный вызов
def algorithm1(Warehouse, auction_size, ba_percentage, stock_percentage):
    # Стратификация склада
    # Определить количество каждой позиции на складе
    WarehouseSize = Warehouse.groupby(['form', 'color', 'quality', 'ownership', 'flu'], as_index=False,
                                      dropna=False).size()
    Warehouse = pd.merge(Warehouse, WarehouseSize, on=['form', 'color', 'quality', 'ownership', 'flu'], how='left')

    # Выбрать элементы с BA=True и stock=False в зависимости от заданных процентов от размера аукциона
    ba_items = Warehouse[(Warehouse["BA"] == True) & (Warehouse["stock"] == False)].sample(
        n=int(auction_size * ba_percentage), random_state=42)

    # Выбрать элементы с stock=True в зависимости от заданных процентов от размера аукциона
    stock_items = Warehouse[Warehouse["stock"] == True].sample(n=int(auction_size * stock_percentage), random_state=42)

    # Объединить выбранные элементы и удалить дубликаты
    selected_items = pd.concat([ba_items, stock_items]).drop_duplicates()

    # Определить количество каждой позиции на складе в разрезе укрупнений по кол-ву позиции на складе
    position_counts = Warehouse.groupby(['size']).size()

    # Масштабировать количество позиций в соответствии с размером аукциона
    position_counts = (position_counts * (auction_size / position_counts.sum())).round().astype(int)

    # Вычесть количество уже отобранных позиций из общего количества позиций
    selected_position_counts = selected_items.groupby(['size']).size()
    position_counts = position_counts.subtract(selected_position_counts, fill_value=0).astype(int)
    position_counts = position_counts.apply(lambda x: 0 if x < 0 else x)

    # Создать итоговую выборку на аукцион, соответствующую долям позиций
    auction_items = selected_items.copy()
    for position, count in position_counts.items():
        if count > 0:
            print(position)
            print(count)
            position_items = Warehouse.loc[Warehouse[['size']].apply(tuple, axis=1) == position]
            sampled_items = position_items.sample(n=count, replace=False, random_state=42)
            auction_items = pd.concat([auction_items, sampled_items])

    return auction_items

def stratification_warehouse(data, lot_count, ba_percentage):
    return data.sample(lot_count)

def algorithm3(data, lot_count, stock_percentage, ba_percentage):
    # Реализация алгоритма 3
    pass

def get_algorithm_info():
    return {
        "algorithm1": {
            "name": "Алгоритм 1",
            "description": "Описание алгоритма 1",
        },
        "algorithm2": {
            "name": "Алгоритм 2",
            "description": "Описание алгоритма 2",
        },
        "algorithm3": {
            "name": "Алгоритм 3",
            "description": "Описание алгоритма 3",
        },
    }

ALGORITHMS = {
    "algorithm1": algorithm1,
    "algorithm2": stratification_warehouse,
    "algorithm3": algorithm3,
}


###################################################################################################
#
# Блок реализации функции выбранного алгоритма и колбэка
#
###################################################################################################

from dash.dependencies import Input, Output, State
import pandas as pd
import dash_html_components as html

# Создайте функцию для запуска алгоритма и возвращения результатов
def run_algorithm(algorithm, lot_count, stock_percentage, ba_percentage, data):
    # Здесь вы можете вызывать функцию, реализующую выбранный алгоритм,
    # и передавать ей параметры lot_count, stock_percentage, ba_percentage
    if algorithm == "algo1":
        result = algorithm1(data, lot_count, stock_percentage, ba_percentage)
    elif algorithm == "algo2":
        result = algorithm2(data, lot_count, stock_percentage, ba_percentage)
    else:
        result = "Выбранный алгоритм в разработке"

    return result

# # Колбек для обработки отправки формы
# @app.callback(
#     Output("result-output", "children"),
#     [
#         Input("submit-button", "n_clicks")
#     ],
#     [
#         State("algorithm-selection", "value"),
#         State("lot-count", "value"),
#         State("stock-percentage", "value"),
#         State("ba-percentage", "value"),
#     ],
# )
# def process_form(n_clicks, algorithm, lot_count, stock_percentage, ba_percentage):
#     if n_clicks is None:
#         return "Здесь будет выводиться результат."
#
#     result = run_algorithm(algorithm, lot_count, stock_percentage, ba_percentage)
#
#     # Создайте выходной файл Excel с результатами
#     output_df = pd.DataFrame({"Результат": [result]})
#     output_df.to_excel("output.xlsx", index=False)
#
#     return html.Div("Результат аукциона:")

###################################################################################################
#
# Конец блока
#
###################################################################################################