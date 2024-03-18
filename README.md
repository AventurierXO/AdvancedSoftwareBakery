# AdvancedSoftwareBakery: Software-Projekt für Advanced Software Engineering

## Beschreibung des Projekts

Dieses Projekt ist ein Management-System für eine imaginäre Bäckerei.
Um Geschäftsprozesse abzubilden, wurde eine grundlegende Struktur gemäß den Standards von "Domain-driven Development" (DDD).
Im Folgenden werden zunächst die Domänen vorgestellt und kurz ihre Funktionen im Management-System umrissen.

### Verkaufsraum

Der Verkaufsraum beinhaltet die Klasse Kunde, in der Bestellungen generiert und deren Erfüllung ausgelöst wird.

### Auslage

Die Auslage umfasst den Tresen sowie die Werkzeuge, die zum Verkauf nötig sind. Dies umfasst den Tresen, der die Backwerke enthält, die Kasse, die Preisliste und den Kaffeeautomaten. Weiterhin ist hier die Klasse Verkäufer_in verortet, die mit den Werkzeugen innerhalb der Domäne sowie mit Kunde und Bäcker_in interagiert, um ihre Aufgaben zu erfüllen und Bestellungen zum Nachfüllen des Tresens auszulösen.

### Backstube

In der Backstube finden die Backprozesse der Bäckerei statt. Dazu gibt es eine Klasse Rezepte, in der die Mengenangaben für die angebotenene Backwerke der Bäckerei zu finden sind. Weiterhin gibt es die Klasse Bäcker_in die den Backprozess ausführt und Bestellungen von der Klasse Verkäufer_innen entgegennimmt, diese im Lager nachprüft und wenn vorhanden an den Tresen liefert. Weiterhin checkt Bäcker_in das Lager nach vorhandenen Backwaren und beginnt Backwaren zu produzieren, wenn eine Backware unter den Mindestbestand fällt. Alternativ kann Verkäufer_in eine Bestellung für bestimmte Backwaren übergeben, die dann gebacken und gelagert werden.

### Lager

Im Lager werden sowohl Zutaten als auch Backwaren geliefert. Gelagerte Backwaren dienen als Puffer für den Tresen. Das Lager kann geprüft, aufgefüllt und geleert werden - je nach Funktion, die auf das Lager zugreift. Auf das Lager wird von der Klasse Chef, Lieferant und Bäcker_in zugegriffen.

### Büro

Im Büro sind die Führungsprozesse verortet. Die Superklasse Angestellte ist dort definiert. Von ihr erben sowohl Chef, Verkäufer_in und Bäcker_in. Die Klasse Chef ist die Führungskraft der Bäckerei und hat die Aufgaben, Angestellte anzustellen oder zu kündigen und Zutaten, die unter den Mindestbestand im Lager fallen, nachzubestellen und zu bezahlen.

### Lieferant

Diese Domäne enthält die Klasse Lieferant, die für Zutaten Bestellung erfüllen und Rechnungen bestellen kann. Um diese Aufgabe erfüllen zu können, gibt es eine Klasse Lagerarbeiter, der die Bestellungen des Lieferanten zusammenstellt. Dazu gibt es eine Klasse Lieferbestand, die den Bestand des Lieferanten umfasst. Weiterhin verfügt die Domäne über eine eigene Kasse und Preisliste, um den internen Verkaufsprozess abzuwickeln.

## Code Dokumentation

Im Folgenden werden für jede Domäne die Schnittstellen beschrieben

### Kunde

Die Klasse Kunde wird folgendermaßen intialisiert:

```
class Kunde:
    def __init__(self, name):
        self.__name = name
```

Bei der Klasse Kunde handelt es sich um eine sehr generische Klasse, die lediglich einen Namen besitzt. Da Kunden mit einem beliebigen Akteur der Klasse Verkäufer_in interagieren können, wird dem Kunden kein bestimmter Verkäufer bei der Initialisierung zugeordnet. Weiterhin besitzt der Kunde keine Werkzeuge, mit denen er interagieren muss, um seine Rolle zu erfüllen.

#### Bestellung von Backwaren:

