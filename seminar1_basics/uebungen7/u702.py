from tools import mytools as mt


def main():
    mt.h1("Übung 7.2 - add Elements to Lists")

    l1 = [1, 2, 3, 4, 5]
    l2 = ["john", "wolf", "main street 17"]

    print(l1)
    print(l2)

    mt.h2("append")
    l1.append(11)
    l1.append(12)
    print(l1)
    l2.append(1234)  # plz
    l2.append("los angeles")
    print(l2)

    mt.h2("extend")
    l1.extend([21, 22, 23, 24])
    print(l1)
    l2.extend(["butcher", 3])  # profession, children
    print(l2)


    mt.end(__name__)


if __name__ == "__main__":
    main()
