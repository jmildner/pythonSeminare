import sqlite3
from tools import mytools as mt, const

def main():
    mt.h1("sqlite eingabe")

    # Verbindung, Cursor
    connection = sqlite3.connect(const.temp+"/firma.db")
    cursor = connection.cursor()

    # Eingabe Name
    eingabe = input("Bitte den gesuchten Namen eingeben: ")
    sql = "SELECT * FROM personen WHERE name LIKE ?"
    cursor.execute(sql, (eingabe,))
    for dsatz in cursor:
        print(dsatz[0], dsatz[1])
    print()

    # Eingabe Teil des Namens
    eingabe = input("Bitte den gesuchten Namensteil eingeben: ")
    sql = "SELECT * FROM personen WHERE name LIKE ?"
    eingabe = '%' + eingabe + '%'
    cursor.execute(sql, (eingabe,))
    for dsatz in cursor:
        print(dsatz[0], dsatz[1])
    print()

    connection.close()

    mt.end(__name__)

if __name__ == "__main__":
    main()
