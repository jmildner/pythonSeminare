class Duck:
    # Class variable
    __number_of_ducks = 0

    @staticmethod
    def get_number_of_ducks():
        return Duck.__number_of_ducks

    @staticmethod
    def show_number_of_ducks():
        print("There are", Duck.get_number_of_ducks(), "Ducks")

    def __init__(self):
        Duck.__number_of_ducks += 1

    def __del__(self):
        Duck.__number_of_ducks -= 1
        print("Duck removing ...")

    def do_fly(self):
        print("I am flying")

    def do_swim(self):
        print("I am swimming")

    def do_quack(self, number=1):
        print("quack " * number)

    def show(self):
        print("I am a Duck, one of", Duck.get_number_of_ducks(), "Ducks")
