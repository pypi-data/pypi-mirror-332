# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:42:10 2025

@author: qiyu
"""
import mysql.connector
from mysql.connector import Error, DatabaseError
import pandas as pd
def create_connection(db_config):
    """Create a database connection using the configuration provided."""
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        print("MySQL Database connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def fetch_table(db_config, db_name, table_name, index_col = None):
    """Fetch a specific table from a database and return it as a DataFrame."""
    # 创建数据库连接
    db_config['database'] = db_name  # 设置要连接的数据库
    connection = create_connection(db_config)
    
    if connection is None:
        print("Failed to create the database connection.")
        return None
    
    try:
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql(query, connection)
        # print(f"Data fetched successfully from table '{table_name}' in database '{db_name}'")
        if index_col:
            df = df.set_index(index_col)
        return df
    except Error as e:
        print(f"The error '{e}' occurred")
        return None
    finally:
        connection.close()  # 关闭连接

def fill_missing_values(df):
    """Fill NaN values based on column types."""
    for column in df.columns:
        dtype = str(df[column].dtype)
        if 'int' in dtype:
            df[column].fillna(0, inplace=True)  # Fill NaN for integers with 0

        elif 'float' in dtype:
            df[column].fillna(0.0, inplace=True)  # Fill NaN for floats with 0.0

        elif 'datetime' in dtype or 'date' in dtype:
            df[column].fillna(pd.Timestamp('1970-01-01'), inplace=True)  # Fill NaN for dates with a default date

        else:
            df[column].fillna('', inplace=True)  # Fill NaN for strings with empty string