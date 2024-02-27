from src.main.Lieferant import Lieferbestand

class Lagerarbeiter:
    def __init__(self, lieferbestand):
        self.lieferbestand = lieferbestand

    def stelle_Lieferung_zusammen(self, bestellung):
        if bestellung == []:
            raise ValueError("Eine zu erfüllende Bestellung kann nicht leer sein!")
        lieferung = []
        lieferbestand = self.lieferbestand.prüfe_Bestand()
        for ware in bestellung:
            if ware not in lieferbestand:
                raise ValueError("In der Bestellung darf sich keine Ware befinden, die der Lieferant nicht verkauft!")
            lieferung.append(ware)
        return lieferung