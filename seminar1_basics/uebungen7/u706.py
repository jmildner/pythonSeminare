from tools import mytools as mt


def main():
    mt.h1("Übung 7.6 - List iteration")

    l1 = list(range(201, 218, 4))
    print(l1)

    print()
    for e in l1:
        print(e)

    print()
    for i in range(len(l1)):
        print(i, l1[i])

    print()
    for i, e in enumerate(l1):
        print(i, e)

    mt.end(__name__)


if __name__ == "__main__":
    main()
