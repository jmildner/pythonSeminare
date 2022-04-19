from seminar2_advanced_oo.u01_classes.person2 import Person2
from seminar2_advanced_oo.u02_vererbung.student import Student
from tools import mytools


def t_s1():
    mytools.h2("test student")
    s = Student(42, "hugo", 4711)
    s.show()


def t_ps():
    mytools.h2("test person und student")
    p = Person2(81, "moritz")
    s = Student(42, "hugo", 4711)
    print(p)
    print(s)


def show(p):
    p.show()


def t_show():
    mytools.h2("test show")
    show(Person2(5, "albert"))
    show(Student(7, "fritz", 123))


def main():
    mytools.h1("U02 Inheritance")
    t_s1()
    t_ps()
    t_show()


if __name__ == "__main__":
    main()
