from seminar2_advanced_oo.u01_classes.person1 import Person1
from seminar2_advanced_oo.u01_classes.person2 import Person2
from tools import mytools


def t_p1():
    mytools.h2("test person1 - no constructor")
    p1 = Person1()
    p1.set_name("Hugo")
    p1.alter = 27
    print(f"name: {p1.name}, alter: {p1.alter}")
    print()
    p2 = Person1()
    p2.public_name = "pub name"
    p2._protected_name = "prot name"
    p2.show()
    p1.show()


def t_p2():
    mytools.h2("test p2")
    p = Person2(32, "hugo")
    p.show()
    p.set_name("xxxx")
    print(f"name: {p.get_name()}")
    p.show()
    print()


def show(p):
    p.show()


def t_p3():
    mytools.h2("test p3 destructor")
    p = Person2(32, "hugo")
    p.show()
    del p
    show(Person2(111, "xxx"))
    Person2(112, "yyy")
    print()


def main():
    mytools.h1("U01 Classes")
    t_p1()
    t_p2()
    t_p3()


if __name__ == "__main__":
    main()
