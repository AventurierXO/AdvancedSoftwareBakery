#Domain Lager

import Backstube, Auslage

class Lagerbestand:
    def __init__(self, bestand):
        self.__bestand = bestand

    def prüf_Bestand(self):
        return self.__bestand

    def wird_gelagert(self, backwaren):
        # backwaren ist eine Liste von Backwaren
        lagerbestand = self.prüf_Bestand()
        for back in backwaren:
            lagerbestand[back] += 50
        print(f"Der Lagerbestand wurde mit {backwaren} aufgefüllt.")
        print(f"Der Lagerbestand sieht nun so aus: {lagerbestand}")

    def wird_aus_dem_Lager_genommen(self, backwaren):
        # backwaren ist eine Liste von Backwerken
        lagerbestand = self.prüf_Bestand()
        geholte_backwaren = []
        for back in backwaren:
            if lagerbestand[back] < 50:
                print(f"Es sind nicht mehr genug Stück von {back} eingelagert.")
            else:
                lagerbestand[back] -= 50
                geholte_backwaren.append(back)
        print(f"Es wurden folgende Backwaren aus dem Lager geholt: {geholte_backwaren}")
        print(f"Der Lagerbestand sieht nun so aus: {lagerbestand}")
        return geholte_backwaren

lagerbestand = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
    "Roggenmischbrot": 50,
    "Vollkornbrot": 50,
    "Dinkelbrot": 50,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 50,
    "Pfannkuchen": 50
}

testbestand = Lagerbestand(lagerbestand)