from src.main import Lager
from src.main import Lieferant

class Lieferant:
    """
    Eine Klasse, die den Lieferanten repräsentiert

    Attribute:
    ----------
    name: String
        ein String, der den Namen des Lieferunternehmens enthält
    lagerarbeiter: Objekt der Klasse Lagerarbeiter
        ein für das Lieferunternehmen arbeitender Lagerarbeiter
    lieferbestand: Objekt der Klasse Lieferbestand
        ein dem Lieferunternehmen zugeordneter Lieferbestand
    kasse: Objekt der Klasse KasseLieferant
        eine Kasse, die dem Lieferunternehmen zugeordnet ist
    """
    def __init__(self, name, lagerarbeiter, lieferbestand, kasse):
        self.__name = name
        self.lieferbestand = lieferbestand
        self.lagerarbeiter = lagerarbeiter
        self.kasse = kasse

    def gebe_namen_an(self):
        return self.__name

    def erfuelle_lieferung(self, bestellung, lagerbestand):
        """Der Lieferant erfuellt die Bestellung durch das Zusammenstellen einer Lieferung, Erstellung einer Rechnung
        und Lieferung an die Baeckerei."""
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht erfuellt werden.")
        fertige_lieferung = self.lagerarbeiter.stelle_lieferung_zusammen(bestellung)
        lagerbestand.lagere_ein(fertige_lieferung)
        rechnung = self.kasse.erstelle_rechnung_lieferung(fertige_lieferung)
        return rechnung

    def kassiere_geld_ein(self, geld):
        """Der Lieferant nimmt einen Geldbetrag für eine erfüllte Bestellung an und zahlt sie in die Kasse ein."""
        if geld <= 0:
            raise ValueError("Der eingenommene Geldbetrag kann nicht kleiner gleich 0 sein!")
        self.kasse.zahle_geld_ein(geld)