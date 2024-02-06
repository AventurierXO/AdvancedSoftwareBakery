#Domain Lager

import Backstube, Auslage

class Lagerbestand:
    def __init__(self, bestand):
        self.__bestand = bestand

    def prüft_Bestand(self):
        return self.__bestand

    def wird_gelagert(self, waren):
        print(waren)
        lagerbestand = self.prüft_Bestand()
        for teil in waren:
            lagerbestand[teil] += 50
        print(f"Der Lagerbestand wurde mit {waren} aufgefüllt.")
        print(f"Der Lagerbestand sieht nun so aus: {lagerbestand}")

    def wird_aus_dem_Lager_genommen(self, waren):
        # waren ist eine Liste von Waren
        lagerbestand = self.prüft_Bestand()
        geholte_waren = []
        for teil in waren:
            if lagerbestand[teil] < 50:
                print(f"Es sind nicht mehr genug Stück von {teil} eingelagert.")
            else:
                lagerbestand[teil] -= 50
                geholte_waren.append(teil)
        print(f"Es wurden folgende Waren aus dem Lager geholt: {geholte_waren}")
        print(f"Der Lagerbestand sieht nun so aus: {lagerbestand}")
        return geholte_waren

lagerbestand = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
    "Roggenmischbrot": 50,
    "Vollkornbrot": 50,
    "Dinkelbrot": 50,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 50,
    "Pfannkuchen": 50,
    "Mehl": 50,
    "Zucker": 50,
    "Milch": 30,
    "Eier": 30,
    "Glasur": 50,
    "Hefe": 50,
    "Streusel": 50
}

testbestand = Lagerbestand(lagerbestand)