```
def kauft_Backwaren(self, auslage, verkäufer):
	bestellung = []
        anzahl_versch_waren = random.randint(1,4)
        liste_waren = auslage.schaue_Waren_an()
        for anzahl in range(anzahl_versch_waren):
            gewünschte_waren = random.choice(liste_waren)
            anzahl_gewünschter_waren = random.randint(1, 4)
            bestellung.append((gewünschte_waren, anzahl_gewünschter_waren))
        verkäufer.verkaufe_Waren(bestellung)
```
Beim Aufruf der Funktion wird ein Akteur von der Klasse Verkäufer_in und ein Objekt der Klasse Auslage_Tresen zugeordnet. Per Zufall wird eine Bestellung generiert, die alle möglichen Backwaren der Auslage enthalten kann. Dazu wird zunächst zufällig bestimmt, wie viele verschiedene Waren bestellt werden. In Abhängigkeit von der Anzahl werden eine oder mehrere Bestellungen genriert, die dann als Tupel in die Bestellung angehängt wird. <br>
Nachdem die Liste bestellter Waren fertig generiert ist, wird sie dem zugeordneten Verkäufer übergeben und sein Verkaufsprozess wird gestartet. <br>

#### Bestellung von Getränken:

```
def kauft_Heißgetränk(self, kaffeemaschine, verkäufer):
        bestellung = []
        anzahl_versch_waren = random.randint(1, 2)
        liste_getränke = kaffeemaschine.schaut_Optionen_an()
        for anzahl in range(anzahl_versch_waren):
            gewünschte_waren = random.choice(liste_getränke)
            anzahl_gewünschter_waren = random.randint(1, 2)
            bestellung.append((gewünschte_waren, anzahl_gewünschter_waren))
        verkäufer.verkaufe_Getränke(bestellung)
```
Dieser Funktion wird wieder ein Akteur von der Klasse Verkäufer_in und ein Objektder Klasse Kaffeemaschine zugeordnet. Ähnlich zu der Backwarenbestellung wird wieder per Zufall die Menge der verschiedenen Waren und eine Anzahl einer bestellten Ware gezogen. <br>
Wie zuvor auch wird die Bestellung abhängig von der Anzahl der Teilbestellungen generiert und als Tupel in der Bestellung gespeichert. Diese Bestellung wird dann dem zugeordneten Verkäufer übergeben und der Prozess des Verkaufes wird gestartet.

#### Bezahlung einer Rechnung:

```
def bezahlen(self, rechnung):
        if rechnung <= 0:
            raise ValueError("Der zu bezahlende Betrag darf nicht 0 oder kleiner sein!")
        geldbetrag = rechnung
        return geldbetrag
```
Der Kunde erhält vom Verkäufer eine Rechnung und bezahlt diese, indem er den Geldbetrag an den Verkäufer übergibt.

### Verkäufer_in

Die Klasse Verkäufer_in wird folgendermaßen initialisiert:
```
class Verkäufer_in(Angestellte):
    def __init__(self, name, lohn, auslage, kasse, kaffeemaschine):
        self.auslage = auslage
        self.kasse = kasse
        self.kaffeemaschine= kaffeemaschine
        super().__init__(name, lohn)
```
Neben den generischen Eigenschaften Name und Lohn, die von der Superklasse geerbt werden, wird jedem Verkäufer jeweils ein Objekt von Typ Auslage_Tresen, Kasse und Kaffeemaschine zugeordnet. Dies ermöglicht, dass die Klasse direkt auf die Objekte zugreifen kann, was auch die Anzahl der zu übergebenden Argumente bei Funktionsaufrufen deutlich vekürzt.

#### Verkauf von Backwaren

```
def verkaufe_Backwaren(self, bestellung, kunde):
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht verarbeitet werden!")
        zu_bezahlen = 0
        fertige_wunschbackwaren = self.auslage.entnehme_Backwerk(bestellung)
        zu_bezahlen += self.kasse.erstelle_Rechnung(fertige_wunschbackwaren)
        if zu_bezahlen == 0:
            raise ValueError("Der Verkauf kann nicht bezahlt werden, weil keine der gewünschten Waren da ist.")
        eingenommenes_geld = self.kassiere_Geld_ein(zu_bezahlen, kunde)
        self.kasse.zahle_Geld_ein(eingenommenes_geld)
```
Der Funktion wird die Bestellung und der entsprechende Kunde übergeben. Zunächst werden die Waren in der Bestellung der Auslage entnommen. Sollten in der Auslage nicht genügen Backwerke vorhanden sein, wird das bestellte Backwerk nicht in der Liste entnommener Backwaren erscheinen. Danach wird in der Kasse die Rechnung für die vorhandenen Backwaren erstellt. Sollte die resultierende Rechnung gleich Null sein, wird der Verkaufsvorgang abgebrochen. Ansonsten wird der zu zahlende Betrag dem Kunden übergeben und das eingenommene Geld wird in die Kasse eingezahlt.

