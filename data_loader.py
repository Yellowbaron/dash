import pandas as pd
import pyodbc

def load_data_from_sql_server(server, database, table, username, password):
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(connection_string)
    query = f'SELECT * FROM {table}'
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def load_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df

def update_local_database(local_db_path, new_data):
    local_db = pd.read_pickle(local_db_path)
    local_db.update(new_data)
    local_db.to_pickle(local_db_path)

def load_data_from_local_database(local_db_path):
    df = pd.read_pickle(local_db_path)
    return df
