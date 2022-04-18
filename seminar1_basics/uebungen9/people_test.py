from seminar1_basics.uebungen9.people_list import PeopleList
from tools import mytools as mt


def main():
    mt.h1("people_test")

    people_list = PeopleList()
    people_list.read()
    people_list.show()
    mt.h2("mass insert")
    people_list.mass_insert()
    people_list.show()
    mt.h2("sort")
    people_list.sort()
    people_list.show()
    people_list.remove()
    people_list.show()
    mt.pause()
    mt.h2("save")
    people_list.save()

    print("\n*** end of people_test ***")


if __name__ == "__main__":
    main()
