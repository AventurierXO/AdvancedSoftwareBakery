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
        print(f"Der Kunde möchte folgende Backwaren kaufen: {bestellung}")
        return bestellung

    def gibt_Name(self):
        return self.__name

    def gibt_Bestellung_auf(self, bestellung):
        # Bestellung ist in Auslage definiert
        print(f"Der Kunde bestellt folgende Backwaren für morgen zum Abholen: {bestellung}")
        bestellung = Auslage.Bestellung(bestellung)
        return bestellung

    def holt_Bestellung_ab(self, bestellung):
        print("Der Kunde holt seine Bestellung ab.")
        print(Auslage.bestellung.schaut_Bestellung_an())

    def bezahlen(self, rechnung):
        geldbetrag = rechnung
        print(f"Der Kunde überreicht {rechnung}€.")
        return geldbetrag

    def bestellt_Kaffee(self):
        print("Der Kunde bestellt einen Kaffee.")
        # braucht noch Inventar in der Auslage

    # Betreten des Verkaufsraums erstellt Kunden?
    # Verlassen des Verkaufsraums löscht Kunden, falls dieser keine Bestellung aufgegeben hat

testkunde = Kunde("Alexandra")