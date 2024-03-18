from Auslage.Verkäufer_in import Verkäufer_in
from Backstube.Bäcker_in import Bäcker_in
from src.main.Büro.Angestellte import Angestellte

class Chef(Angestellte):
    def __init__(self, name, lohn, lagerbestand, lieferant, angestellte):
        self.lagerbestand = lagerbestand
        self.lieferant = lieferant
        self.angestellte = angestellte
        super().__init__(name, lohn)

    def ändere_Lohn_Mitarbeiter(self, mitarbeiter, lohnänderung):
        """Der Lohn eines Mitarbeiters wird auf den übergebenen Betrag geändert."""
        if lohnänderung <= 0:
            raise ValueError(f"Der Lohn kann nicht kleiner oder gleich 0 sein.")
        mitarbeiter.ändere_Lohn(lohnänderung)

    def bestelle_Zutaten(self):
        """Eine Bestellung von Zutaten wird an den Lieferanten übergeben und bezahlt."""
        bestellung = self.Bestellung_erstellen()
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht an den Lieferanten überstellt werden!")
        rechnung = self.lieferant.erfülle_Lieferung(bestellung, self.lagerbestand)
        self.bezahlt_Rechnung(rechnung)

    def Bestellung_erstellen(self):
        """Wenn im Lager weniger als 50 von einer Zutat vorhanden sind, werden diese in eine Liste aufgenommen."""
        bestellung = self.lagerbestand.prüfe_fehlende_Waren(back = False)
        if bestellung == []:
            raise ValueError(f"Im Moment müssen keine Zutaten nachbestellt werden.")
        return bestellung

    def bezahlt_Rechnung(self, rechnung):
        """Eine ausstehende Rechnung wird bezahlt."""
        if rechnung <= 0:
            raise ValueError("Die Rechnung muss größer gleich 0 sein!")
        geldbetrag = rechnung
        self.lieferant.kassiere_Geld_ein(geldbetrag)

    def stelle_an(self, name, lohn, position, auslage, kasse, kaffeemaschine, lagerbestand, rezepte):
        """Ein neuer Mitarbeiter wird angelegt und in das Angestellten-Verzeichnis aufgenommen."""
        if name in list(self.angestellte.keys()):
            raise KeyError("Es können keine zwei Angestellte denselben Namen haben! Bitte prüfen, ob der/die Angestellte bereits angelegt ist oder Namen durch Zahl ergänzen!")
        if position == "Bäcker_in":
            neuer_angestellter = Bäcker_in(name, lohn, lagerbestand, rezepte)
        if position == "Verkäufer_in":
            neuer_angestellter = Verkäufer_in(name, lohn, auslage, kasse, kaffeemaschine)
        self.angestellte.update({neuer_angestellter.gebe_Namen_an() : (neuer_angestellter.gebe_Lohn_an(), type(neuer_angestellter).__name__)})

    def kündige(self, angestellter):
        """Ein Mitarbeiter wird aus dem Angestellten-Verzeichnis gelöscht."""
        self.angestellte.pop(angestellter.gebe_Namen_an())