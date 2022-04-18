from tools import mytools as mt, const

texte = []
file_name_1 = const.temp + "/u8a.txt"
file_name_2 = const.temp + "/u8b.txt"


def get_text():
    return mt.gets("enter text ($$$=end)")


def get_data_from_console():
    text = get_text()
    while text != "$$$":
        texte.append(text)
        text = get_text()
    print(texte)


def write_file_1():
    file = open(file_name_1, "w", encoding='utf-8')
    for i, t in enumerate(texte):
        if i == 0:
            file.write(t)
        else:
            file.write("\n" + t)
    file.close()
    print(file_name_2 + " written")


def write_file_2():
    with open(file_name_2, "w", encoding='utf-8') as file:
        for i, t in enumerate(texte):
            if i == 0:
                file.write(t)
            else:
                file.write("\n" + t)
    print(file_name_2 + " written")


def main():
    mt.h1("Übung 8.1 - write files")
    get_data_from_console()
    write_file_1()
    write_file_2()

    mt.end(__name__)


if __name__ == "__main__":
    main()
