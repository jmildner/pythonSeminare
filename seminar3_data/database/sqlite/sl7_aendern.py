import sqlite3
from tools import mytools as mt, const


def ausgabe(cursor):
    # SQL-Abfrage, senden, Ausgabe
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])
    print()


def main():
    mt.h1("sqlite aendern")

    # Verbindung, Cursor
    connection = sqlite3.connect(const.temp+"/firma.db")
    cursor = connection.cursor()

    # Vorher
    ausgabe(cursor)

    # Datensatz aktualisieren
    sql = "UPDATE personen SET gehalt = 3788 " \
        "WHERE personalnummer = 81343"
    cursor.execute(sql)
    connection.commit()

    # Nachher
    ausgabe(cursor)

    connection.close()

    mt.end(__name__)


if __name__ == "__main__":
    main()
