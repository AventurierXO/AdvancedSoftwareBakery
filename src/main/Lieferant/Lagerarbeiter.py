from src.main.Lieferant import Lieferbestand

class Lagerarbeiter:
    def __init__(self, lieferbestand):
        self.lieferbestand = lieferbestand

    def stelle_lieferung_zusammen(self, bestellung):
        """Aus der Bestellung wird die Lieferung zusammengestellt."""
        if bestellung == []:
            raise ValueError("Eine zu erfuellende Bestellung kann nicht leer sein!")
        lieferung = []
        lieferbestand = self.lieferbestand.pruefe_bestand()
        for ware in bestellung:
            if ware not in lieferbestand:
                raise KeyError("In der Bestellung darf sich keine Ware befinden, die der Lieferant nicht verkauft!")
            lieferung.append(ware)
        return lieferung