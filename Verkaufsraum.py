#Domain Verkaufsraum

import Auslage

class Kunde:
    def __init__(self, name):
        self.__name = name

    def kauft_Backwaren(self):
        print("Der Kunde möchte folgende Backwaren kaufen: []")
        # Bestellung erstellen

    def gibt_Name(self):
        return self.__name

    def gibt_Bestellung_auf(self, bestellung):
        #bestellung ist eine Liste von Tupeln, in denen der Name und die Anzahl gewünschter Backwaren steht
        print(f"Der Kunde bestellt folgende Backwaren für morgen zum Abholen: {bestellung}")
        # braucht noch Inventar in der Auslage

    def holt_Bestellung_ab(self):
        print("Der Kunde holt seine Bestellung ab.")
        # braucht noch Inventar in der Auslage

    def bezahlen(self, rechnung):
        print(f"Der Kunde überreicht {rechnung}€.")
        Auslage.Kasse.geld_einzahlen(rechnung)

    def kauft_Backware(self, wunschwaren):
        rechnung = 0
        #wunschwaren ist eine Liste von Tupeln sein in denen die Backware und die Anzahl steht
        for teilbestellung in wunschwaren:
            backware = teilbestellung[0]
            anzahl = teilbestellung[1]
            if Auslage.bestand[backware] <= anzahl:
                print(f"{backware} ist leider ausverkauft.")
            else:
                Auslage.bestand[backware] -= anzahl
                print(f"Hier sind {anzahl}-mal {backware}.")
                rechnung += anzahl * Auslage.preisliste[backware]
        print(f"Der Preis für die Bestellung beträgt {rechnung}€.")
        self.bezahlen(rechnung)
        print(f"Vielen Dank für Ihren Einkauf.")

    def bestellt_Kaffee(self):
        print("Der Kunde bestellt einen Kaffee.")
        # braucht noch Inventar in der Auslage

    # Betreten des Verkaufsraums erstellt Kunden?
    # Verlassen des Verkaufsraums löscht Kunden, falls dieser keine Bestellung aufgegeben hat
