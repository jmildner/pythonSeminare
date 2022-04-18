from tools import mytools as mt, const

file_name_1 = const.temp + "/u8a.txt"
file_name_2 = const.temp + "/u8b.txt"


def read_file_1():
    mt.h2("read and show file 1")
    file = open(file_name_1, "r", encoding='utf-8')
    buffer = file.read()
    lines = buffer.split("\n")
    print(lines)
    file.close()


def read_file_2():
    mt.h2("read and show file 2")
    with open(file_name_2, "r", encoding='utf-8') as file:
        buffer = file.read()
        lines = buffer.split("\n")
        print(lines)


def main():
    mt.h1("Übung 8.1 - read files")
    read_file_1()
    read_file_2()

    mt.end(__name__)


if __name__ == "__main__":
    main()
