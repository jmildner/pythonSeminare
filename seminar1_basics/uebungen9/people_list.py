import random

from seminar1_basics.uebungen9.person import Person
from tools import mytools as mt, const


class PeopleList:

    def __init__(self) -> None:
        self.__number_addresses = 0
        self.__people = []

    def add(self) -> None:
        self.__number_addresses += 1
        self.__people.append(Person())

    def show(self) -> None:
        print(f"\nnumber of addresses: {self.__number_addresses}")
        print("------------------------")
        for i in range(self.__number_addresses):
            self.__people[i].show()

    def read(self) -> None:
        try:
            with open(const.people_file_name, 'r') as file:
                buffer = file.read()
                if len(buffer) == 0:
                    print("no addresses available")
                else:
                    addresses = buffer.split("\n")
                    for person in addresses:
                        elements = person.split(const.delimiter)
                        pnr = int(elements[0])
                        name = elements[1]
                        addr = elements[2]
                        self.__number_addresses += 1
                        person = Person(pnr, name, addr)
                        self.__people.append(person)
                    print(f"{self.__number_addresses} addresses read")
        except FileNotFoundError:
            print("no addresses available")

        print()

    def save(self) -> None:
        with open(const.people_file_name, 'w') as file:
            for i in range(self.__number_addresses):
                if i != 0:
                    file.write("\n")
                file.write(str(self.__people[i]))
        print(f"{self.__number_addresses} addresses saved into "
              f"'{const.people_file_name}'")

    def mass_insert(self) -> None:
        number = 10
        for i in range(number):
            pnr = random.randint(1_000, 9_999)
            name = f'n-{str(random.randint(1, 9))}'
            addr = f'a-{str(random.randint(1, 9))}'
            person = Person(pnr, name, addr)
            self.__number_addresses += 1
            self.__people.append(person)
        print(f'{number} addresses inserted')

    def sort(self) -> None:
        for i in range(0, self.__number_addresses - 1):
            for j in range(i + 1, self.__number_addresses):
                vi = self.__people[i].get_pnr()
                vj = self.__people[j].get_pnr()
                if vi > vj:
                    self.__people[i], self.__people[j] = \
                        self.__people[j], self.__people[i]
        print("addresses sorted")

    def remove(self) -> None:
        if self.__number_addresses == 0:
            print("\tnothing to delete")
            print()
            return

        addr_id = mt.geti_r("\tid to delete", 0, 100000)
        ix_to_delete = -1
        for i in range(self.__number_addresses):
            if self.__people[i].get_pnr() == addr_id:
                ix_to_delete = i
                break
        if ix_to_delete > -1:
            del (self.__people[ix_to_delete])
            self.__number_addresses -= 1
            print(f"Index {ix_to_delete} deleted")
        else:
            print(f"ID {addr_id} not found")

        print()
