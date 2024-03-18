from src.main import Lager
from src.main import Lieferant

class Lieferant:
    def __init__(self, name, lagerarbeiter, lieferbestand, kasse):
        self.__name = name
        self.lieferbestand = lieferbestand
        self.lagerarbeiter = lagerarbeiter
        self.kasse = kasse

    def gibt_Namen_an(self):
        return self.__name

    def erfülle_Lieferung(self, bestellung, lagerbestand):
        """Der Lieferant erfüllt die Bestellung durch das Zusammenstellen einer Lieferung, Erstellung einer Rechnung
        und Lieferung an die Bäckerei."""
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht erfüllt werden.")
        fertige_lieferung = self.lagerarbeiter.stelle_Lieferung_zusammen(bestellung)
        lagerbestand.lagere_ein(fertige_lieferung)
        rechnung = self.kasse.erstelle_Rechnung_Lieferung(fertige_lieferung)
        return rechnung

    def kassiere_Geld_ein(self, geld):
        self.kasse.zahle_Geld_ein(geld)