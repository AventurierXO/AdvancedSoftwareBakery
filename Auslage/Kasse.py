class Kasse:
    def __init__(self, geld):
        self.__geld = geld

    def geld_in_kasse(self):
        return self.__geld

    def geld_einzahlen(self, betrag):
        if betrag <= 0:
            raise ValueError("Es sollen keine Beträge kleiner oder gleich 0 eingezahlt werden!")
        self.__geld += float(betrag)
        print(f"Es wurden {betrag} € in die Kasse eingezahlt.")
