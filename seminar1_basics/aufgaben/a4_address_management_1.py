import random
from tools import mytools

number_addresses = 0
ids = []
names = []
addresses = []


def main():
    pre_processing()
    main_processing()
    post_processing()


def pre_processing():
    start_message()
    read_addresses()


def main_processing():
    show_help()
    action = get_action()
    while action != 0:
        vera(action)
        action = get_action()


def post_processing():
    save_addresses()
    stop_message()


def show_help():
    print('''Action:
    0 = end of program
    1 = input address
    2 = show addresses
    3 = sort addresses
    4 = remove address
    5 = save addresses
    6 = help
    7 = mass insert (only during the test phase) 
    ''')


def get_action():
    return mytools.geti_r("please insert the action (6=help)", 0, 7)


def vera(action):
    if action == 1:
        input_address()
    elif action == 2:
        show_addresses()
    elif action == 3:
        sort_addresses()
    elif action == 4:
        remove_address()
    elif action == 5:
        save_addresses()
    elif action == 6:
        show_help()
    elif action == 7:
        mass_insert()
    else:
        return


def input_address():
    global number_addresses

    addr_id = mytools.geti_r("\tID     ", 1, 100000)
    name = mytools.gets("\tName   ")
    addr = mytools.gets("\tAddress")
    ids.append(addr_id)
    names.append(name)
    addresses.append(addr)
    number_addresses += 1
    print(f'als {number_addresses}. address inserted')

    print()


def mass_insert():
    global number_addresses

    random_id = random.randint(100, 200)
    number = 10
    for i in range(number):
        addr_id = random_id
        name = f'name-{random_id}'
        addr = f'addr-{random_id}'
        random_id += 1
        ids.append(addr_id)
        names.append(name)
        addresses.append(addr)
        number_addresses += 1

    print(f'{number} addresses inserted')
    print()


def show_addresses():
    global number_addresses

    print(f"\nnumber of addresses: {number_addresses}")
    print("------------------------")
    for i in range(number_addresses):
        print(f"{ids[i]:10} ", end="")
        print(f"\t\t{names[i]:20} ", end="")
        print(f"{addresses[i]}")

    print()


def sort_addresses():
    print("sort under construction")
    print()


def remove_address():
    global number_addresses

    if number_addresses == 0:
        print("\tnothing to delete")
        print()
        return

    addr_id = mytools.geti_r("\tid to delete", 0, 100000)
    ix_to_delete = -1
    for i in range(number_addresses):
        if ids[i] == addr_id:
            ix_to_delete = i
            break
    if ix_to_delete > -1:
        ids.pop(ix_to_delete)
        names.pop(ix_to_delete)
        addresses.pop(ix_to_delete)
        number_addresses -= 1
        print(f"Index {ix_to_delete} deleted")
    else:
        print(f"ID {addr_id} not found")

    print()


def read_addresses():
    print("read addresses under construction")
    print()


def save_addresses():
    print()
    print("save addresses under construction")
    print()


def start_message():
    print("-------------------------------")
    print("Program: a4_address_management ")
    print("Author:  Johann Mildner        ")
    print("-------------------------------")
    print("this program is used to maintain")
    print("an address file")
    print()


def stop_message():
    print("*** end of Program ***")
    print("Thank you for using this Program, Good Bye!")
    print("-------------------------------------------")


if __name__ == "__main__":
    main()
