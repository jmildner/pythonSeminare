from tools import mytools as mt, const

people = []
file_name = const.temp + "/u8c.txt"


def get_people_from_console():
    pnr = mt.gets("enter pnr (end=$$$)")
    while pnr != "$$$":
        name = mt.gets("enter name")
        addr = mt.gets("enter addr")
        person = (pnr, name, addr)
        people.append(person)
        pnr = mt.gets("enter pnr (end=$$$)")


def write_file():
    with open(file_name, "w", encoding='utf-8') as file:
        for i, p in enumerate(people):
            pnr, name, addr = p
            if i != 0:
                file.write("\n")
            file.write(pnr + const.delimiter + name + const.delimiter + addr)
    print(file_name + " written")


def read_file():
    with open(file_name, "r", encoding='utf-8') as file:
        buffer = file.read()
        if len(buffer) > 0:
            people2 = buffer.split("\n")
            for p in people2:
                person = p.split(const.delimiter)
                pnr, name, addr = person
                print(pnr, name, addr)


def main():
    mt.h1("Übung 8.1 - read files")
    get_people_from_console()
    write_file()
    read_file()

    mt.end(__name__)


if __name__ == "__main__":
    main()
