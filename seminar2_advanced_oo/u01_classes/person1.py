class Person1:
    public_name = "public name"
    _protected_name = "protected name"
    __private_name = "private name"

    name = None

    def show(self):
        print("Person1:")
        print("    ", self.public_name)
        print("    ", self._protected_name)
        print("    ", self.__private_name)
        print("    ", self.name)

    def set_name(self, name):
        self.name = name
