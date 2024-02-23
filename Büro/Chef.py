import Lieferant
from Büro.Angestellte import Angestellte


class Chef(Angestellte):
    def __init__(self, name, lohn):
        super().__init__(name, lohn)

    def ändert_lohn(self, mitarbeiter, lohnänderung):
        print(f"Der bisherige Lohn beträgt {mitarbeiter.gibt_Lohn_an()} €.")
        if lohnänderung <= 0:
            raise ValueError(f"Der Lohn kann nicht kleiner oder gleich 0 sein.")
        mitarbeiter.ändere_Lohn(lohnänderung)
        print(f"Der Lohn wurde auf {mitarbeiter.gibt_Lohn_an()} € geändert.")

    def bestellt_Zutaten(self, lagerbestand):
        bestellung = self.Bestellung_erstellen(lagerbestand)
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht an den Lieferanten überstellt werden!")
        rechnung = Lieferant.testlieferant.erfüllt_Lieferung(bestellung)
        self.bezahlt_rechnung(rechnung)

    def Bestellung_erstellen(self, lagerbestand):
        bestellung = lagerbestand.prüft_fehlende_Waren(lagerbestand, back = False)
        if bestellung == []:
            print(f"Im Moment müssen keine Zutaten nachbestellt werden.")
        else:
            print(f"Der Chef hat eine Bestellung für folgende Waren erstellt: {bestellung}")
        return bestellung

    def bezahlt_rechnung(self, rechnung):
        print(f"Es werden {rechnung} € vom Chef and das Lieferunternehmen überwiesen.")
