from seminar2_advanced_oo.u03_enten.duck import Duck
from seminar2_advanced_oo.u03_enten.lead_duck import LeadDuck
from seminar2_advanced_oo.u03_enten.readhead_duck import  RedheadDuck
from seminar2_advanced_oo.u03_enten.rubber_duck import RubberDuck
from seminar2_advanced_oo.u03_enten.wild_duck import WildDuck
from seminar2_advanced_oo.u03_enten.wooden_duck import WoodenDuck
from tools import mytools


def t1():
    mytools.h2("test 1")
    Duck()  # Duck is created and immediately deleted
    Duck.show_number_of_ducks()

    e2 = Duck()
    Duck.show_number_of_ducks()
    del (e2)
    Duck.show_number_of_ducks()

    list_of_ducks = []
    for i in range(10):
        list_of_ducks.append(Duck())
        Duck.show_number_of_ducks()

    mytools.pause()


def life(e):
    print()
    e.show()
    e.do_fly()
    e.do_swim()
    e.do_quack()


def t2():
    mytools.h2("test 2")
    e1 = Duck()
    life(e1)
    e2 = WildDuck()
    life(e2)
    e3 = RedheadDuck()
    life(e3)
    e4 = WoodenDuck()
    life(e4)
    e5 = LeadDuck()
    life(e5)
    e6 = RubberDuck()
    life(e6)


def main():
    mytools.h1("U03 Enten")
    t1()
    t2()
    t2()
    mytools.pause()


if __name__ == "__main__":
    main()
