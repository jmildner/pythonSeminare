import mysql.connector
from tools import mytools as mt


# download and install mysql-connector
# pip install mysql-connector-python

def main():
    mt.h1("mysql - create")

    # Docker - Database
    conn = mysql.connector.connect(
        user='root', password='geheim', host='localhost', port='3316')

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Dropping database MYDATABASE if already exists.
    cursor.execute('DROP database IF EXISTS MYDATABASE')

    # Preparing query to create a database
    sql = "CREATE database MYDATABASE"

    # Creating a database
    cursor.execute(sql)

    # Retrieving the list of databases
    print("List of databases: ")
    cursor.execute("SHOW DATABASES")
    # print(cursor.fetchall())

    all_dbs = cursor.fetchall()
    for db in all_dbs:
        print("    ", db[0])  # db ist ein tuple

    # Closing the connection
    conn.close()


if __name__ == "__main__":
    main()
