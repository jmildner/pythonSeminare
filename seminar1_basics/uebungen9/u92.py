from tools import mytools
from seminar1_basics.uebungen9.phonebook import Phonebook

book = Phonebook()


def create():
    book.add("meier", "123456789")
    book.add("miller", "77887788")
    book.add("schuster", "123432123")
    book.add("lincoln", "993432123")
    book.add("E.T.", "00000999-3463456546345634634654455456549934-32123")


def lookup(name):
    print(f"{name:10}: {book.get(name)} ")


def main():
    mytools.h1("Übung 9.2 - OO Phonebook")

    create()
    lookup("miller")
    lookup("erwin")
    lookup("meier")
    lookup("E.T.")

    print("\n*** end of u92 ***")


if __name__ == "__main__":
    main()
