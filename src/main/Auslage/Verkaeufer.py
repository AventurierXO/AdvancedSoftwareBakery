from src.main import Auslage
from src.main.Buero.Angestellte import Angestellte

class Verkaeufer(Angestellte):
    """
    Diese Klasse repräsentiert einen Verkäufer

    Attribute:
    ----------
    name: String
        der Name des Verkäufers
    lohn: Int
        der Lohn des Verkäufers
    auslage: Objekt der Klasse AuslageTresen
        die Auslage, aus der der Verkäufer die Waren verkauft
    kasse: Objekt der Klasse Kasse
        die dem Verkäufer zugeordnete Kasse
    kaffeemaschine: Objekt der Klasse Kaffeemaschine
        die dem Verkäufer zugeordnete Kaffeemaschine
    """
    def __init__(self, name, lohn, auslage, kasse, kaffeemaschine):
        self.auslage = auslage
        self.kasse = kasse
        self.kaffeemaschine= kaffeemaschine
        super().__init__(name, lohn)

    def kassiere_geld_ein(self, rechnung, kunde):
        """Von dem Kunden wird der Betrag in Hoehe der uebergebenen Rechnung verlangt."""
        if rechnung <= 0:
            raise ValueError("Der zu bezahlende Betrag kann nicht kleiner oder gleich 0 sein!")
        eingenommenes_geld = kunde.bezahlen(rechnung)
        return eingenommenes_geld

    def verkaufe_backwaren(self, bestellung, kunde):
        """Der Verkaeufer nimmt die Bestellung des Kunden an und verkauft ihm die gewuenschten Backwaren."""
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht verarbeitet werden!")
        zu_bezahlen = 0
        fertige_wunschbackwaren = self.auslage.entnehme_backwerk(bestellung)
        zu_bezahlen += self.kasse.erstelle_rechnung(fertige_wunschbackwaren)
        eingenommenes_geld = self.kassiere_geld_ein(zu_bezahlen, kunde)
        self.kasse.zahle_geld_ein(eingenommenes_geld)

    def verkaufe_getraenke(self, bestellung, kunde):
        """Der Verkaeufer nimmt die Bestellung des Kunden an und verkauft ihm die gewuenschten Getraenke."""
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht verarbeitet werden!")
        zu_bezahlen = 0
        fertige_wunschgetraenke = self.kaffeemaschine.mache_getraenk(bestellung)
        zu_bezahlen += self.kasse.erstelle_rechnung(fertige_wunschgetraenke)
        eingenommenes_geld = self.kassiere_geld_ein(zu_bezahlen, kunde)
        self.kasse.zahle_geld_ein(eingenommenes_geld)

    def bestelle_backwaren_nach(self, baecker):
        """Es werden fehlende Backwaren aufgenommen und als Bestellung an einen Baecker ueberreicht, der diese aus dem
        Lager nachliefert. Die gelieferten Backwaren werden dann in die Auslage gelegt."""
        fehlende_backwaren = self.auslage.erfasse_fehlende_backwaren()
        if fehlende_backwaren == []:
            raise ValueError("Es sind noch genug Backstuecke von jeder Sorte vorhanden.")
        geholte_backwaren = baecker.liefere_backstuecke(fehlende_backwaren)
        self.auslage.fuelle_bestand_nach(geholte_backwaren)
