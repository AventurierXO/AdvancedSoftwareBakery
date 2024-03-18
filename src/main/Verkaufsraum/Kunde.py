import random
from Verkaufsraum.BestellungBuilder import BestellungBuilder

class Kunde:
    def __init__(self, name):
        self.__name = name

    def gibt_Name(self):
        return self.__name

    def kauft_Backwaren(self, auslage, verkäufer):
        """Eine Kundenbestellung für Backwaren wird generiert und an den Verkäufer zur Verarbeitung übergeben."""
        bestellung = BestellungBuilder().Gebäckoptionen(auslage.schaue_Waren_an()).Backbestellung_erzeugen()
        verkäufer.verkaufe_Waren(bestellung, self)

    def kauft_Heißgetränk(self, kaffeemaschine, verkäufer):
        """Eine Kundenbestellung für Getränke wird generiert und an den Verkäufer zur Verarbeitung übergeben."""
        bestellung = BestellungBuilder().Getränkeoptionen(kaffeemaschine.schaue_Optionen_an()).Getränkebestellung_erzeugen()
        verkäufer.verkaufe_Getränke(bestellung, self)

    def bezahlen(self, rechnung):
        """Der Kunde bezahlt eine übergebene Rechnung mit dem entsprechenden Betrag."""
        if rechnung <= 0:
            raise ValueError("Der zu bezahlende Betrag darf nicht 0 oder kleiner sein!")
        geldbetrag = rechnung
        return geldbetrag