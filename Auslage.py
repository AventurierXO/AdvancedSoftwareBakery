#Domain Auslage/Thresen

import Backstube

class Auslage_Thresen:
    def __init__(self, auslage):
        self.__auslage = auslage

    def prüf_Bestand(self):
        return self.__auslage

    def schaue_Waren_an(self):
        return list(self.__auslage.keys())

    def erfasst_fehlende_Backwaren(self):
        auslage = self.prüf_Bestand()
        fehlende_backwaren = []
        for backware in auslage:
            if auslage[backware] == 0:
                fehlende_backwaren.append(backware)
        return fehlende_backwaren

    def entnehme_Backwerk(self, wunschwaren):
        einkauf = []
        auslage = self.prüf_Bestand()
        for teilbestellung in wunschwaren:
            backware = teilbestellung[0]
            anzahl = teilbestellung[1]
            if auslage[backware] <= anzahl:
                print(f"{backware} ist leider ausverkauft.")
            else:
                auslage[backware] -= anzahl
                einkauf.append((backware, anzahl))
                print(f"Es werden {anzahl}-mal {backware} aus der Auslage entnommen.")
        print(f"Der Kunde erhält folgende Waren: {einkauf}")
        print(f"Die verbleibende Auslage nach Abzug des Einkaufs: {auslage}")
        return einkauf

    def fülle_Bestand_nach(self, lieferung):
        auslage = self.prüf_Bestand()
        for teil in lieferung:
            auslage[teil] += 50
        print(f"Folgende Backwerke in der Auslage wurden um je 50 Stück nachgefüllt: {lieferung}")

class Preisliste:

    def __init__(self, preisliste):
        self.__preisliste = preisliste

    def prüf_Preisliste(self):
        return self.__preisliste

class Kasse:
    def __init__(self, geld):
        self.__geld = geld

    def geld_in_kasse(self):
        return self.__geld

    def geld_einzahlen(self, betrag):
        self.__geld += float(betrag)
        print(f"Es wurden {betrag} € in die Kasse eingezahlt.")

class Bestellung:
    # eine Bestellung ist eine Liste von Tupeln, die jeweils das Backwerk
    # und die Anzahl der bestellten Backwerke enthält

    def __init__(self, bestellung):
        self.__bestellung = bestellung

    def schaut_Bestellung_an(self):
        return self.__bestellung

auslage = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
    "Roggenmischbrot": 50,
    "Vollkornbrot": 50,
    "Dinkelbrot": 50,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 50,
    "Pfannkuchen": 50
}

# zum Testen fürs Nachfüllen
auslage2 = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
    "Roggenmischbrot": 0,
    "Vollkornbrot": 0,
    "Dinkelbrot": 50,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 50,
    "Pfannkuchen": 50
}

preisliste = {
    "Weizensemmel": 0.30,
    "Kürbiskernbrötchen": 0.40,
    "Roggenmischbrot": 2.00,
    "Vollkornbrot": 2.30,
    "Dinkelbrot": 2.10,
    "Croissant": 1.20,
    "Streuselkuchen": 1.40,
    "Bienenstich": 1.40,
    "Pfannkuchen": 1.20
}

kasse = Kasse(10000)
auslage = Auslage_Thresen(auslage)
preisliste = Preisliste(preisliste)
auslage2 = Auslage_Thresen(auslage2)