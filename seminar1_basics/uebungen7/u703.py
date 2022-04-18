from tools import mytools as mt


def main():
    mt.h1("Übung 7.3 - remove Elements from Lists")

    l1 = [1, 2, 3, 4, 5, "java",
          11, "python", 11, "python", 12, 12]
    print(l1)

    mt.h2("pop(x) - 4(5), 4(java)")
    p1 = l1.pop(4)
    p2 = l1.pop(4)
    print(l1, p1, p2)

    mt.h2("pop() - 12")
    p3 = l1.pop()
    print(l1, p3)

    mt.h2("remove() - by value 11,python")
    print(l1)
    l1.remove(11)
    print(l1)
    l1.remove("python")
    print(l1)

    mt.h2("clear() - all elements")
    l1.clear()
    print(l1)

   
    mt.end(__name__)



if __name__ == "__main__":
    main()
