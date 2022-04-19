from seminar2_advanced_oo.u03_enten.duck import Duck


class RubberDuck(Duck):

    def show(self):
        print("I am a RubberDuck, one of", Duck.get_number_of_ducks(), "Ducks")

    def do_fly(self):
        print("I cannot fly")

    def do_quack(self, number=1):
        print("quietsch " * number)