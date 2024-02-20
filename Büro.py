#Domain Büro

import Auslage, Lager, Lieferant, Verkaufsraum, Backstube
import random

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
        zutaten = ("Mehl", "Zucker", "Milch", "Eier", "Hefe", "Wasser", "Butter")
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
        rechnung = 0
        for ware in einkauf:
            rechnung += ware[1] * preisliste[ware[0]]
        return rechnung

    def kassiere_Geld_ein(self, rechnung, kunde):
        eingenommenes_geld = kunde.bezahlen(rechnung)
        return eingenommenes_geld

    def verkaufe_Waren(self, auslage, kaffeemaschine, kasse, kunde):
        # nehme Wünsche des Kunden auf
        back = random.randint(0, 1)
        getränk = random.randint(0, 1)
        zu_bezahlen = 0
        if back == 1 or getränk == 0:
            wunschbackwaren = kunde.kauft_Backwaren(auslage)
            fertige_wunschbackwaren = auslage.entnehme_Backwerk(wunschbackwaren)
            zu_bezahlen += self.erstelle_Rechnung(fertige_wunschbackwaren)
        if getränk == 1:
            wunschgetränke = kunde.kauft_Heißgetränk(kaffeemaschine)
            fertige_wunschgetränke = kaffeemaschine.macht_Getränk(wunschgetränke)
            zu_bezahlen += self.erstelle_Rechnung(fertige_wunschgetränke)
        rechnung = format(zu_bezahlen, ".2f")
        print(f"Der Preis für den Einkauf beträgt {rechnung} €.")
        eingenommenes_geld = self.kassiere_Geld_ein(rechnung, kunde)
        kasse.geld_einzahlen(eingenommenes_geld)

    def gibt_Bestellung_weiter(self, bestellung, bäcker):
        bäcker.nimmt_Bestellung_an(bestellung)
        print(f"Die Bestellung wurde an {bäcker} übergeben.")

    def nimmt_Backlieferung_entgegen(self, bäcker):
        lieferung = bäcker.liefert_Backstücke()
        return lieferung

    def Backwaren_nachbestellen(self, auslage, bäcker, lagerbestand):
        fehlende_backwaren = auslage.erfasst_fehlende_Backwaren()
        if fehlende_backwaren != []:
            geholte_backwaren = bäcker.liefert_Backstücke(fehlende_backwaren, lagerbestand)
            auslage.fülle_Bestand_nach(geholte_backwaren)
        else:
            print(f"Es sind noch genug Backstücke von jeder Sorte vorhanden.")

class Bäcker_in(Angestellte):

    def liefert_Backstücke(self, anforderung,lagerbestand):
        geholte_backwaren = lagerbestand.wird_aus_dem_Lager_genommen(anforderung)
        print(f"Folgende Backwaren werden zum Verkaufstresen gebracht: {geholte_backwaren}")
        return geholte_backwaren

    def nimmt_Bestellung_an(self, bestellung):
        print(f"Bäcker_in {self.gibt_Namen_an()} hat die Bestellung behalten und bearbeitet sie nun.")
        self.bearbeitet_Bestellung(bestellung)

    def bearbeitet_Bestellung(self, bestellung):
        fertige_bestellung = []
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

    def produziere_Backstück(self, backstücke):
        fertig_gebacken = []
        rezepte = Backstube.rezepte.schaut_Rezepte_an()
        for teil in backstücke:
            zutatenliste = self.holt_Rezept(teil, rezepte)
            self.holt_Zutaten(zutatenliste)
            fertig_gebacken.append(teil)
        return fertig_gebacken

    def holt_Rezept(self, backstück, rezepte):
        return rezepte[backstück]

    def holt_Zutaten(self, zutatenliste):
        for zutat in zutatenliste:
            Lager.testbestand.wird_aus_dem_Lager_genommen([zutat[0]], anzahl = zutat[1])
        print(f"Alle Zutaten wurden nun aus dem Lager genommen.")

    def backt(self, bestellung = []):
        if bestellung == []:
            aufzufüllende_backstücke = self.ermittelt_nachzufüllende_backstücke()
        else:
            aufzufüllende_backstücke = bestellung
        if aufzufüllende_backstücke != []:
            print(f"Folgende Backstücke müssen aufgefüllt werden: {aufzufüllende_backstücke}")
            neue_backstücke = self.produziere_Backstück(aufzufüllende_backstücke)
            Lager.testbestand.wird_gelagert(neue_backstücke)
            print(f"Der Backprozess wurde abgeschlossen.")
        else:
            print(f"Im Moment gibt es keinen Bedarf für neue Backwaren.")

testchef = Chef("Jana", 4000)
testverkäufer = Verkäufer_in("Alexander", 2000)
testbäcker = Bäcker_in("Linda", 3000)