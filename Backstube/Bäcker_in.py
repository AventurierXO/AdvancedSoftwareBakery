import Backstube
from Büro.Angestellte import Angestellte


class Bäcker_in(Angestellte):
    def __init__(self, name, lohn):
        super().__init__(name, lohn)

    def __init__(self, name, lohn):
        super().__init__(name, lohn)

    def liefert_Backstücke(self, anforderung,lagerbestand):
        if anforderung == []:
            raise ValueError("Es sollten keine Backstücke geliefert werden, wenn keine Anforderung besteht!")
        geholte_backwaren = lagerbestand.wird_aus_dem_Lager_genommen(anforderung)
        if geholte_backwaren == []:
            raise ValueError("Es können nur dann Backwaren an die Auslage geliefert werden, wenn sie im Lager vorhanden sind.")
        print(f"Folgende Backwaren werden zum Verkaufstresen gebracht: {geholte_backwaren}")
        return geholte_backwaren

    def ermittelt_nachzufüllende_backstücke(self, lagerbestand):
        aufzufüllende_backstücke = lagerbestand.prüft_fehlende_Waren(lagerbestand)
        return aufzufüllende_backstücke

    def produziere_Backstück(self, backstücke, lagerbestand):
        if backstücke == []:
            raise ValueError("Die Liste zu produzierender Backstücke sollte nicht leer sein!")
        fertig_gebacken = []
        for teil in backstücke:
            zutatenliste = Backstube.rezepte.holt_Rezept(teil)
            self.holt_Zutaten(zutatenliste, lagerbestand)
            fertig_gebacken.append(teil)
        return fertig_gebacken

    def holt_Zutaten(self, zutatenliste, lagerbestand):
        for zutat in zutatenliste:
            lagerbestand.wird_aus_dem_Lager_genommen([zutat[0]], anzahl = zutat[1])
        print(f"Alle Zutaten wurden nun aus dem Lager genommen.")

    def backt(self, lagerbestand, bestellung = []):
        if bestellung == []:
            aufzufüllende_backstücke = self.ermittelt_nachzufüllende_backstücke(lagerbestand)
        else:
            aufzufüllende_backstücke = bestellung
        if aufzufüllende_backstücke != []:
            print(f"Folgende Backstücke müssen aufgefüllt werden: {aufzufüllende_backstücke}")
            neue_backstücke = self.produziere_Backstück(aufzufüllende_backstücke, lagerbestand)
            lagerbestand.wird_gelagert(neue_backstücke)
            print(f"Der Backprozess wurde abgeschlossen.")
        else:
            print(f"Im Moment gibt es keinen Bedarf für neue Backwaren.")
