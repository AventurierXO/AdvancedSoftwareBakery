import random


class Kunde:
    def __init__(self, name):
        self.__name = name

    def gibt_Name(self):
        return self.__name

    def kauft_Backwaren(self, auslage, verkäufer):
        # Die Bestellungen der Kunden werden zufällig generiert
        bestellung = []
        anzahl_versch_waren = random.randint(1,4)
        liste_waren = auslage.schaue_Waren_an()
        for anzahl in range(anzahl_versch_waren):
            gewünschte_waren = random.choice(liste_waren)
            anzahl_gewünschter_waren = random.randint(1, 4)
            bestellung.append((gewünschte_waren, anzahl_gewünschter_waren))
        print(f"Der Kunde möchte folgende Waren kaufen: {bestellung}")
        verkäufer.verkaufe_Waren(bestellung)

    def kauft_Heißgetränk(self, kaffeemaschine, verkäufer):
        bestellung = []
        anzahl_versch_waren = random.randint(1, 2)
        liste_getränke = kaffeemaschine.schaut_Optionen_an()
        for anzahl in range(anzahl_versch_waren):
            gewünschte_waren = random.choice(liste_getränke)
            anzahl_gewünschter_waren = random.randint(1, 2)
            bestellung.append((gewünschte_waren, anzahl_gewünschter_waren))
        print(f"Der Kunde möchte folgende Backwaren kaufen: {bestellung}")
        verkäufer.verkaufe_Getränke(bestellung)

    def bezahlen(self, rechnung):
        if rechnung <= 0:
            raise ValueError("Der zu bezahlende Betrag darf nicht 0 oder kleiner sein!")
        geldbetrag = rechnung
        print(f"Der Kunde bezahlt {rechnung}€.")
        return geldbetrag
