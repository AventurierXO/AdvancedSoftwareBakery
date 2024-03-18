class Lagerbestand:
    def __init__(self, bestand):
        self.__bestand = bestand

    def prüfe_Bestand(self):
        return self.__bestand

    def prüfe_fehlende_Waren(self, back = True):
        """Wenn weniger als 50 Stück von einer Ware vorhanden sind, wird diese aufgenommen. Wenn back == True ist,
        dann werden fehlende Backwaren ermittelt. Wenn back == False ist, dann werden fehlende Zutaten ermittelt."""
        aufzufüllende_Waren = []
        bestand = self.prüfe_Bestand()
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

    def lagere_ein(self, waren):
        """Eine Liste von Waren wird im Lager um 50 Stück nachgefüllt."""
        if waren == []:
            raise ValueError("Eine Liste einzulagernder Waren darf nicht leer sein!")
        lagerbestand = self.prüfe_Bestand()
        for teil in waren:
            lagerbestand[teil] += 50

    def nimm_aus_dem_Lager(self, waren, anzahl = 50):
        """Nimmt Waren aus der übergebenen Liste und füllt das Lager um eine gegebene Anzahl nach. Diese beträgt per
        Default 50."""
        if anzahl <= 0 or anzahl >= 51:
            raise ValueError("Es muss mindestens ein Stück der Ware aus dem Lager geholt werden bzw. nicht mehr als 50!")
        if waren == []:
            raise ValueError("Es können nur Waren aus dem Lager geholt werden, wenn sie gebraucht werden!")
        lagerbestand = self.prüfe_Bestand()
        geholte_waren = []
        for teil in waren:
            if teil not in list(lagerbestand.keys()):
                raise KeyError("Die Ware gibt es im Lager nicht.")
            if lagerbestand[teil] < anzahl:
                raise ValueError(f"Es sind nicht mehr genug Stück von {teil} eingelagert.")
            else:
                lagerbestand[teil] -= anzahl
                geholte_waren.append(teil)
        if geholte_waren == []:
            raise ValueError("Es können keine Waren geliefert werden, wenn sie im Lager nicht vorhanden sind!")
        return geholte_waren
