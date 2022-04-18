class Phonebook:
    def __init__(self):
        self.__entries = {}

    def add(self, name, number):
        self.__entries[name] = number

    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return "not available"
