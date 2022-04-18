import sqlite3
from tools import mytools as mt, const


def main():
    mt.h1("sqlite like")

    # Verbindung, Cursor
    connection = sqlite3.connect(const.temp+"/firma.db")
    cursor = connection.cursor()

    # SQL-Abfragen

    # Beliebig viele beliebige Zeichen
    sql = "SELECT * FROM personen WHERE name LIKE 'm%'"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1])
    print()

    # Beinhaltet ...
    sql = "SELECT * FROM personen WHERE name LIKE '%i%'"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1])
    print()

    # Einzelne beliebige Zeichen
    sql = "SELECT * FROM personen WHERE name LIKE 'M__er'"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1])

    # Verbindung beenden
    connection.close()

    mt.end(__name__)

if __name__ == "__main__":
    main()
