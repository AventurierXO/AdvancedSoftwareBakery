import Büro, Auslage, Backstube, Lager, Verkaufsraum, Lager, Lieferant

if __name__ == '__main__':

    #Anmerkung: Im Moment findet noch keine permanente Veränderung der Datenstrukturen auslage und testbestand statt

    #Verkauf eines Backwerks
    print(f"Hier eine Darstellung für den Verkauf eines Backwerks:")
    Büro.testverkäufer.verkaufe_Waren(Auslage.auslage, Auslage.kasse, Verkaufsraum.testkunde)

    #Nachfüllen der Auslage aus dem Lager
    print(f"Hier eine Darstellung für einen Auffüllungsprozess der Auslage:")
    Büro.testverkäufer.Backwaren_nachbestellen(Auslage.auslage2, Büro.testbäcker, Lager.testbestand)

    #Durchführen einer Lohnänderung
    print(f"Hier eine Darstellung von einer Lohnänderung:")
    Büro.testchef.ändert_lohn(Büro.testverkäufer, 2500)

    #hier den Backprozess einfügen!

    #Lieferung für Zutaten:
    print(f"Hier eine Darstellung für das Nachbestellen von Zutaten:")
    Büro.testchef.bestellt_Zutaten()

    """
    weitere Geschäftsprozesse, die noch implementiert werden müssen:
    2. Erfüllen einer Bestellung
      a) Der Kunde gibt eine Bestellung auf.
      b) Die Bestellung wird von einem Verkäufer aufgenommen.
      c) Der Verkäufer gibt die Bestellung an einen Bäcker weiter.
      d) Der Bäcker backt die Bestellung und lagert sie als Paket ins Lager ein.
      e) Der Kunde möchte seine Bestellung abholen.
      f) Aus dem Lager wird die Bestellung entnommen und dem Kunden überreicht.
      g) Dem Kunden wird eine Rechnung ausgestellt.
      h) Der Kunde bezahlt die Rechnung.
    3. Backen
      a) Im Lager ist ein Backstück leer.
      b) An einen Bäcker wird eine Bestellung für 150 neue Backstücke erteilt.
      c) Der Bäcker holt die Zutaten aus dem Lager.
      d) Der Bäcker fertigt den Teig.
      e) Der Bäcker backt das Backwerk.
      f) Der Bäcker lässt die Backstücke abkühlen.
      g) Wenn es sich um einen Kuchen handelt, wird dieser zusätzlich verziert.
      h) Der Bäcker bringt die Backstücke ins Lager.
    4. Kaffee verkaufen
      a) Der Kunde bestellt Kaffee.
      b) Ein Verkäufer geht zur Kaffemaschine und lässt dort eine Tasse Kaffee zubereiten.
      c) Der Kaffee wird dem Kunden überreicht.
      d) Für den Kaffee wird eine Rechnung erstellt bzw. zu einer bestehenden Rechnung hinzugefügt.
    #5. Ein neuer Mitarbeiter wird eingestellt
    #  (Auswahlprozess modellieren?)
    #  a) Im Büro wird ein neuer Mitarbeiter seiner neuen Rolle zugeteilt.
    6. Mitarbeiter bezahlen
      a) Jeden Monat wird im Büro der Lohn an die Mitarbeiter bezahlt.
    7. Erweiterung des Verkaufsprozesses im Verkaufsraum
      - Einrichten einer Schlange
      - Tische, wo man sitzen, essen und trinken kann? (Welcher Tisch ist gerade frei für wie viele Personen?)
    """