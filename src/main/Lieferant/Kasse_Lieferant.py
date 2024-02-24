from Auslage.Kasse import Kasse

class Kasse_Lieferant(Kasse):
    def __init__(self, geld, preisliste):
        super().__init__(geld, preisliste)

    def erstellt_Rechnung(self, lieferung):
        if lieferung == []:
            raise ValueError("Es kann keine Rechnung erstellt werden, wenn die Lieferung leer ist!")
        rechnung = 0
        preisliste_check = self.preisliste.prüf_Preisliste()
        for teillieferung in lieferung:
            preis = preisliste_check[teillieferung]
            rechnung += preis * 50
        return rechnung
