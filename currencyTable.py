import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        cursor.close() 
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        

dropcurrency = '''
DROP TABLE currency;
'''

create_currency_table='''
CREATE TABLE currency(
    location VARCHAR(20) PRIMARY KEY,
    measure VARCHAR(6),
    value DECIMAL(18,4)
    );
'''

connection = create_db_connection('localhost', 'root', '123Twister!', 'exchange')

loadtable = '''
LOAD DATA INFILE 'currencyData2020.csv' INTO TABLE currency
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
(location, measure, value);'''

localon = '''
SET GLOBAL local_infile = true;'''

pivot = '''
SELECT location, value FROM currency;

SELECT
'''





execute_query(connection, dropcurrency)
execute_query(connection, create_currency_table)
execute_query(connection, localon)
execute_query(connection, loadtable)






















        




