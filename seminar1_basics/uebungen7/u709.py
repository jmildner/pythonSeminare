from tools import mytools as mt


def main():
    mt.h1("Übung 7.9 - Dictionary")

    mt.h1("erstellen")
    students = {}
    print(students, type(students))
    students = {"ben": 6, "ann": 6, "urs": 4, "fritz": 6, "max": 4, "hans": 6}
    print(students)

    mt.h1("lesen und anpasen")
    s1 = students["max"]
    print(s1)
    students["max"] = 5  # anpassen
    print(students)

    mt.h1("hinzufügen und löschen")
    students["alexander"] = 4.4
    print(students)
    s2 = students.pop("urs")  # keyError wenn urs nicht vorhanden
    print(s2)
    print(students)
    del students["ben"]  # keyError wenn ben nicht vorhanden
    print(students)

    if "ann" in students:
        del students["ann"]
        print("ann gelöscht")
    else:
        print("ann nicht vorhanden")

    if "ann" in students:
        del students["ann"]
        print("ann gelöscht")
    else:
        print("ann nicht vorhanden")

    mt.h1("über key iterieren")

    for key in students:
        print(key)

    mt.h1("über value iterieren")
    for value in students.values():
        print(value)

    mt.h1("über key und value iterieren")
    for key, value in students.items():
        print(f"{key:10} {value}")

  
    mt.end(__name__)



if __name__ == "__main__":
    main()
