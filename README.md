# AdvancedSoftwareBakery: Software-Projekt fuer Advanced Software Engineering

## Wegweiser

[Event Storming, Core Domain Chart, Domain Relation Chart, UML Diagramme & DSL Demo (Sequenzdiagramm fuer Verkauf von Backwaren)](https://github.com/AventurierXO/AdvancedSoftwareBakery/tree/main/Diagramme) <br>
[CCD Cheat Sheet und Erfahrungen](https://github.com/AventurierXO/AdvancedSoftwareBakery/tree/main/CCD)<br>
[Main: Domains](https://github.com/AventurierXO/AdvancedSoftwareBakery/tree/main/src/main) <br>
[Fluent Interface Anwendung](https://github.com/AventurierXO/AdvancedSoftwareBakery/blob/main/src/main/Verkaufsraum/BestellungBuilder.py) <br>
[Build](https://github.com/AventurierXO/mavendemo) <br>
[Continuous Delivery](https://github.com/AventurierXO/AdvancedSoftwareBakery/blob/main/pyproject.toml) <br>
[Unit-Tests](https://github.com/AventurierXO/AdvancedSoftwareBakery/tree/main/tests) <br>
Dokumentation und Lieblings-Shortcuts hierunter

## Beschreibung des Projekts

Dieses Projekt ist ein Management-System fuer eine imaginaere Baeckerei.
Um Geschaeftsprozesse abzubilden, wurde eine grundlegende Struktur gemaess den Standards von "Domain-driven Development" (DDD).
Im Folgenden werden zunaechst die Domaenen vorgestellt und kurz ihre Funktionen im Management-System umrissen.

### Verkaufsraum

Der Verkaufsraum beinhaltet die Klasse Kunde, in der Bestellungen generiert und deren Erfuellung ausgeloest wird.

### Auslage

Die Auslage umfasst den Tresen sowie die Werkzeuge, die zum Verkauf noetig sind. Dies umfasst den Tresen, der die Backwerke enthaelt, die Kasse, die Preisliste und den Kaffeeautomaten. Weiterhin ist hier die Klasse Verkaeufer verortet, die mit den Werkzeugen innerhalb der Domaene sowie mit Kunde und Baecker interagiert, um ihre Aufgaben zu erfuellen und Bestellungen zum Nachfuellen des Tresens auszuloesen.

### Backstube

In der Backstube finden die Backprozesse der Baeckerei statt. Dazu gibt es eine Klasse Rezepte, in der die Mengenangaben fuer die angebotenene Backwerke der Baeckerei zu finden sind. Weiterhin gibt es die Klasse Baecker die den Backprozess ausfuehrt und Bestellungen von der Klasse Verkaeufernen entgegennimmt, diese im Lager nachprueft und wenn vorhanden an den Tresen liefert. Weiterhin checkt Baecker das Lager nach vorhandenen Backwaren und beginnt Backwaren zu produzieren, wenn eine Backware unter den Mindestbestand faellt. Alternativ kann Verkaeufer eine Bestellung fuer bestimmte Backwaren uebergeben, die dann gebacken und gelagert werden.

### Lager

Im Lager werden sowohl Zutaten als auch Backwaren geliefert. Gelagerte Backwaren dienen als Puffer fuer den Tresen. Das Lager kann geprueft, aufgefuellt und geleert werden - je nach Funktion, die auf das Lager zugreift. Auf das Lager wird von der Klasse Chef, Lieferant und Baecker zugegriffen.

### Buero

Im Buero sind die Fuehrungsprozesse verortet. Die Superklasse Angestellte ist dort definiert. Von ihr erben sowohl Chef, Verkaeufer und Baecker. Die Klasse Chef ist die Fuehrungskraft der Baeckerei und hat die Aufgaben, Angestellte anzustellen oder zu kuendigen und Zutaten, die unter den Mindestbestand im Lager fallen, nachzubestellen und zu bezahlen.

### Lieferant

Diese Domaene enthaelt die Klasse Lieferant, die fuer Zutaten Bestellung erfuellen und Rechnungen bestellen kann. Um diese Aufgabe erfuellen zu koennen, gibt es eine Klasse Lagerarbeiter, der die Bestellungen des Lieferanten zusammenstellt. Dazu gibt es eine Klasse Lieferbestand, die den Bestand des Lieferanten umfasst. Weiterhin verfuegt die Domaene ueber eine eigene Kasse und Preisliste, um den internen Verkaufsprozess abzuwickeln.

## Code Dokumentation

Im Folgenden werden fuer jede Domaene die Schnittstellen beschrieben

### Kunde

Die Klasse Kunde wird folgendermassen intialisiert:

```
class Kunde:
    def __init__(self, name):
        self.__name = name
```

Bei der Klasse Kunde handelt es sich um eine sehr generische Klasse, die lediglich einen Namen besitzt. Da Kunden mit einem beliebigen Akteur der Klasse Verkaeufer interagieren koennen, wird dem Kunden kein bestimmter Verkaeufer bei der Initialisierung zugeordnet. Weiterhin besitzt der Kunde keine Werkzeuge, mit denen er interagieren muss, um seine Rolle zu erfuellen.

#### Bestellung von Backwaren:

```
def kauft_backwaren(self, auslage, verkaeufer):
        bestellung = BestellungBuilder().gebaeckoptionen(auslage.schaue_waren_an()).backbestellung_erzeugen()
        verkaeufer.verkaufe_Waren(bestellung, self)
```
Beim Aufruf der Funktion wird ein Akteur von der Klasse Verkaeufer und ein Objekt der Klasse Auslage_Tresen zugeordnet. Per Zufall wird mit Hilfe des Bestellungsbuilders eine Bestellung generiert, die alle moeglichen Backwaren der Auslage enthalten kann. Dazu wird zunaechst zufaellig bestimmt, wie viele verschiedene Waren bestellt werden. In Abhaengigkeit von der Anzahl werden eine oder mehrere Bestellungen genriert, die dann als Tupel in die Bestellung angehaengt wird. <br>
Nachdem die Liste bestellter Waren fertig generiert ist, wird sie dem zugeordneten Verkaeufer uebergeben und sein Verkaufsprozess wird gestartet. <br>

#### Bestellung von Getraenken:

```
def kauft_heissgetraenk(self, kaffeemaschine, verkaeufer):
        bestellung = BestellungBuilder().getraenkeoptionen(kaffeemaschine.schaue_optionen_an()).getraenkebestellung_erzeugen()
        verkaeufer.verkaufe_getraenke(bestellung, self)
```
Dieser Funktion wird wieder ein Akteur von der Klasse Verkaeufer und ein Objektder Klasse Kaffeemaschine zugeordnet. aehnlich zu der Backwarenbestellung wird wieder der Bestellungsbuilder verwendet, um eine zufaellige Bestellung von Getraenken zu erzeugen. Diese Bestellung wird dann dem zugeordneten Verkaeufer uebergeben und der Prozess des Verkaufes wird gestartet.

#### Bezahlung einer Rechnung:

```
def bezahlen(self, rechnung):
        if rechnung <= 0:
            raise ValueError("Der zu bezahlende Betrag darf nicht 0 oder kleiner sein!")
        geldbetrag = rechnung
        return geldbetrag
```
Der Kunde erhaelt vom Verkaeufer eine Rechnung und bezahlt diese, indem er den Geldbetrag an den Verkaeufer uebergibt.

### Verkaeufer

Die Klasse Verkaeufer wird folgendermassen initialisiert:
```
class Verkaeufer(Angestellte):
    def __init__(self, name, lohn, auslage, kasse, kaffeemaschine):
        self.auslage = auslage
        self.kasse = kasse
        self.kaffeemaschine= kaffeemaschine
        super().__init__(name, lohn)
```
Neben den generischen Eigenschaften Name und Lohn, die von der Superklasse geerbt werden, wird jedem Verkaeufer jeweils ein Objekt von Typ Auslage_Tresen, Kasse und Kaffeemaschine zugeordnet. Dies ermoeglicht, dass die Klasse direkt auf die Objekte zugreifen kann, was auch die Anzahl der zu uebergebenden Argumente bei Funktionsaufrufen deutlich vekuerzt.

#### Verkauf von Backwaren

```
def verkaufe_backwaren(self, bestellung, kunde):
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht verarbeitet werden!")
        zu_bezahlen = 0
        fertige_wunschbackwaren = self.auslage.entnehme_backwerk(bestellung)
        zu_bezahlen += self.kasse.erstelle_rechnung(fertige_wunschbackwaren)
        if zu_bezahlen == 0:
            raise ValueError("Der Verkauf kann nicht bezahlt werden, weil keine der gewuenschten Waren da ist.")
        eingenommenes_geld = self.kassiere_geld_ein(zu_bezahlen, kunde)
        self.kasse.zahle_geld_ein(eingenommenes_geld)
```
Der Funktion wird die Bestellung und der entsprechende Kunde uebergeben. Zunaechst werden die Waren in der Bestellung der Auslage entnommen. Sollten in der Auslage nicht genuegen Backwerke vorhanden sein, wird das bestellte Backwerk nicht in der Liste entnommener Backwaren erscheinen. Danach wird in der Kasse die Rechnung fuer die vorhandenen Backwaren erstellt. Sollte die resultierende Rechnung gleich Null sein, wird der Verkaufsvorgang abgebrochen. Ansonsten wird der zu zahlende Betrag dem Kunden uebergeben und das eingenommene Geld wird in die Kasse eingezahlt.

#### Verkauf von Getraenken:
```
def verkaufe_getraenke(self, bestellung, kunde):
	if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht verarbeitet werden!")
        zu_bezahlen = 0
        fertige_wunschgetraenke = self.kaffeemaschine.mache_getraenk(bestellung)
        zu_bezahlen += self.kasse.erstelle_rechnung(fertige_wunschgetraenke)
        eingenommenes_geld = self.kassiere_geld_ein(zu_bezahlen, kunde)
        self.kasse.zahle_geld_ein(eingenommenes_geld)
```
Der Funktion wird wieder eine Bestellung und der zugehoerige Kunde uebergeben. Die Getraenke werden von der Kaffeemaschine zubereitet und der Preis der Bestellung wird in der Kasse berechnet. Der zu zahlende Betrag wird dann vom Kunden eingefordert und im Anschluss in die Kasse eingezahlt.

#### Nachbestellen von Backwaren:
```
def bestelle_backwaren_nach(self, baecker):
        fehlende_backwaren = self.auslage.erfasse_fehlende_backwaren()
        if fehlende_backwaren == []:
            raise ValueError(f"Es sind noch genug Backstuecke von jeder Sorte vorhanden.")
        geholte_backwaren = baecker.liefere_backstuecke(fehlende_backwaren)
        self.auslage.fuelle_bestand_nach(geholte_backwaren)
```
Dieser Funktion wird ein Baecker zugewiesen, der die Auffuellung der Auslage uebernehmen soll. Es wird eine Liste fehlender Backwaren in der Auslage generiert, die dann dem Baecker uebergeben wird. Falls diese Liste leer ist, wird der Prozess abgebroche. Wenn vorhanden, liefert der Baecker die Backwaren aus dem Lager an die Auslage, wo sie dann zur Auslage hinzugefuegt werden.

### Baecker
Die Klasse Baecker wird folgendermassen initialisiert:
```
class Baecker(Angestellte):
    def __init__(self, name, lohn, lagerbestand, rezepte):
        self.lagerbestand = lagerbestand
        self.rezepte = rezepte
        super().__init__(name, lohn)
```
Der Klasse Baecker wird im Speziellen der Lagerbestand und die Rezepte zugewiesen, die essentiell fuer ihre rollenspezifischen Prozesse sind.

#### Backen neuer Backwaren
```
def backe(self, bestellung = []):
        if bestellung == []:
            aufzufuellende_backstuecke = self.ermittle_nachzufuellende_backstuecke()
        else:
            aufzufuellende_backstuecke = bestellung
        if aufzufuellende_backstuecke == []:
            raise ValueError(f"Im Moment gibt es keinen Bedarf fuer neue Backwaren.")
        neue_backstuecke = self.produziere_backstueck(aufzufuellende_backstuecke)
        self.lagerbestand.lagere_ein(neue_backstuecke)
```
Der Funktion backe kann eine Bestellung uebergeben werden, muss aber nicht. Falls keine Bestellung vorliegt, was der Regelfall ist, wird im Lagerbestand ermittelt, welche Backwerke unter der Mindestgrenze liegen. Sollten alle Backwerke auf oder ueber der Mindestgrenze liegen, wird der Prozess abgebrochen. Ansonsten werden die Backwerke produziert und eingelagert.

### Chef
Die Klasse Chef wird folgendermassen initialisiert:
```
class Chef(Angestellte):
    def __init__(self, name, lohn, lagerbestand, lieferant, angestellte):
        self.lagerbestand = lagerbestand
        self.lieferant = lieferant
        self.angestellte = angestellte
        super().__init__(name, lohn)
```
Die Klasse Chef bekommt neben Namen und Lohn auch den Lagerbestand, einen Lieferanten und ein Dictionary mit allen Angestellten zugewiesen, um ihre rollenspezifischen Aufgaben zu erfuellen.

#### Bestellung von Zutaten
```
def bestelle_zutaten(self):
        bestellung = self.erstelle_bestellung()
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht an den Lieferanten ueberstellt werden!")
        rechnung = self.lieferant.erfuelle_lieferung(bestellung, self.lagerbestand)
        self.bezahle_rechnung(rechnung)
```
Der Chef erstellt eine Bestellung, indem er das Lager prueft und die Zutaten hinzufuegt, wenn sie unter der Mindestzahl liegen. Wenn alle Zutaten genug befuellt sind, wird der Prozess abgebrochen. Die Lieferung wird dann dem Lieferanten ueberstellt und fuehrt zu einer Rechnung, die der Chef bezahlt und dazu fuehrt, dass der Lieferant das Geld in seine Kasse einbezahlt.

#### Mitarbeiter anstellen
```
def stelle_an(self, name, lohn, position, auslage, kasse, kaffeemaschine, lagerbestand, rezepte):
        if name in list(self.angestellte.keys()):
            raise KeyError("Es koennen keine zwei Angestellte denselben Namen haben! Bitte pruefen, ob der/die Angestellte bereits angelegt ist oder Namen durch Zahl ergaenzen!")
        if position == "Baecker":
            neuer_angestellter = Baecker(name, lohn, lagerbestand, rezepte)
        if position == "Verkaeufer":
            neuer_angestellter = Verkaeufer(name, lohn, auslage, kasse, kaffeemaschine)
        self.angestellte.update({neuer_angestellter.gebe_namen_an() : (neuer_angestellter.gebe_lohn_an(), type(neuer_angestellter).__name__)})
```
Es gibt zwei Mitarbeiterklassen, die der Chef anstellen kann: Baecker und Verkaeufer. <br>
Dazu muessen die Daten des neuen Mitarbeiters uebergeben werden, wie der Name, der Lohn und die Position. Weiterhin werden die rollenspezifischen Werkzeuge zugeordnet, damit beim Anlegen des Mitarbeiters gemaess der Definition der Rollen diese mit uebergeben werden koennen. <br>
Wenn der Name bereits einem Mitarbeiter "gehoert", dann muss eine aenderung vorgenommen werden, damit der neue Mitarbeiter angelegt werden kann. Danach werden die Mitarbeiter angelegt und in das Angestellten-Dictionary aufgenommen. <br>
Der Kuendigungsprozess erfordert lediglich die Entfernung des Mitarbeiters aus dem Angestellten-Dictionary.

### Lieferant
Die Klasse Lieferant wird folgendermassen initialisiert:
```
def __init__(self, name, lagerarbeiter, lieferbestand, kasse):
        self.__name = name
        self.lieferbestand = lieferbestand
        self.lagerarbeiter = lagerarbeiter
        self.kasse = kasse
```
Der Klasse Lieferant wird ein Name, ein Lagerarbeiter, ein Lieferbestand und eine Kasse zur Initialisierung uebergeben.

#### Erfuellen einer Lieferung
```
def erfuelle_lieferung(self, bestellung, lagerbestand):
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht erfuellt werden.")
        fertige_lieferung = self.lagerarbeiter.stelle_lieferung_zusammen(bestellung)
        lagerbestand.lagere_ein(fertige_lieferung)
        rechnung = self.kasse.erstelle_rechnung_lieferung(fertige_lieferung)
        return rechnung
```
Der Funktion wird die Bestellung und der Lagerbestand des Kunden uebergeben. Der Lieferant uebergibt dem Lagerarbeiter die Bestellung, die dieser sogleich als fertie Lieferung zusammenstellt. Die Lieferung wird dann zur Baeckerei gebracht und dort eingelagert. Aus der Lieferung wird ein Rechnungsbetrag errechnet und dem Chef uebersandt, die dieser bezahlt und daraufhin die Einzahlung in die Kasse ausloest.

## Am meisten genutzte Tastenkombinationen in PyCharm

Alt Enter: <br>
Kontextmenue - immer dann nuetzlich, um Variablen oder Funktionen wiederzufinden, z.B. wenn man sich verschrieben hat oder Probleme mit der Sichtbarkeit bestehen. <br>
<br>
Alt F7: <br>
Nach dem ueberarbeiten einer Funktion kann man so schnell suchen, wo sie ueberall vorkommt, um zu ueberpruefen, ob etwas kaputt gegangen ist. <br>
<br>
Shift F6: <br>
Dieser Shortcut hilft dabei, alle Variablen- / Funktionsnamen auf einmal umzubenennen. Wurde viel benutzt, um ein einheitliches Benennungsschema umzusetzen.