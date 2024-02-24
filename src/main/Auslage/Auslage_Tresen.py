class Auslage_Tresen:
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
            if auslage[backware] < 50:
                if auslage[backware] <0:
                    raise ValueError(f"Die Auslage darf keinen negativen Bestand haben! -> {backware}")
                fehlende_backwaren.append(backware)
        return fehlende_backwaren


    def entnehme_Backwerk(self, wunschwaren):
        if wunschwaren == []:
            raise ValueError("Die Liste der zu entnehmenden Waren kann nicht leer sein!")
        einkauf = []
        auslage = self.prüf_Bestand()
        for teilbestellung in wunschwaren:
            backware = teilbestellung[0]
            anzahl = teilbestellung[1]
            if anzahl == 0:
                raise ValueError("Es können nicht 0 Backwerke entnommen werden!")
            if auslage[backware] <= anzahl:
                raise ValueError(f"Es sind nicht genug Teile {backware} vorhanden.")
            else:
                auslage[backware] -= anzahl
                einkauf.append((backware, anzahl))
        if einkauf == []:
            raise ValueError("Wenn der Einkauf leer ist, braucht er nicht weiter verarbeitet zu werden.")
        return einkauf

    def fülle_Bestand_nach(self, lieferung):
        if lieferung == []:
            raise ValueError("Um die Auslage befüllen zu können, muss die Lieferung Backwerke enthalten!")
        auslage = self.prüf_Bestand()
        for teil in lieferung:
            if teil not in list(auslage.keys()):
                raise KeyError("Die Backware gibt es in der Auslage nicht.")
            auslage[teil] += 50