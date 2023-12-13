import Büro, Auslage, Backstube, Lager, Verkaufsraum, Lager, Lieferant

if __name__ == '__main__':

    #Anmerkung: Im Moment findet noch keine permanente Veränderung der Datenstrukturen auslage und testbestand statt

    #Verkauf eines Backwerks
    print(f"Hier eine Darstellung für den Verkauf eines Backwerks:")
    Büro.testverkäufer.verkaufe_Waren(Auslage.auslage, Auslage.kasse, Verkaufsraum.testkunde)

    #Nachfüllen der Auslage aus dem Lager
    print(f"Hier eine Darstellung für einen Auffüllungsprozess der Auslage:")
    Büro.testverkäufer.Backwaren_nachbestellen(Auslage.auslage2, Büro.testbäcker, Lager.testbestand)