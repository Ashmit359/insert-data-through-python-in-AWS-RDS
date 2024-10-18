import mysql.connector
from mysql.connector import Error

host = 'enter host name here'   
database = 'data_insert_python'  
user = 'admin'      
password = 'enter password here'  

try:
   
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        print("Connected to MariaDB")

        cursor = connection.cursor()

        insert_query = """INSERT INTO employees (id, name, hire_date) 
                          VALUES (%s, %s, %s)"""
        data_to_insert = (3, 'deepak', '2024-10-01')

        cursor.execute(insert_query, data_to_insert)

        connection.commit()

        print("Data inserted successfully")

except Error as e:
    print(f"Error while connecting or inserting: {e}")

finally:

    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MariaDB connection closed")
