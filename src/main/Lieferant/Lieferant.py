from src.main import Lager
from src.main import Lieferant

class Lieferant:
    def __init__(self, name, preisliste, lagerarbeiter, lieferbestand, kasse):
        self.__name = name
        self.preisliste = preisliste
        self.lieferbestand = lieferbestand
        self.lagerarbeiter = lagerarbeiter
        self.kasse = kasse

    def gibt_Name(self):
        return self.__name

    def erstellt_Rechnung(self, lieferung):
        if lieferung == []:
            raise ValueError("Es kann keine Rechnung erstellt werden, wenn die Lieferung leer ist!")
        rechnung = 0
        preisliste_check = self.preisliste.prüf_Preisliste()
        for teillieferung in lieferung:
            preis = preisliste_check[teillieferung]
            rechnung += preis * 50
        return rechnung

    def erfüllt_Lieferung(self, bestellung, lagerbestand):
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht erfüllt werden.")
        fertige_lieferung = self.lagerarbeiter.stellt_Lieferung_zusammen(bestellung)
        lagerbestand.wird_gelagert(fertige_lieferung)
        rechnung = self.erstellt_Rechnung(fertige_lieferung)
        return rechnung

    def kassiere_Geld_ein(self, geld):
        self.kasse.geld_einzahlen(geld)