import sys

from tools import mytools

global_variable = 4711


def vorlauf():
    global global_variable
    global_variable += 4712
    print(global_variable, lv)


def main():
    mytools.h1("main")

    print("argc: ", len(sys.argv))
    for i, eachArg in enumerate(sys.argv):
        print(f"argv[{i}]: {eachArg}")

    global lv, lv2
    lv = 1.7
    lv2 = "hallo"

    local_variable = 815

    print(global_variable, local_variable)
    vorlauf()
    print(global_variable, local_variable)
    print(lv)
    print("\n*** end of program ***")


if __name__ == "__main__":
    main()
