class Kasse:
    def __init__(self, geld, preisliste):
        self.__geld = geld
        self.preisliste = preisliste

    def geld_in_kasse(self):
        return self.__geld

    def geld_einzahlen(self, betrag):
        if betrag <= 0:
            raise ValueError("Es sollen keine Beträge kleiner oder gleich 0 eingezahlt werden!")
        self.__geld += float(betrag)

    def erstelle_Rechnung(self, einkauf):
        preisliste_check = self.preisliste.prüf_Preisliste()
        rechnung = 0
        if einkauf == []:
            raise ValueError("Der zu bezahlende Einkauf kann nicht leer sein!")
        for ware in einkauf:
            if ware[0] not in preisliste_check:
                raise KeyError(f"Die bestellte Ware {ware[0]} ist nicht in der Preisliste!")
            rechnung += ware[1] * preisliste_check[ware[0]]
        return rechnung
