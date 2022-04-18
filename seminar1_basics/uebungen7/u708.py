from tools import mytools as mt


def main():
    mt.h1("Übung 7.8 - Set")

    mt.h1("erstellen")

    words = set()
    words = {1, 2, 3, "hallo", "welt", "mars", "universe", 1, 2, 3}
    print(words)

    mt.h1("einfügen")
    words.add("foo")
    words.add("bar")
    words.add("foo")
    words.update([11, 12, 13, "foo"])
    words.update([42])
    words.add("foo")
    words.add("jupiter")
    print(words)

    mt.h1("löschen")
    erg = words.pop()
    print(erg)
    words.remove("bar")
    if "bar" in words:
        words.remove("bar")
    else:
        print("bar nicht (mehr) vorhanden")
    print(words)
    words.discard("mars")
    words.discard("mars")
    print(words)

    mt.h1("check if vorhanden")

    if "jupiter" in words:
        print("jupiter vorhanden")
    else:
        print("jupiter nicht vorhanden")

    if "sirius" in words:
        print("sirius vorhanden")
    else:
        print("sirius nicht vorhanden")

    mt.h1("iterieren")

    for word in words:
        print(word)

   
    mt.end(__name__)



if __name__ == "__main__":
    main()
