import mysql.connector


def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="employee_db"
        )

        return connection

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None