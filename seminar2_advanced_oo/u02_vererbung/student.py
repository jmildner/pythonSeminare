from seminar2_advanced_oo.u01_classes.person2 import Person2


class Student(Person2):

    def __init__(self, pnr, name, matr_nr):
        self.__matr_nr = matr_nr
        super().__init__(pnr, name)

    def __str__(self):
        super_string = super().__str__()
        self_string = "matr_nr=" + str(self.__matr_nr)
        return super_string + ", " + self_string

    def get_matr_nr(self):
        return self.__matr_nr

    def set_matr_nr(self, matr_nr):
        self.__matr_nr = matr_nr

    def show(self):
        print(f"Student: {self}")
