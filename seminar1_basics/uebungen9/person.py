from tools import mytools as mt, const


class Person:
    def __init__(self, *args):
        if len(args) == 3:
            self.__pnr = args[0]
            self.__name = args[1]
            self.__address = args[2]
        elif len(args) == 0:
            self.__pnr = mt.geti("enter pnr  ")
            self.__name = mt.gets("enter name ")
            self.__address = mt.gets("enter addr ")
        else:
            self.__pnr = 0
            self.__name = "ma"
            self.__address = "na"

    def get_pnr(self):
        return int(self.__pnr)

    def show(self):
        print(f"{self.__pnr:10} ", end="")
        print(f"\t\t{self.__name:20} ", end="")
        print(f"{self.__address}")

    def __str__(self):
        return str(self.__pnr) + \
               const.delimiter + self.__name + \
               const.delimiter + self.__address
