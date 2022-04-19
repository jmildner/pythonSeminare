from seminar2_advanced_oo.u03_enten.duck import Duck


class WoodenDuck(Duck):

    def show(self):
        print("I am a WoodenDuck, one of", Duck.get_number_of_ducks(), "Ducks")

    def do_fly(self):
        print("I cannot fly")

    def do_quack(self, number=1):
        print("I cannot quack " * number)
