from tools import const

number_addresses = 0
ids = []
names = []
addresses = []


def main():
    read_addresses()
    sort_addresses()
    show_addresses()


def show_addresses():
    global number_addresses

    print(f"\nnumber of addresses: {number_addresses}")
    print("------------------------")
    for i in range(number_addresses):
        print(f"{names[i]:10}", end="")
        print(f"{addresses[i]:10}", end="")
        print(f"{ids[i]}", end="")
        print()


def sort_addresses():
    for i in range(0, len(ids) - 1):
        for j in range(i + 1, len(ids)):
            vi = f"{names[i]:32}{addresses[i]:32}{ids[i]:6}"
            vj = f"{names[j]:32}{addresses[j]:32}{ids[j]:6}"
            if vi > vj:
                ids[i], ids[j] = ids[j], ids[i]
                names[i], names[j] = names[j], names[i]
                addresses[i], addresses[j] = addresses[j], addresses[i]

    print("addresses sorted")
    print()


def read_addresses():
    global number_addresses
    try:
        with open(const.people_file_name, 'r') as file:
            buffer = file.read()
            people = buffer.split("\n")
            for person in people:
                elements = person.split(const.delimiter)
                ids.append(int(elements[0]))
                names.append(elements[1])
                addresses.append(elements[2])
                number_addresses += 1
            print(f"{number_addresses} addresses read")
    except FileNotFoundError:
        print("no addresses available")

    print()


if __name__ == "__main__":
    main()
