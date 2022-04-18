from seminar1_basics.uebungen9.person import Person
from tools import mytools


def main():
    mytools.h1("Übung 9.1 - OO Person")

    mytools.h2("Person")
    pers3 = Person()
    pers3.show()
    pers1 = Person(42, "max", "basel")
    pers1.show()

    print("\n*** end of u91 ***")


if __name__ == "__main__":
    main()
