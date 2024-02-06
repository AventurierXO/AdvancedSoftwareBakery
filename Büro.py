#Domain Büro

import Auslage, Auslage, Lager, Lieferant, Verkaufsraum, Backstube

class Angestellte:
    def __init__(self, name, lohn):
        self.__name = name
        self.__lohn = lohn

    def gibt_Namen_an(self):
        return self.__name

    def gibt_Lohn_an(self):
        return self.__lohn


class Chef(Angestellte):

    def prüft_Lohn(self):
        return self.__lohn

    def ändert_lohn(self, mitarbeiter, lohnänderung):
        print(f"Der bisherige Lohn beträgt {mitarbeiter.gibt_Lohn_an()} €.")
        if lohnänderung < 0:
            print(f"Der Lohn kann nicht kleiner als 0 sein.")
        else:
            mitarbeiter.__lohn = lohnänderung
            print(f"Der Lohn wurde auf {lohnänderung} € geändert.")

    def Mitarbeiter_einstellen(self, name, position, lohn):
        mitarbeiter = position(name, lohn)
        print(f"Mitarbeiter/in {name} wurde als {mitarbeiter} angelegt.")

    def check_Lager(self):
        lager = Lager.testbestand.prüft_Bestand()
        return lager

    def bestellt_Zutaten(self):
        lager = self.check_Lager()
        bestellung = self.Bestellung_erstellen(lager)
        if bestellung != []:
            rechnung = Lieferant.testlieferant.erfüllt_Lieferung(bestellung)
            self.bezahlt_rechnung(rechnung)

    def Bestellung_erstellen(self, lager):
        bestellung = []
        zutaten = ("Mehl", "Zucker", "Milch", "Eier", "Glasur", "Hefe", "Streusel")
        for ware in zutaten:
            if lager[ware] < 50:
                bestellung.append(ware)
        if bestellung == []:
            print(f"Im Moment müssen keine Zutaten nachbestellt werden.")
        else:
            print(f"Der Chef hat eine Bestellung für folgende Waren erstellt: {bestellung}")
        return bestellung

    def bezahlt_rechnung(self, rechnung):
        print(f"Es werden {rechnung} € vom Chef and das Lieferunternehmen überwiesen.")


class Verkäufer_in(Angestellte):
    def geld_zählen(self):
        print(Auslage.kasse.geld_in_kasse())

    def prüft_Auslage(self):
        auslage = Auslage.auslage.prüf_Bestand()
        return auslage

    def füllt_Auslage_nach(self):
        auslage = self.prüft_Auslage()
        nachfüllliste = []
        for key in auslage:
            if auslage[key] == 0:
                nachfüllliste.append(key)
        return nachfüllliste

    def erstelle_Rechnung(self, einkauf):
        preisliste = Auslage.preisliste.prüf_Preisliste()
        sum = 0
        for ware in einkauf:
            sum += ware[1] * preisliste[ware[0]]
            rechnung = format(sum, ".2f")
        print(f"Der Preis für den Einkauf beträgt {rechnung} €.")
        return rechnung

    def kassiere_Geld_ein(self, rechnung, kunde):
        print(f"Das macht dann {rechnung} €, bitte.")
        eingenommenes_geld = kunde.bezahlen(rechnung)
        return eingenommenes_geld

    def verkaufe_Waren(self, auslage, kasse, kunde):
        # nehme Wünsche des Kunden auf
        wunschwaren = kunde.kauft_Backwaren(auslage)
        einkauf = auslage.entnehme_Backwerk(wunschwaren)
        rechnung = self.erstelle_Rechnung(einkauf)
        eingenommenes_geld = self.kassiere_Geld_ein(rechnung, kunde)
        kasse.geld_einzahlen(eingenommenes_geld)
        print(f"Vielen Dank für den Einkauf. Ich wünsche einen schönen Tag.")

    def gibt_Bestellung_weiter(self, bestellung, bäcker):
        bäcker.nimmt_Bestellung_an(bestellung)
        print(f"Die Bestellung wurde an {bäcker} übergeben.")

    def nimmt_Backlieferung_entgegen(self, bäcker):
        lieferung = bäcker.liefert_Backstücke()
        return lieferung


    def Backwaren_nachbestellen(self, auslage, bäcker, lagerbestand):
        check_backwaren = auslage.erfasst_fehlende_Backwaren()
        if check_backwaren != []:
            geholte_backwaren = bäcker.liefert_Backstücke(check_backwaren, lagerbestand)
            auslage.fülle_Bestand_nach(geholte_backwaren)
        else:
            print(f"Es sind noch Backstücke von jeder Sorte vorhanden.")

class Bäcker_in(Angestellte):

    def holt_Zutaten(self):
        # holt benötigte Zutaten aus dem Lager, sofern diese vorhanden sind
        pass

    def backen(self, backwerk):
        # backt ein bestimmtes Backwerk
        pass

    def liefert_Backstücke(self, anforderung,lagerbestand):
        geholte_backwaren = lagerbestand.wird_aus_dem_Lager_genommen(anforderung)
        print(f"Folgende Backwaren werden zum Verkaufstresen gebracht: {geholte_backwaren}")
        return geholte_backwaren

    def nimmt_Bestellung_an(self, bestellung):
        print(f"Bäcker_in {self.gibt_Namen_an()} hat die Bestellung behalten und bearbeitet sie nun.")
        self.bearbeitet_Bestellung(bestellung)

    def bearbeitet_Bestellung(self, bestellung):
        fertige_bestellung = {}
        for teilbestellung in bestellung:
            self.backen(teilbestellung)
            fertige_bestellung.update({f"{teilbestellung[0]}": teilbestellung[1]})
        # bringt fertige Bestellung ins Lager bis sie abgeholt wird

    def ermittelt_nachzufüllende_backstücke(self):
        backstücke = ("Weizensemmel", "Kürbiskernbrötchen", "Roggenmischbrot", "Vollkornbrot", \
                      "Dinkelbrot", "Croissant", "Streuselkuchen", "Bienenstich", "Pfannkuchen")
        aufzufüllende_backstücke = []
        for backwerk in backstücke:
            if Lager.lagerbestand[backwerk] < 50:
                aufzufüllende_backstücke.append(backwerk)
        return aufzufüllende_backstücke
    def backt(self):
        aufzufüllende_backstücke = self.ermittelt_nachzufüllende_backstücke()


testchef = Chef("Jana", 4000)
testverkäufer = Verkäufer_in("Alexander", 2000)
testbäcker = Bäcker_in("Linda", 3000)