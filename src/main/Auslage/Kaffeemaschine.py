class Kaffeemaschine:
    def __init__(self, getränke_optionen):
        self.__getränke_optionen = getränke_optionen

    def schaue_Optionen_an(self):
        return self.__getränke_optionen

    def mache_Getränk(self, getränke):
        """Jedes Getränk in der Liste wird gemäß der Anzahl zubereitet und gibt eine Liste fertiger Getränke zurück."""
        if getränke == []:
            raise ValueError("Die Kaffeemaschine kann keine leere Bestellung annehmen!")
        fertige_getränke = []
        for getränk in getränke:
            if (getränk[0] in self.__getränke_optionen) & (getränk[1] > 0):
                fertige_getränke.append(getränk)
            else:
                raise ValueError(f"Dieses Getränk kann die Kaffeemaschine nicht zubereiten!")
        return fertige_getränke
