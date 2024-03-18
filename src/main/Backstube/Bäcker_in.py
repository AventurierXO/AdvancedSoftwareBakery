import Lager
from src.main.Büro.Angestellte import Angestellte


class Bäcker_in(Angestellte):
    def __init__(self, name, lohn, lagerbestand, rezepte):
        self.lagerbestand = lagerbestand
        self.rezepte = rezepte
        super().__init__(name, lohn)

    def liefere_Backstücke(self, anforderung):
        """Der Bäcker nimmt eine Anforderung von einem Verkäufer an und holt die Backwaren aus dem Lager und gibt sie zurück."""
        if anforderung == []:
            raise ValueError("Es sollten keine Backstücke geliefert werden, wenn keine Anforderung besteht!")
        geholte_backwaren = self.lagerbestand.nimm_aus_dem_Lager(anforderung)
        if geholte_backwaren == []:
            self.backe()
            raise ValueError("Es können nur dann Backwaren an die Auslage geliefert werden, wenn sie im Lager vorhanden sind.")
        return geholte_backwaren

    def ermittle_nachzufüllende_Backstücke(self):
        """Backwaren, die im Lager weniger als 50-mal vorhanden sind, werden aufgenommen."""
        aufzufüllende_backstücke = self.lagerbestand.prüfe_fehlende_Waren()
        return aufzufüllende_backstücke

    def produziere_Backstück(self, backstücke):
        """Backwaren, die in der übergebenen Liste vorhanden sind, werden gebacken und zurückgegeben."""
        if backstücke == []:
            raise ValueError("Die Liste zu produzierender Backstücke sollte nicht leer sein!")
        fertig_gebacken = []
        for teil in backstücke:
            zutatenliste = self.rezepte.hole_Rezept(teil)
            self.hole_Zutaten(zutatenliste)
            fertig_gebacken.append(teil)
        return fertig_gebacken

    def hole_Zutaten(self, zutatenliste):
        """Die in einer Liste übergebenen Zutaten werden aus dem Lager geholt."""
        if zutatenliste == []:
            raise ValueError("Die Zutatenliste kann nicht leer sein!")
        for zutat in zutatenliste:
            self.lagerbestand.nimm_aus_dem_Lager([zutat[0]], anzahl = zutat[1])

    def backe(self, bestellung = []):
        """Eine Bestellung oder im Lager fehlende Backwaren werden gebacken und eingelagert."""
        if bestellung == []:
            aufzufüllende_backstücke = self.ermittle_nachzufüllende_Backstücke()
        else:
            aufzufüllende_backstücke = bestellung
        if aufzufüllende_backstücke == []:
            raise ValueError(f"Im Moment gibt es keinen Bedarf für neue Backwaren.")
        neue_backstücke = self.produziere_Backstück(aufzufüllende_backstücke)
        self.lagerbestand.lagere_ein(neue_backstücke)
