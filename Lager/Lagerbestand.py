class Lagerbestand:
    def __init__(self, bestand):
        self.__bestand = bestand

    def prüft_Bestand(self):
        return self.__bestand

    def prüft_fehlende_Waren(self, lagerbestand, back = True):
        aufzufüllende_Waren = []
        bestand = lagerbestand.prüft_Bestand()
        if back == True:
            backstücke = ("Weizensemmel", "Kürbiskernbrötchen", "Roggenmischbrot", "Vollkornbrot", \
                          "Dinkelbrot", "Croissant", "Streuselkuchen", "Bienenstich", "Pfannkuchen")
            zu_checken = backstücke
        else:
            zutaten = ["Mehl", "Zucker", "Milch", "Eier", "Hefe", "Wasser", "Butter", "Kürbiskerne"]
            zu_checken = zutaten
        for ware in zu_checken:
            if bestand[ware] < 50:
                if bestand[ware] < 0:
                    raise ValueError(f"Ein Lagerbestand darf nicht negativ sein! {ware}")
                aufzufüllende_Waren.append(ware)
        return aufzufüllende_Waren

    def wird_gelagert(self, waren):
        print(waren)
        lagerbestand = self.prüft_Bestand()
        for teil in waren:
            lagerbestand[teil] += 50
        print(f"Der Lagerbestand wurde mit {waren} aufgefüllt.")
        print(f"Der Lagerbestand sieht nun so aus: {lagerbestand}")

    def wird_aus_dem_Lager_genommen(self, waren, anzahl = 50):
        if anzahl == 0 or anzahl == 51:
            raise ValueError("Es muss mindestens ein Stück der Ware aus dem Lager geholt werden bzw. nicht mehr als 50!")
        if waren == []:
            raise ValueError("Es können nur Waren aus dem Lager geholt werden, wenn sie gebraucht werden!")
        lagerbestand = self.prüft_Bestand()
        geholte_waren = []
        for teil in waren:
            if teil not in list(lagerbestand.keys()):
                raise KeyError("Die Ware gibt es im Lager nicht.")
            if lagerbestand[teil] < anzahl:
                print(f"Es sind nicht mehr genug Stück von {teil} eingelagert.")
            else:
                lagerbestand[teil] -= anzahl
                geholte_waren.append(teil)
        if geholte_waren == []:
            raise ValueError("Es können keine Waren geliefert werden, wenn sie im Lager nicht vorhanden sind!")
        print(f"Es wurden folgende Waren aus dem Lager geholt: {geholte_waren}")
        print(f"Der Lagerbestand sieht nun so aus: {lagerbestand}")
        return geholte_waren
