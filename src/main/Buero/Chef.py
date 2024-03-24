from Auslage.Verkaeufer import Verkaeufer
from Backstube.Baecker import Baecker
from src.main.Buero.Angestellte import Angestellte

class Chef(Angestellte):
    def __init__(self, name, lohn, lagerbestand, lieferant, angestellte):
        self.lagerbestand = lagerbestand
        self.lieferant = lieferant
        self.angestellte = angestellte
        super().__init__(name, lohn)

    def aendere_lohn_mitarbeiter(self, mitarbeiter, lohnaenderung):
        """Der Lohn eines Mitarbeiters wird auf den uebergebenen Betrag geaendert."""
        if lohnaenderung <= 0:
            raise ValueError("Der Lohn kann nicht kleiner oder gleich 0 sein.")
        mitarbeiter.aendere_lohn(lohnaenderung)

    def bestelle_zutaten(self):
        """Eine Bestellung von Zutaten wird an den Lieferanten uebergeben und bezahlt."""
        bestellung = self.erstelle_bestellung()
        rechnung = self.lieferant.erfuelle_lieferung(bestellung, self.lagerbestand)
        self.bezahle_rechnung(rechnung)

    def erstelle_bestellung(self):
        """Wenn im Lager weniger als 50 von einer Zutat vorhanden sind, werden diese in eine Liste aufgenommen."""
        bestellung = self.lagerbestand.pruefe_fehlende_waren(back = False)
        if bestellung == []:
            raise ValueError("Im Moment muessen keine Zutaten nachbestellt werden.")
        return bestellung

    def bezahle_rechnung(self, rechnung):
        """Eine ausstehende Rechnung wird bezahlt."""
        if rechnung <= 0:
            raise ValueError("Die Rechnung muss groesser gleich 0 sein!")
        geldbetrag = rechnung
        self.lieferant.kassiere_geld_ein(geldbetrag)

    def stelle_an(self, name, lohn, position, auslage, kasse, kaffeemaschine, lagerbestand, rezepte):
        """Ein neuer Mitarbeiter wird angelegt und in das Angestellten-Verzeichnis aufgenommen."""
        if name in list(self.angestellte.keys()):
            raise KeyError("Es koennen keine zwei Angestellte denselben Namen haben! Bitte pruefen, ob der/die Angestellte bereits angelegt ist oder Namen durch Zahl ergaenzen!")
        if position == "Baecker":
            neuer_angestellter = Baecker(name, lohn, lagerbestand, rezepte)
        if position == "Verkaeufer":
            neuer_angestellter = Verkaeufer(name, lohn, auslage, kasse, kaffeemaschine)
        self.angestellte.update({neuer_angestellter.gebe_namen_an() : (neuer_angestellter.gebe_lohn_an(), type(neuer_angestellter).__name__)})

    def kuendige(self, angestellter):
        """Ein Mitarbeiter wird aus dem Angestellten-Verzeichnis geloescht."""
        self.angestellte.pop(angestellter.gebe_namen_an())