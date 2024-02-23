import Lager
from Lieferant import testpreisliste, testlagerarbeiter


class Lieferant:
    def __init__(self, name):
        self.__name = name

    def gibt_Name(self):
        return self.__name

    def erstellt_Rechnung(self, lieferung, anzahl = 50):
        if lieferung == []:
            raise ValueError("Es kann keine Rechnung erstellt werden, wenn die Lieferung leer ist!")
        if anzahl == 0:
            raise ValueError("Es kann keine Menge von 0 Zutaten geliefert werden!")
        rechnung = 0
        preisliste = testpreisliste.schaut_Preise_an()
        for teillieferung in lieferung:
            preis = preisliste[teillieferung]
            rechnung += preis * anzahl
        return rechnung

    def erfüllt_Lieferung(self, bestellung):
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht erfüllt werden.")
        fertige_lieferung = testlagerarbeiter.stellt_Lieferung_zusammen(bestellung)
        Lager.testbestand.wird_gelagert(fertige_lieferung)
        rechnung = self.erstellt_Rechnung(fertige_lieferung)
        print(f"Die bestellte Lieferung kostet {rechnung} €.")
        return rechnung
