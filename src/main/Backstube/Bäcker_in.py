import Lager
from src.main.Büro.Angestellte import Angestellte


class Bäcker_in(Angestellte):
    def __init__(self, name, lohn, lagerbestand, rezepte):
        self.lagerbestand = lagerbestand
        self.rezepte = rezepte
        super().__init__(name, lohn)

    def liefere_Backstücke(self, anforderung):
        if anforderung == []:
            raise ValueError("Es sollten keine Backstücke geliefert werden, wenn keine Anforderung besteht!")
        geholte_backwaren = self.lagerbestand.nimm_aus_dem_Lager(anforderung)
        if geholte_backwaren == []:
            raise ValueError("Es können nur dann Backwaren an die Auslage geliefert werden, wenn sie im Lager vorhanden sind.")
        return geholte_backwaren

    def ermittle_nachzufüllende_Backstücke(self):
        aufzufüllende_backstücke = self.lagerbestand.prüfe_fehlende_Waren()
        return aufzufüllende_backstücke

    def produziere_Backstück(self, backstücke):
        if backstücke == []:
            raise ValueError("Die Liste zu produzierender Backstücke sollte nicht leer sein!")
        fertig_gebacken = []
        for teil in backstücke:
            zutatenliste = self.rezepte.hole_Rezept(teil)
            self.hole_Zutaten(zutatenliste)
            fertig_gebacken.append(teil)
        return fertig_gebacken

    def hole_Zutaten(self, zutatenliste):
        if zutatenliste == []:
            raise ValueError("Die Zutatenliste kann nicht leer sein!")
        for zutat in zutatenliste:
            self.lagerbestand.nimm_aus_dem_Lager([zutat[0]], anzahl = zutat[1])

    def backe(self, bestellung = []):
        if bestellung == []:
            aufzufüllende_backstücke = self.ermittle_nachzufüllende_Backstücke()
        else:
            aufzufüllende_backstücke = bestellung
        if aufzufüllende_backstücke != []:
            neue_backstücke = self.produziere_Backstück(aufzufüllende_backstücke)
            self.lagerbestand.lagere_ein(neue_backstücke)
        else:
            raise ValueError(f"Im Moment gibt es keinen Bedarf für neue Backwaren.")