#### Verkauf von Getränken:
```
def verkaufe_Getränke(self, bestellung, kunde):
	if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht verarbeitet werden!")
        zu_bezahlen = 0
        fertige_wunschgetränke = self.kaffeemaschine.mache_Getränk(bestellung)
        zu_bezahlen += self.kasse.erstelle_Rechnung(fertige_wunschgetränke)
        eingenommenes_geld = self.kassiere_Geld_ein(zu_bezahlen, kunde)
        self.kasse.zahle_Geld_ein(eingenommenes_geld)
```
Der Funktion wird wieder eine Bestellung und der zugehörige Kunde übergeben. Die Getränke werden von der Kaffeemaschine zubereitet und der Preis der Bestellung wird in der Kasse berechnet. Der zu zahlende Betrag wird dann vom Kunden eingefordert und im Anschluss in die Kasse eingezahlt.

#### Nachbestellen von Backwaren:
```
def bestelle_Backwaren_nach(self, bäcker):
        fehlende_backwaren = self.auslage.erfasse_fehlende_Backwaren()
        if fehlende_backwaren == []:
            raise ValueError(f"Es sind noch genug Backstücke von jeder Sorte vorhanden.")
        geholte_backwaren = bäcker.liefere_Backstücke(fehlende_backwaren)
        self.auslage.fülle_Bestand_nach(geholte_backwaren)
```
Dieser Funktion wird ein Bäcker zugewiesen, der die Auffüllung der Auslage übernehmen soll. Es wird eine Liste fehlender Backwaren in der Auslage generiert, die dann dem Bäcker übergeben wird. Falls diese Liste leer ist, wird der Prozess abgebroche. Wenn vorhanden, liefert der Bäcker die Backwaren aus dem Lager an die Auslage, wo sie dann zur Auslage hinzugefügt werden.

### Bäcker_in
Die Klasse Bäcker_in wird folgendermaßen initialisiert:
```
class Bäcker_in(Angestellte):
    def __init__(self, name, lohn, lagerbestand, rezepte):
        self.lagerbestand = lagerbestand
        self.rezepte = rezepte
        super().__init__(name, lohn)
```
Der Klasse Bäcker_in wird im Speziellen der Lagerbestand und die Rezepte zugewiesen, die essentiell für ihre rollenspezifischen Prozesse sind.

#### Backen neuer Backwaren
```
def backe(self, bestellung = []):
        if bestellung == []:
            aufzufüllende_backstücke = self.ermittle_nachzufüllende_Backstücke()
        else:
            aufzufüllende_backstücke = bestellung
        if aufzufüllende_backstücke == []:
            raise ValueError(f"Im Moment gibt es keinen Bedarf für neue Backwaren.")
        neue_backstücke = self.produziere_Backstück(aufzufüllende_backstücke)
        self.lagerbestand.lagere_ein(neue_backstücke)
```
Der Funktion backe kann eine Bestellung übergeben werden, muss aber nicht. Falls keine Bestellung vorliegt, was der Regelfall ist, wird im Lagerbestand ermittelt, welche Backwerke unter der Mindestgrenze liegen. Sollten alle Backwerke auf oder über der Mindestgrenze liegen, wird der Prozess abgebrochen. Ansonsten werden die Backwerke produziert und eingelagert.

### Chef
Die Klasse Chef wird folgendermaßen initialisiert:
```
class Chef(Angestellte):
    def __init__(self, name, lohn, lagerbestand, lieferant, angestellte):
        self.lagerbestand = lagerbestand
        self.lieferant = lieferant
        self.angestellte = angestellte
        super().__init__(name, lohn)
```
Die Klasse Chef bekommt neben Namen und Lohn auch den Lagerbestand, einen Lieferanten und ein Dictionary mit allen Angestellten zugewiesen, um ihre rollenspezifischen Aufgaben zu erfüllen.

