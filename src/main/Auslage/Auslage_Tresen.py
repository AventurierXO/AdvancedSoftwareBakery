"""Klasse Auslage_Tresen: Haelt Funktionen, die es ermoeglichen mit der Auslage zu interagieren"""
class Auslage_Tresen:
    def __init__(self, auslage):
        self.__auslage = auslage

    def pruefe_bestand(self):
        return self.__auslage

    def schaue_waren_an(self):
        return list(self.__auslage.keys())

    def erfasse_fehlende_backwaren(self):
        """Die Auslage wird nach Backwaren untersucht, die eine Stueckzahl <50 aufweisen und gibt diese in einer Liste zurueck."""
        auslage = self.pruefe_bestand()
        fehlende_backwaren = []
        for backware in auslage:
            if auslage[backware] < 50:
                if auslage[backware] <0:
                    raise ValueError(f"Die Auslage darf keinen negativen Bestand haben! -> {backware}")
                fehlende_backwaren.append(backware)
        return fehlende_backwaren


    def entnehme_backwerk(self, wunschwaren):
        """Fuer jedes Element in der uebergebenen Liste werden die Backwaren in der geforderten Anzahl entnommen, wenn genug vorhanden sind."""
        if wunschwaren == []:
            raise ValueError("Die Liste der zu entnehmenden Waren kann nicht leer sein!")
        einkauf = []
        auslage = self.pruefe_bestand()
        for teilbestellung in wunschwaren:
            backware = teilbestellung[0]
            anzahl = teilbestellung[1]
            if backware not in list(auslage.keys()):
                raise KeyError("Die Backware gibt es in der Auslage nicht.")
            if anzahl == 0:
                raise ValueError("Es koennen nicht 0 Backwerke entnommen werden!")
            if auslage[backware] <= anzahl:
                raise ValueError(f"Es sind nicht genug Teile {backware} vorhanden.")
            else:
                auslage[backware] -= anzahl
                einkauf.append((backware, anzahl))
        if einkauf == []:
            raise ValueError("Wenn der Einkauf leer ist, braucht er nicht weiter verarbeitet zu werden.")
        return einkauf

    def fuelle_bestand_nach(self, lieferung):
        """Die Auslage wird mit jeder Backwerksorte in der Lieferung um 50 aufgefuellt."""
        if lieferung == []:
            raise ValueError("Um die Auslage befuellen zu koennen, muss die Lieferung Backwerke enthalten!")
        auslage = self.pruefe_bestand()
        for teil in lieferung:
            if teil not in list(auslage.keys()):
                raise KeyError("Die Backware gibt es in der Auslage nicht.")
            auslage[teil] += 50