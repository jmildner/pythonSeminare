class Person2:

    def __init__(self, pnr, name):
        self.__pnr = pnr
        self.__name = name
        print("constructed", end=" ... ")
        self.show()

    def __del__(self):
        print(f"destructing ... {self}")

    def __str__(self):
        return f"id={self.__pnr}, name={self.__name}"

    def show(self):
        print("Person:", self)

    def get_pnr(self):
        return self.__pnr

    def set_pnr(self, pnr):
        self.__pnr = pnr

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
