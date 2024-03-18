import random

class BestellungBuilder:

    def Gebäckoptionen(self, gebäcke):
        self.gebäcke = gebäcke
        return self

    def Getränkeoptionen(self, getränke):
        self.getränke = getränke
        return self

    def Backbestellung_erzeugen(self):
        bestellung = []
        # Die Bestellungen der Kunden werden zufällig generiert
        anzahl_versch_waren = random.randint(1, 4)
        for anzahl in range(anzahl_versch_waren):
            gewünschte_waren = random.choice(self.gebäcke)
            anzahl_gewünschter_waren = random.randint(1, 4)
            bestellung.append((gewünschte_waren, anzahl_gewünschter_waren))
        return bestellung

    def Getränkebestellung_erzeugen(self):
        bestellung = []
        anzahl_versch_waren = random.randint(1, 2)
        for anzahl in range(anzahl_versch_waren):
            gewünschte_waren = random.choice(self.getränke)
            anzahl_gewünschter_waren = random.randint(1, 2)
            bestellung.append((gewünschte_waren, anzahl_gewünschter_waren))
        return bestellung