#### Bestellung von Zutaten
```
def bestelle_Zutaten(self):
        bestellung = self.Bestellung_erstellen()
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht an den Lieferanten überstellt werden!")
        rechnung = self.lieferant.erfülle_Lieferung(bestellung, self.lagerbestand)
        self.bezahlt_Rechnung(rechnung)
```
Der Chef erstellt eine Bestellung, indem er das Lager prüft und die Zutaten hinzufügt, wenn sie unter der Mindestzahl liegen. Wenn alle Zutaten genug befüllt sind, wird der Prozess abgebrochen. Die Lieferung wird dann dem Lieferanten überstellt und führt zu einer Rechnung, die der Chef bezahlt und dazu führt, dass der Lieferant das Geld in seine Kasse einbezahlt.

#### Mitarbeiter anstellen
```
def stelle_an(self, name, lohn, position, auslage, kasse, kaffeemaschine, lagerbestand, rezepte):
        if name in list(self.angestellte.keys()):
            raise KeyError("Es können keine zwei Angestellte denselben Namen haben! Bitte prüfen, ob der/die Angestellte bereits angelegt ist oder Namen durch Zahl ergänzen!")
        if position == "Bäcker_in":
            neuer_angestellter = Bäcker_in(name, lohn, lagerbestand, rezepte)
        if position == "Verkäufer_in":
            neuer_angestellter = Verkäufer_in(name, lohn, auslage, kasse, kaffeemaschine)
        self.angestellte.update({neuer_angestellter.gebe_Namen_an() : (neuer_angestellter.gebe_Lohn_an(), type(neuer_angestellter).__name__)})
```
Es gibt zwei Mitarbeiterklassen, die der Chef anstellen kann: Bäcker_in und Verkäufer_in. <br>
Dazu müssen die Daten des neuen Mitarbeiters übergeben werden, wie der Name, der Lohn und die Position. Weiterhin werden die rollenspezifischen Werkzeuge zugeordnet, damit beim Anlegen des Mitarbeiters gemäß der Definition der Rollen diese mit übergeben werden können. <br>
Wenn der Name bereits einem Mitarbeiter "gehört", dann muss eine Änderung vorgenommen werden, damit der neue Mitarbeiter angelegt werden kann. Danach werden die Mitarbeiter angelegt und in das Angestellten-Dictionary aufgenommen. <br>
Der Kündigungsprozess erfordert lediglich die Entfernung des Mitarbeiters aus dem Angestellten-Dictionary.

### Lieferant
Die Klasse Lieferant wird folgendermaßen initialisiert:
```
def __init__(self, name, lagerarbeiter, lieferbestand, kasse):
        self.__name = name
        self.lieferbestand = lieferbestand
        self.lagerarbeiter = lagerarbeiter
        self.kasse = kasse
```
Der Klasse Lieferant wird ein Name, ein Lagerarbeiter, ein Lieferbestand und eine Kasse zur Initialisierung übergeben.

#### Erfüllen einer Lieferung
```
def erfülle_Lieferung(self, bestellung, lagerbestand):
        if bestellung == []:
            raise ValueError("Eine leere Bestellung kann nicht erfüllt werden.")
        fertige_lieferung = self.lagerarbeiter.stelle_Lieferung_zusammen(bestellung)
        lagerbestand.lagere_ein(fertige_lieferung)
        rechnung = self.kasse.erstelle_Rechnung_Lieferung(fertige_lieferung)
        return rechnung
```
Der Funktion wird die Bestellung und der Lagerbestand des Kunden übergeben. Der Lieferant übergibt dem Lagerarbeiter die Bestellung, die dieser sogleich als fertie Lieferung zusammenstellt. Die Lieferung wird dann zur Bäckerei gebracht und dort eingelagert. Aus der Lieferung wird ein Rechnungsbetrag errechnet und dem Chef übersandt, die dieser bezahlt und daraufhin die Einzahlung in die Kasse auslöst.

## Am meisten genutzte Tastenkombinationen in PyCharm

Alt Enter: <br>
Kontextmenü - immer dann nützlich, um Variablen oder Funktionen wiederzufinden, z.B. wenn man sich verschrieben hat oder Probleme mit der Sichtbarkeit bestehen. <br>
<br>
Alt F7: <br>
Nach dem Überarbeiten einer Funktion kann man so schnell suchen, wo sie überall vorkommt, um zu überprüfen, ob etwas kaputt gegangen ist. <br>
<br>
Shift F6: <br>
Dieser Shortcut hilft dabei, alle Variablen- / Funktionsnamen auf einmal umzubenennen. Wurde viel benutzt, um ein einheitliches Benennungsschema umzusetzen.