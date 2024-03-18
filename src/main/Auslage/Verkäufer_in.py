from src.main import Auslage
from src.main.Büro.Angestellte import Angestellte


class Verkäufer_in(Angestellte):
    def __init__(self, name, lohn, auslage, kasse, kaffeemaschine):
        self.auslage = auslage
        self.kasse = kasse
        self.kaffeemaschine= kaffeemaschine
        super().__init__(name, lohn)

    def kassiere_Geld_ein(self, rechnung, kunde):
        """Von dem Kunden wird der Betrag in Höhe der übergebenen Rechnung verlangt."""
        if rechnung <= 0:
            raise ValueError("Der zu bezahlende Betrag kann nicht kleiner oder gleich 0 sein!")
        eingenommenes_geld = kunde.bezahlen(rechnung)
        return eingenommenes_geld

    def verkaufe_Backwaren(self, bestellung, kunde):
        """Der Verkäufer nimmt die Bestellung des Kunden an und verkauft ihm die gewünschten Backwaren."""
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht verarbeitet werden!")
        zu_bezahlen = 0
        fertige_wunschbackwaren = self.auslage.entnehme_Backwerk(bestellung)
        zu_bezahlen += self.kasse.erstelle_Rechnung(fertige_wunschbackwaren)
        if zu_bezahlen == 0:
            raise ValueError("Der Verkauf kann nicht bezahlt werden, weil keine der gewünschten Waren da ist.")
        eingenommenes_geld = self.kassiere_Geld_ein(zu_bezahlen, kunde)
        self.kasse.zahle_Geld_ein(eingenommenes_geld)

    def verkaufe_Getränke(self, bestellung, kunde):
        """Der Verkäufer nimmt die Bestellung des Kunden an und verkauft ihm die gewünschten Getränke."""
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht verarbeitet werden!")
        zu_bezahlen = 0
        fertige_wunschgetränke = self.kaffeemaschine.mache_Getränk(bestellung)
        zu_bezahlen += self.kasse.erstelle_Rechnung(fertige_wunschgetränke)
        eingenommenes_geld = self.kassiere_Geld_ein(zu_bezahlen, kunde)
        self.kasse.zahle_Geld_ein(eingenommenes_geld)

    def bestelle_Backwaren_nach(self, bäcker):
        """Es werden fehlende Backwaren aufgenommen und als Bestellung an einen Bäcker überreicht, der diese aus dem
        Lager nachliefert. Die gelieferten Backwaren werden dann in die Auslage gelegt."""
        fehlende_backwaren = self.auslage.erfasse_fehlende_Backwaren()
        if fehlende_backwaren == []:
            raise ValueError("Es sind noch genug Backstücke von jeder Sorte vorhanden.")
        geholte_backwaren = bäcker.liefere_Backstücke(fehlende_backwaren)
        self.auslage.fülle_Bestand_nach(geholte_backwaren)
