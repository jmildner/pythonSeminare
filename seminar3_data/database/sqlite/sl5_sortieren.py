import sqlite3
from tools import mytools as mt, const

def main():
    mt.h1("sqlite sortieren")

    # Verbindung, Cursor
    connection = sqlite3.connect(const.temp+"/firma.db")
    cursor = connection.cursor()

    # Sortierung absteigend
    sql = "SELECT * FROM personen ORDER BY gehalt DESC"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[3])
    print()

    # Sortierung nach mehreren Feldern
    sql = "SELECT * FROM personen ORDER BY name, vorname"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1])

    connection.close()

    mt.end(__name__)

if __name__ == "__main__":
    main()
