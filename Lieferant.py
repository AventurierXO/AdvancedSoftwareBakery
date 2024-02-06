#Domain Lieferant

import Lager

class Lieferant:
    def __init__(self, name):
        self.__name = name

    def gibt_Name(self):
        return self.__name

    def erfüllt_Lieferung(self, bestellung):
        fertige_lieferung = testlagerarbeiter.stellt_Lieferung_zusammen(bestellung)
        Lager.testbestand.wird_gelagert(fertige_lieferung)
        rechnung = self.erstellt_Rechnung(fertige_lieferung)
        print(f"Die bestellte Lieferung kostet {rechnung} €.")
        return rechnung


    def erstellt_Rechnung(self, lieferung, anzahl = 50):
        rechnung = 0
        for teillieferung in lieferung:
            preis = preisliste[teillieferung]
            rechnung += preis * anzahl
        rechnung = format(rechnung, ".2f")
        return rechnung

    def liefert_Bestellung(self, lieferung):
        for ware in lieferung:
            Lager.testbestand.wird_gelagert(ware)

class Lagerarbeiter:

    def stellt_Lieferung_zusammen(self, bestellung):
        lieferung= []
        for ware in bestellung:
            lieferung.append(ware)
        return lieferung
        print(f"Der Lagerarbeiter der Lieferung hat die Bestellung zusammengestellt: {lieferung}")

class Lieferbestand:

    def __init__(self, bestand):
        self.__bestand = bestand

    def prüft_bestand(self):
        return self.__bestand

bestand = {
    "Mehl": 1000,
    "Zucker": 1000,
    "Milch": 1000,
    "Eier": 1000,
    "Glasur": 1000,
    "Hefe": 1000,
    "Streusel": 1000
}

preisliste = {
    "Mehl": 1.00,
    "Zucker": 1.00,
    "Milch": 1.50,
    "Eier": 2.50,
    "Glasur": 1.80,
    "Hefe": 1.80,
    "Streusel": 2.00
}

testlieferbestand = Lieferbestand(bestand)
testlieferant = Lieferant("Speedy Food")
testlagerarbeiter = Lagerarbeiter()