class Lagerbestand:
    def __init__(self, bestand):
        self.__bestand = bestand

    def pruefe_bestand(self):
        return self.__bestand

    def pruefe_fehlende_waren(self, back = True):
        """Wenn weniger als 50 Stueck von einer Ware vorhanden sind, wird diese aufgenommen. Wenn back == True ist,
        dann werden fehlende Backwaren ermittelt. Wenn back == False ist, dann werden fehlende Zutaten ermittelt."""
        aufzufuellende_waren = []
        bestand = self.pruefe_bestand()
        if back == True:
            backstuecke = ("Weizensemmel", "Kuerbiskernbroetchen", "Roggenmischbrot", "Vollkornbrot", \
                          "Dinkelbrot", "Croissant", "Streuselkuchen", "Bienenstich", "Pfannkuchen")
            zu_checken = backstuecke
        else:
            zutaten = ["Mehl", "Zucker", "Milch", "Eier", "Hefe", "Wasser", "Butter", "Kuerbiskerne"]
            zu_checken = zutaten
        for ware in zu_checken:
            if bestand[ware] < 50:
                aufzufuellende_waren.append(ware)
        return aufzufuellende_waren

    def lagere_ein(self, waren):
        """Eine Liste von Waren wird im Lager um 50 Stueck nachgefuellt."""
        if waren == []:
            raise ValueError("Eine Liste einzulagernder Waren darf nicht leer sein!")
        lagerbestand = self.pruefe_bestand()
        for teil in waren:
            if teil not in list(lagerbestand.keys()):
                raise KeyError("Die Ware gibt es im Lager nicht.")
            lagerbestand[teil] += 50

    def nimm_aus_dem_lager(self, waren, anzahl = 50):
        """Nimmt Waren aus der uebergebenen Liste und fuellt das Lager um eine gegebene Anzahl nach. Diese betraegt per
        Default 50."""
        if anzahl <= 0 or anzahl >= 51:
            raise ValueError("Es muss mindestens ein Stueck der Ware aus dem Lager geholt werden bzw. nicht mehr als 50!")
        if waren == []:
            raise ValueError("Es koennen nur Waren aus dem Lager geholt werden, wenn sie gebraucht werden!")
        lagerbestand = self.pruefe_bestand()
        geholte_waren = []
        for teil in waren:
            if teil not in list(lagerbestand.keys()):
                raise KeyError("Die Ware gibt es im Lager nicht.")
            if lagerbestand[teil] < anzahl:
                raise ValueError(f"Es sind nicht mehr genug Stueck von {teil} eingelagert.")
            else:
                lagerbestand[teil] -= anzahl
                geholte_waren.append(teil)
        if geholte_waren == []:
            raise ValueError("Es koennen keine Waren geliefert werden, wenn sie im Lager nicht vorhanden sind!")
        return geholte_waren
