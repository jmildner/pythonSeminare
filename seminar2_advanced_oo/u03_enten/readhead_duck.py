from seminar2_advanced_oo.u03_enten.duck import Duck


class RedheadDuck(Duck):

    def show(self):
        print("I am a RedheadDuck, one of", Duck.get_number_of_ducks(), "Ducks")
