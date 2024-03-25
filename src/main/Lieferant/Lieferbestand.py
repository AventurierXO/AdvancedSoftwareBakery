class Lieferbestand:
    """
    Diese Klasse repräsentiert den Lagerbestand eines Lieferanten

    Attribute:
    ----------
    bestand: liste
        eine Liste mit den Namen der lieferbaren Waren (es wird davon ausgegangen, dass das Kontingent unendlich ist)
    """
    def __init__(self, bestand):
        self.__bestand = bestand

    def pruefe_bestand(self):
        return self.__bestand
