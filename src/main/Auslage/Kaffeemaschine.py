class Kaffeemaschine:
    """
    Diese Klasse repräsentiert eine Kaffeemaschine

    Attribute:
    ----------
    getraenke_optionen: list
        eine Liste möglicher Getränke, die die Kaffeemaschine produzieren kann
    """
    def __init__(self, getraenke_optionen):
        self.__getraenke_optionen = getraenke_optionen

    def schaue_optionen_an(self):
        return self.__getraenke_optionen

    def mache_getraenk(self, getraenke):
        """Jedes Getraenk in der Liste wird gemaess der Anzahl zubereitet und gibt eine Liste fertiger Getraenke zurueck."""
        if getraenke == []:
            raise ValueError("Die Kaffeemaschine kann keine leere Bestellung annehmen!")
        fertige_getraenke = []
        for getraenk in getraenke:
            if (getraenk[0] in self.__getraenke_optionen) & (getraenk[1] > 0):
                fertige_getraenke.append(getraenk)
            else:
                raise ValueError("Diese Bestellung kann die Kaffeemaschine nicht zubereiten (falsches Getränk oder Anzahl)!")
        return fertige_getraenke
