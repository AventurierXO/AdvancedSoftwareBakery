from Auslage.Kasse import Kasse

class KasseLieferant(Kasse):
    """
    Diese Klasse repräsentiert die Kasse des Lieferanten

    Attribute:
    ----------
    geld: Integer
        Geldbetrag, der sich in der Kasse befindet
    preisliste: Objekt der Klasse PreislisteLieferant
        Waren im Angebot des Lieferanten und die zugehörigen Preise
    """
    def __init__(self, geld, preisliste):
        super().__init__(geld, preisliste)

    def erstelle_rechnung_lieferung(self, lieferung):
        """Fuer eine fertige Lieferung wird die Rechnung berechnet."""
        if lieferung == []:
            raise ValueError("Es kann keine Rechnung erstellt werden, wenn die Lieferung leer ist!")
        rechnung = 0
        preisliste_check = self.preisliste.pruefe_preisliste()
        for teillieferung in lieferung:
            preis = preisliste_check[teillieferung]
            rechnung += preis * 50
        return rechnung
