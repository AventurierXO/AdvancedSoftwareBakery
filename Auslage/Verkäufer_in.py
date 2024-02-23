import random

import Auslage
from Büro.Angestellte import Angestellte


class Verkäufer_in(Angestellte):
    def __init__(self, name, lohn):
        super().__init__(name, lohn)

    def erstelle_Rechnung(self, einkauf):
        preisliste = Auslage.preisliste.prüf_Preisliste()
        rechnung = 0
        if einkauf == []:
            raise ValueError("Der zu bezahlende Einkauf kann nicht leer sein!")
        for ware in einkauf:
            if ware[0] not in preisliste:
                raise KeyError(f"Die bestellte Ware {ware[0]} ist nicht in der Preisliste!")
            rechnung += ware[1] * preisliste[ware[0]]
        return rechnung

    def kassiere_Geld_ein(self, rechnung, kunde):
        if rechnung <= 0:
            raise ValueError("Der zu bezahlende Betrag kann nicht kleiner oder gleich 0 sein!")
        eingenommenes_geld = kunde.bezahlen(rechnung)
        return eingenommenes_geld

    def verkaufe_Backaren(self, bestellung, auslage, kasse, kunde):
        zu_bezahlen = 0
        fertige_wunschbackwaren = auslage.entnehme_Backwerk(bestellung)
        zu_bezahlen += self.erstelle_Rechnung(fertige_wunschbackwaren)
        if zu_bezahlen == 0:
            raise ValueError("Der Verkauf kann nicht bezahlt werden, weil keine der gewünschten Waren da ist.")
        rechnung = format(zu_bezahlen, ".2f")
        print(f"Der Preis für den Einkauf beträgt {rechnung} €.")
        eingenommenes_geld = self.kassiere_Geld_ein(zu_bezahlen, kunde)
        kasse.geld_einzahlen(eingenommenes_geld)

    def verkaufe_Getränke(self, bestellung, kaffeemaschine, kasse, kunde):
        zu_bezahlen = 0
        fertige_wunschgetränke = kaffeemaschine.macht_Getränk(bestellung)
        zu_bezahlen += self.erstelle_Rechnung(fertige_wunschgetränke)
        eingenommenes_geld = self.kassiere_Geld_ein(zu_bezahlen, kunde)
        kasse.geld_einzahlen(eingenommenes_geld)

    def Backwaren_nachbestellen(self, auslage, bäcker, lagerbestand):
        fehlende_backwaren = auslage.erfasst_fehlende_Backwaren()
        if fehlende_backwaren != []:
            geholte_backwaren = bäcker.liefert_Backstücke(fehlende_backwaren, lagerbestand)
            auslage.fülle_Bestand_nach(geholte_backwaren)
        else:
            print(f"Es sind noch genug Backstücke von jeder Sorte vorhanden.")
