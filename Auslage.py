#Domain Auslage/Thresen

import Backstube

class Verkäufer_in:
    def __init__(self, name, lohn):
        self.__name = name
        self.__lohn = lohn

    def prüft_Lohn(self):
        return self.__lohn

    def ändert_Lohn(self, lohnänderung):
        self.__lohn = lohnänderung

    def gibt_Name(self):
        return self.__name

class Auslage_Thresen:
    def __init__(self, bestand):
        self.__bestand = bestand

    def prüft_Bestand(self):
        return self.__bestand

class Kasse:
    def __init__(self, geld):
        self.__geld = geld

    def geld_ändern(self, betrag):
        self.__geld += betrag

    def geld_einzahlen(self, betrag):
        self.geld_ändern(betrag)



bestand = {
    "Weizensemmel": 0,
    "Kürbiskernbrötchen": 0,
    "Roggenmischbrot": 0,
    "Vollkornbrot": 0,
    "Dinkelbrot": 0,
    "Croissant": 0,
    "Streuselkuchen": 0,
    "Bienenstich": 0,
    "Pfannkuchen": 0
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