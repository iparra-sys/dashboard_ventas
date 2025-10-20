import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='iveth_user',
        password='Angel1308.',
        database='dashboard_ventas_db'
    )
