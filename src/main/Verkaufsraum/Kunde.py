import random
from Verkaufsraum.BestellungBuilder import BestellungBuilder

class Kunde:
    """
    Diese Klasse repräsentiert den Kunden

    Attribute:
    ----------
    name: String
        der Name des Kunden
    """
    def __init__(self, name):
        self.__name = name

    def gebe_namen_an(self):
        return self.__name

    def kauft_backwaren(self, auslage, verkaeufer):
        """Eine Kundenbestellung fuer Backwaren wird generiert und an den Verkaeufer zur Verarbeitung uebergeben."""
        bestellung = BestellungBuilder().gebaeckoptionen(auslage.schaue_waren_an()).backbestellung_erzeugen()
        verkaeufer.verkaufe_Waren(bestellung, self)

    def kauft_heissgetraenk(self, kaffeemaschine, verkaeufer):
        """Eine Kundenbestellung fuer Getraenke wird generiert und an den Verkaeufer zur Verarbeitung uebergeben."""
        bestellung = BestellungBuilder().getraenkeoptionen(kaffeemaschine.schaue_optionen_an()).getraenkebestellung_erzeugen()
        verkaeufer.verkaufe_getraenke(bestellung, self)

    def bezahlen(self, rechnung):
        """Der Kunde bezahlt eine uebergebene Rechnung mit dem entsprechenden Betrag."""
        if rechnung <= 0:
            raise ValueError("Der zu bezahlende Betrag darf nicht 0 oder kleiner sein!")
        geldbetrag = rechnung
        return geldbetrag