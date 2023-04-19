###################################################################

# Sql connection

###################################################################

import pyodbc
from pyodbc import *
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib as plt
import time

# Parameters for Connection
db_tp = (r"Driver={ODBC Driver 17 for SQL Server};"  # odbc database source is 2017
         r"Server=DESKTOP-P08L89R;"
         r"Database=AdventureWorksDW2019;"
         r"UID=db-python;"
         r"PWD=12345;")


# Create Connection function


def create_conn():
    """
    Function to connect Microsoft SQL ODBC 17
    -----------------------------------------
    Returns: Connection command

    """
    try:
        pyodbc.connect(db_tp)
        print('Connection Successful')
    except ConnectionRefusedError:
        print('Connection is not successful')

    return pyodbc.connect(db_tp)


cursor = create_conn().cursor()


# Get Columns


def get_columns(table) -> list:
    """

    Args:
        table: SQL table name in order to get columns names,
                use table name without dbo.

    Returns: list of columns of given table name

    """
    columns_list = []

    for i in cursor.execute(f"SELECT COLUMN_NAME \
    FROM INFORMATION_SCHEMA.COLUMNS \
    WHERE TABLE_NAME = '{table}'"):
        columns_list.append(i[0])

    print(columns_list)
    return columns_list


"""
# type(columns_list[0])  # -> str

# ['ProductKey', 'OrderDateKey', 'DueDateKey', 
# 'ShipDateKey', 'CustomerKey', 'PromotionKey', 
# 'CurrencyKey', 'SalesTerritoryKey', 'SalesOrderNumber', 
# 'SalesOrderLineNumber', 'RevisionNumber', 'OrderQuantity', 
# 'UnitPrice', 'ExtendedAmount', 'UnitPriceDiscountPct', 'DiscountAmount', 
# 'ProductStandardCost', 'TotalProductCost', 'SalesAmount', 'TaxAmt', 'Freight', 
# 'CarrierTrackingNumber', 'CustomerPONumber', 'OrderDate', 'DueDate', 'ShipDate']
"""


# Create pandas dataframe func


def create_dataframe(table):
    import time
    """
    Info: Creates dataframe from sql query for the table given
    Returns: pandas dataframe from the sql query

    """
    columns_list = get_columns(f'{table}')
    start_time = time.time()
    rows = cursor.execute(f"SELECT * FROM {table}")
    df = pd.DataFrame(data=(tuple(t) for t in rows), columns=columns_list)
    print("--- %s seconds ---" % (time.time() - start_time))
    return df


df_ = create_dataframe('FactInternetSales')  # 1.15 seconds with pyodbc
df_.head()
df_.info()  # 60398 rows x 26 columns

###################################################################
# Extra check time

# connection = create_conn()

# st_time = time.time()
# query = """SELECT * FROM FactInternetSales"""
# table = pd.read_sql(query, connection)  # supports SQLAlchemy and takes 1.38 seconds
# print("--- %s seconds ---" % (time.time() - st_time))
# connection.close()

###################################################################

# will try fetchall() later

cursor.close()
