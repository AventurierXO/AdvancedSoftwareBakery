import Lager
from src.main.Buero.Angestellte import Angestellte


class Baecker(Angestellte):
    def __init__(self, name, lohn, lagerbestand, rezepte):
        self.lagerbestand = lagerbestand
        self.rezepte = rezepte
        super().__init__(name, lohn)

    def liefere_backstuecke(self, anforderung):
        """Der Baecker nimmt eine Anforderung von einem Verkaeufer an und holt die Backwaren aus dem Lager und gibt sie zurueck."""
        if anforderung == []:
            raise ValueError("Es sollten keine Backstuecke geliefert werden, wenn keine Anforderung besteht!")
        geholte_backwaren = self.lagerbestand.nimm_aus_dem_lager(anforderung)
        if geholte_backwaren == []:
            self.backe()
            raise ValueError("Es koennen nur dann Backwaren an die Auslage geliefert werden, wenn sie im Lager vorhanden sind.")
        return geholte_backwaren

    def ermittle_nachzufuellende_backstuecke(self):
        """Backwaren, die im Lager weniger als 50-mal vorhanden sind, werden aufgenommen."""
        aufzufuellende_backstuecke = self.lagerbestand.pruefe_fehlende_waren()
        return aufzufuellende_backstuecke

    def produziere_backstueck(self, backstuecke):
        """Backwaren, die in der uebergebenen Liste vorhanden sind, werden gebacken und zurueckgegeben."""
        if backstuecke == []:
            raise ValueError("Die Liste zu produzierender Backstuecke sollte nicht leer sein!")
        fertig_gebacken = []
        for teil in backstuecke:
            zutatenliste = self.rezepte.hole_rezept(teil)
            self.hole_zutaten(zutatenliste)
            fertig_gebacken.append(teil)
        return fertig_gebacken

    def hole_zutaten(self, zutatenliste):
        """Die in einer Liste uebergebenen Zutaten werden aus dem Lager geholt."""
        if zutatenliste == []:
            raise ValueError("Die Zutatenliste kann nicht leer sein!")
        for zutat in zutatenliste:
            self.lagerbestand.nimm_aus_dem_lager([zutat[0]], anzahl = zutat[1])

    def backe(self, bestellung = []):
        """Eine Bestellung oder im Lager fehlende Backwaren werden gebacken und eingelagert."""
        if bestellung == []:
            aufzufuellende_backstuecke = self.ermittle_nachzufuellende_backstuecke()
        else:
            aufzufuellende_backstuecke = bestellung
        if aufzufuellende_backstuecke == []:
            raise ValueError("Im Moment gibt es keinen Bedarf fuer neue Backwaren.")
        neue_backstuecke = self.produziere_backstueck(aufzufuellende_backstuecke)
        self.lagerbestand.lagere_ein(neue_backstuecke)
