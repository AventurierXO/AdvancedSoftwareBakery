from Lieferant import testlieferbestand


class Lagerarbeiter:

    def stellt_Lieferung_zusammen(self, bestellung):
        if bestellung == []:
            raise ValueError("Eine zu erfüllende Bestellung kann nicht leer sein!")
        lieferung = []
        lieferbestand = testlieferbestand.prüft_bestand()
        for ware in bestellung:
            if ware not in lieferbestand:
                raise ValueError("In der Bestellung darf sich keine Ware befinden, die der Lieferant nicht verkauft!")
            lieferung.append(ware)
        print(f"Der Lagerarbeiter der Lieferung hat die Bestellung zusammengestellt: {lieferung}")
        return lieferung
