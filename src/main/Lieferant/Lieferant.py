from src.main import Lager
from src.main import Lieferant

class Lieferant:
    def __init__(self, name, lagerarbeiter, lieferbestand, kasse):
        self.__name = name
        self.lieferbestand = lieferbestand
        self.lagerarbeiter = lagerarbeiter
        self.kasse = kasse

    def gibt_Name(self):
        return self.__name

    def erfüllt_Lieferung(self, bestellung, lagerbestand):
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht erfüllt werden.")
        fertige_lieferung = self.lagerarbeiter.stellt_Lieferung_zusammen(bestellung)
        lagerbestand.wird_gelagert(fertige_lieferung)
        rechnung = self.kasse.erstellt_Rechnung(fertige_lieferung)
        return rechnung

    def kassiere_Geld_ein(self, geld):
        self.kasse.geld_einzahlen(geld)