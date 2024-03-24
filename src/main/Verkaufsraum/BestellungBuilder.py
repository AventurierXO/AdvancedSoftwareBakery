import random

class BestellungBuilder:

    def gebaeckoptionen(self, gebaecke):
        self.gebaecke = gebaecke
        return self

    def getraenkeoptionen(self, getraenke):
        self.getraenke = getraenke
        return self

    def backbestellung_erzeugen(self):
        bestellung = []
        # Die Bestellungen der Kunden werden zufaellig generiert
        anzahl_versch_waren = random.randint(1, 4)
        for anzahl in range(anzahl_versch_waren):
            gewuenschte_waren = random.choice(self.gebaecke)
            anzahl_gewuenschter_waren = random.randint(1, 4)
            bestellung.append((gewuenschte_waren, anzahl_gewuenschter_waren))
        return bestellung

    def getraenkebestellung_erzeugen(self):
        bestellung = []
        anzahl_versch_waren = random.randint(1, 2)
        for anzahl in range(anzahl_versch_waren):
            gewuenschte_waren = random.choice(self.getraenke)
            anzahl_gewuenschter_waren = random.randint(1, 2)
            bestellung.append((gewuenschte_waren, anzahl_gewuenschter_waren))
        return bestellung