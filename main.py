import Büro, Auslage, Backstube, Lager, Verkaufsraum, Lager, Lieferant

if __name__ == '__main__':

    #Anmerkung: Im Moment findet keine permanente Veränderung der Datenstrukturen auslage und testbestand statt

    #Verkauf eines Backwerks oder Getränks oder beidem zusammen
    print(f"Hier eine Darstellung für den Verkauf eines Backwerks:")
    Büro.testverkäufer.verkaufe_Waren(Auslage.auslage, Auslage.kaffeemaschine, Auslage.kasse, Verkaufsraum.testkunde)

    # Nachfüllen der Auslage aus dem Lager
    print(f"Hier eine Darstellung für einen Auffüllungsprozess der Auslage:")
    Büro.testverkäufer.Backwaren_nachbestellen(Auslage.auslage, Büro.testbäcker, Lager.testbestand)

    # Backprozess
    print(f"Hier eine Darstellung von einem Backprozess:")
    Büro.testbäcker.backt(Lager.testbestand)

    #Durchführen einer Lohnänderung
    print(f"Hier eine Darstellung von einer Lohnänderung:")
    Büro.testchef.ändert_lohn(Büro.testverkäufer, 2500)

    #Lieferung für Zutaten:
    print(f"Hier eine Darstellung für das Nachbestellen von Zutaten:")
    Büro.testchef.bestellt_Zutaten(Lager.testbestand)

""" TO DO:
    beim Lieferanten ne Kasse eröffnen und nen richtigen Bezahlvorgang für den Chef einrichten"""