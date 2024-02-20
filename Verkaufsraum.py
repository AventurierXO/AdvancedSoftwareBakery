#Domain Verkaufsraum

import Auslage
import random
class Kunde:
    def __init__(self, name):
        self.__name = name

    def kauft_Backwaren(self, auslage):
        # Die Bestellungen der Kunden werden zufällig generiert
        bestellung = []
        anzahl_versch_waren = random.randint(1,4)
        liste_waren = auslage.schaue_Waren_an()
        for anzahl in range(anzahl_versch_waren):
            gewünschte_waren = random.choice(liste_waren)
            anzahl_gewünschter_waren = random.randint(1, 4)
            bestellung.append((gewünschte_waren, anzahl_gewünschter_waren))
        print(f"Der Kunde möchte folgende Waren kaufen: {bestellung}")
        return bestellung

    def gibt_Name(self):
        return self.__name

    def bezahlen(self, rechnung):
        geldbetrag = rechnung
        print(f"Der Kunde überreicht {rechnung}€.")
        return geldbetrag

    def kauft_Heißgetränk(self, kaffeemaschine):
        getränke = []
        anzahl_versch_waren = random.randint(1, 2)
        liste_getränke = kaffeemaschine.schaut_Optionen_an()
        for anzahl in range(anzahl_versch_waren):
            gewünschte_waren = random.choice(liste_getränke)
            anzahl_gewünschter_waren = random.randint(1, 2)
            getränke.append((gewünschte_waren, anzahl_gewünschter_waren))
        print(f"Der Kunde möchte folgende Backwaren kaufen: {getränke}")
        return getränke

    # Betreten des Verkaufsraums erstellt Kunden?
    # Verlassen des Verkaufsraums löscht Kunden, falls dieser keine Bestellung aufgegeben hat

testkunde = Kunde("Alexandra")