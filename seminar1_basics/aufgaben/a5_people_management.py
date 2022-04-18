from seminar1_basics.uebungen9.people_list import PeopleList
from tools import mytools

number_addresses = 0
people_list = PeopleList()


def main():
    pre_processing()
    main_processing()
    post_processing()


def pre_processing():
    start_message()
    people_list.read()


def main_processing():
    show_help()
    action = get_action()
    while action != 0:
        vera(action)
        action = get_action()


def post_processing():
    people_list.save()
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
        people_list.add()
    elif action == 2:
        people_list.show()
    elif action == 3:
        people_list.sort()
    elif action == 4:
        people_list.remove()
    elif action == 5:
        people_list.save()
    elif action == 6:
        show_help()
    elif action == 7:
        people_list.mass_insert()
    else:
        return


def start_message():
    print("---------------------------------")
    print("Program: a5_people_management    ")
    print("Author:  Johann Mildner          ")
    print("---------------------------------")
    print("this program is used to maintain")
    print("an address file")
    print()


def stop_message():
    print("*** end of Program ***")
    print("Thank you for using this Program, Good Bye!")
    print("-------------------------------------------")


if __name__ == "__main__":
    main()
