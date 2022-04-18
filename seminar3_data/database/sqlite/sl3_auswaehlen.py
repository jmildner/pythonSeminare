import sqlite3
from tools import mytools as mt, const


def main():
    mt.h1("sqlite auswaehlen")

    # Verbindung, Cursor
    connection = sqlite3.connect(const.temp+"/firma.db")
    cursor = connection.cursor()

    # SQL-Abfragen
    # Einzelne Felder
    sql = "SELECT name, vorname FROM personen"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1])
    print()

    # Auswahl mit WHERE-Klausel und Vergleichsoperator
    sql = "SELECT * FROM personen " \
        "WHERE gehalt > 3600"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[3])
    print()

    # Auswahl mit Zeichenkette
    sql = "SELECT * FROM personen " \
        "WHERE name = 'Schmitz'"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1])
    print()

    # Auswahl mit logischen Operatoren
    sql = "SELECT * FROM personen " \
        "WHERE gehalt >= 3600 AND gehalt <= 3650"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[3])

    # Verbindung beenden
    connection.close()

    mt.end(__name__)


if __name__ == "__main__":
    main()
