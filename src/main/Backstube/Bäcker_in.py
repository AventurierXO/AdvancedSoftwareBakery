import Lager
from src.main.Büro.Angestellte import Angestellte


class Bäcker_in(Angestellte):
    def __init__(self, name, lohn, lagerbestand, rezepte):
        self.lagerbestand = lagerbestand
        self.rezepte = rezepte
        super().__init__(name, lohn)

    def liefert_Backstücke(self, anforderung):
        if anforderung == []:
            raise ValueError("Es sollten keine Backstücke geliefert werden, wenn keine Anforderung besteht!")
        geholte_backwaren = self.lagerbestand.wird_aus_dem_Lager_genommen(anforderung)
        if geholte_backwaren == []:
            raise ValueError("Es können nur dann Backwaren an die Auslage geliefert werden, wenn sie im Lager vorhanden sind.")
        return geholte_backwaren

    def ermittelt_nachzufüllende_backstücke(self):
        aufzufüllende_backstücke = self.lagerbestand.prüft_fehlende_Waren()
        return aufzufüllende_backstücke

    def produziere_Backstück(self, backstücke):
        if backstücke == []:
            raise ValueError("Die Liste zu produzierender Backstücke sollte nicht leer sein!")
        fertig_gebacken = []
        for teil in backstücke:
            zutatenliste = self.rezepte.holt_Rezept(teil)
            self.holt_Zutaten(zutatenliste)
            fertig_gebacken.append(teil)
        return fertig_gebacken

    def holt_Zutaten(self, zutatenliste):
        if zutatenliste == []:
            raise ValueError("Die Zutatenliste kann nicht leer sein!")
        for zutat in zutatenliste:
            self.lagerbestand.wird_aus_dem_Lager_genommen([zutat[0]], anzahl = zutat[1])

    def backt(self, bestellung = []):
        if bestellung == []:
            aufzufüllende_backstücke = self.ermittelt_nachzufüllende_backstücke(self.lagerbestand)
        else:
            aufzufüllende_backstücke = bestellung
        if aufzufüllende_backstücke != []:
            neue_backstücke = self.produziere_Backstück(aufzufüllende_backstücke)
            self.lagerbestand.wird_gelagert(neue_backstücke)
        else:
            raise ValueError(f"Im Moment gibt es keinen Bedarf für neue Backwaren.")
