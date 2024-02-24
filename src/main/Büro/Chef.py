from src.main.Büro.Angestellte import Angestellte

class Chef(Angestellte):
    def __init__(self, name, lohn, lagerbestand, lieferant):
        self.lagerbestand = lagerbestand
        self.lieferant = lieferant
        super().__init__(name, lohn)

    def ändert_lohn(self, mitarbeiter, lohnänderung):
        if lohnänderung <= 0:
            raise ValueError(f"Der Lohn kann nicht kleiner oder gleich 0 sein.")
        mitarbeiter.ändere_Lohn(lohnänderung)

    def bestellt_Zutaten(self):
        bestellung = self.Bestellung_erstellen()
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht an den Lieferanten überstellt werden!")
        rechnung = self.lieferant.erfüllt_Lieferung(bestellung, self.lagerbestand)
        self.bezahlt_Rechnung(rechnung)

    def Bestellung_erstellen(self):
        bestellung = self.lagerbestand.prüft_fehlende_Waren(back = False)
        if bestellung == []:
            raise ValueError(f"Im Moment müssen keine Zutaten nachbestellt werden.")
        return bestellung

    def bezahlt_Rechnung(self, rechnung):
        if rechnung <= 0:
            raise ValueError("Die Rechnung muss größer gleich 0 sein!")
        self.lieferant.kassiere_Geld_ein(rechnung)

