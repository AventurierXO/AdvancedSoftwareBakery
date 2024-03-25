# AdvancedSoftwareBakery: Software-Projekt fuer Advanced Software Engineering

## Wegweiser

1) [Git](#git)
2) [Event Storming, Core Domain Chart, Domain Relation Chart, UML Diagramme & DSL Demo (Sequenzdiagramm fuer Verkauf von Backwaren)](https://github.com/AventurierXO/AdvancedSoftwareBakery/tree/main/Diagramme) <br>
3) [Domains](https://github.com/AventurierXO/AdvancedSoftwareBakery/tree/main/src/main) <br> fuer Event Storming, Core Domain Chart und Domain Relation Chart siehe Link unter 2. <br>
   [Erfahrungen DDD](#ddd)
4) [Metrics Sonarcube](https://github.com/AventurierXO/AdvancedSoftwareBakery/blob/main/Metrics/SonarqubeMetrics.png)<br>
    [Erfahrungen Metrics](#metrics)
5) [CCD Cheat Sheet und CCD Anwendung](https://github.com/AventurierXO/AdvancedSoftwareBakery/tree/main/CCD)<br>
   [Erfahrungen CCD](#clean-code-development)
6) [Build Maven Demo](https://github.com/AventurierXO/mavendemo) <br>
   [Erfahrungen Build](#build)
7) [Continuous Delivery](https://github.com/AventurierXO/AdvancedSoftwareBakery/blob/main/pyproject.toml) <br>
   [Erfahrungen Continuous Delivery](#continuous-delivery)
8) [Unit Tests](https://github.com/AventurierXO/AdvancedSoftwareBakery/tree/main/src/main/tests) <br>
   [Erfahrungen Unit Tests](#unit-tests)
9) [Lieblings-Tastenkombinationen](#lieblings-tastenkombinationen) <br>
10) [DSL Demo: Verkauf von Backwaren](https://github.com/AventurierXO/AdvancedSoftwareBakery/blob/main/Diagramme/Sequenzidagramm%20f%C3%BCr%20den%20Verkauf%20von%20Backwaren.png) <br>
    [Erfahrungen DSL Demo](#dsl-demo)
11) Functional Programming <br>
[Functional Programming: Python](https://github.com/AventurierXO/AdvancedSoftwareBakery/tree/main/Functional%20Programming) <br>
[Functional Programming: Java](https://github.com/AventurierXO/mavendemo/tree/master/src) <br>
    [Erfahrungen Functional Programming](#functional-programming)
12) [Code Dokumentation](#code-dokumentation)
13) [Fluent Interface Anwendung](https://github.com/AventurierXO/AdvancedSoftwareBakery/blob/main/src/main/Verkaufsraum/BestellungBuilder.py) <br>

## Einfuehrung ins Projekt

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
Beim Aufruf der Funktion wird ein Akteur von der Klasse Verkaeufer und ein Objekt der Klasse AuslageTresen zugeordnet. Per Zufall wird mithilfe des Bestellungsbuilders eine Bestellung generiert, die alle moeglichen Backwaren der Auslage enthalten kann. Dazu wird zunaechst zufaellig bestimmt, wie viele verschiedene Waren bestellt werden. In Abhaengigkeit von der Anzahl werden eine oder mehrere Bestellungen genriert, die dann als Tupel in die Bestellung angehaengt wird. <br>
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
Neben den generischen Eigenschaften Name und Lohn, die von der Superklasse geerbt werden, wird jedem Verkaeufer jeweils ein Objekt von Typ AuslageTresen, Kasse und Kaffeemaschine zugeordnet. Dies ermoeglicht, dass die Klasse direkt auf die Objekte zugreifen kann, was auch die Anzahl der zu uebergebenden Argumente bei Funktionsaufrufen deutlich vekuerzt.

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
Wenn der Name bereits einem Mitarbeiter "gehoert", dann muss eine Aenderung vorgenommen werden, damit der neue Mitarbeiter angelegt werden kann. Danach werden die Mitarbeiter angelegt und in das Angestellten-Dictionary aufgenommen. <br>
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

## Erlaeuterungen Aufgaben Part B

### Git
Git wurde vorwiegend ueber das Git-Plugin von PyCharm sowie ueber Git Desktop genutzt. Es wurden regelmaessige Aktualisierungen
mit Kommentaren zur Aenderung gepushed und Aenderungen wurden auch einmal rueckgaengig gemacht, da ein fehlerhafter Push
stattgefunden hat. Konflikte konnten aufgrund der Natur des Projekts nicht abgegbildet werden.
<br>[zurueck zum Wegweiser](#wegweiser)
### UML
Mithilfe der Browserversion von PlantUML wurden die Diagramme erzeugt. Es war ein Spass, sich durch die Dokumentation
zu arbeiten und zu lernen, wie die entsprechenden Diagrammtypen geschrieben werden und deren Darstellung in Echtzeit zu
beobachten. Es war auch eine wichtige Stuetze bei der Festhaltung des Projektfortschritts. <br>
Im Git sind die finalen Versionen der Diagramme zu finden, sie wurden aber ueber das Projekt hinweg mehrmals
aktualisiert, um Aenderungen bei Klassen, Funktionen und Zusammenhaenge zwischen Klassen abzubilden.
<br>[zurueck zum Wegweiser](#wegweiser)
### DDD
Die Domaenen wurden zu Beginn des Projekts entworfen und gemaess des Feedbacks auf 6 erhoeht. Die Domaenen und ihre Funktionen
wurden gemaess der Fachlichkeit im Kontext einer gelaeufigen Baeckerei entworfen und umgesetzt. Zu Beginn war aber noch
nicht wirklich klar, welche Funktionalitaeten wirklich implementiert werden, da fuer mich wichtig war, den Umfang des
Projekts so zu gestalten, dass ich es auch in der urspruenglich kuerzeren Umsetzungszeit schaffen kann. Demzufolge sind
Ideen des ersten Entwurfs wie im Verkaufsraum ein Tischmanagement einzurichten, sodass Kunden im Verkaufsraum auch
Backwaren und Getraenke direkt verzehren koennen, verworfen worden, um mehr Zeit fuer ein ordentliches Design von
den vorhandenen Geschaeftsprozessen zu gewaehrleisten. <br>
Aehnlich zu den UML-Diagrammen wurde auch auf das Eventstorming ein Auge behalten, um fuer Ideen und Funktionalitaeten
fuer mehr Qualitaet offen zu bleiben. Ideen, die engueltig verworfen wurden, wurden aus dem Diagramm entfernt. Die
im Git zu findende Version ist die finale, in der die Geschaeftsprozesse auch entsprechend ihren Domaenen zugeordnet sind. <br>
Die Beziehung der Domaenen hat sich ueber das Projekt insofern geaendert, als dass zu Beginn der Implementierung viel
Spaghetti-Code vorlag, der nicht der intialen Vorstellung der Beziehungen zwischen Domaenen entsprach. Diese Dissonanz
konnte erst mit Einfuehrung der Interaktionsschicht mit den Angestelltenklassen umgesetzt werden, sodass das finale Projekt
von der initialen Vorstellung nur gering abweicht. Abweichungen sind nur gering und dadurch erklaert, dass bei der Implementierung
die einfachste und verstaendlichste Loesung abwich. Die finale Loesung ist trotz Abweichung insofern in Ordnung, als dass
keine kreisfoermigen Abhaengigkeiten von Domaenen entstanden sind.
<br>[zurueck zum Wegweiser](#wegweiser)
### Metrics
Wie empfohlen wurde fuer das Projekt SonarQube genutzt. SonarQube war eine riesige Hilfe dabei, Fehler zu entdecken (vor
allem fuer eine Anfaengerin wie mich, die fuer erfahrene Entwickler offensichtliche Fehler nicht erkennt). SonarQube
war ueber das gesamte Projekt hinweg fuer mich das Werkzeug, an dass ich mich immer erinnern werde und fuer ein kuenftiges
Projekt von Beginn an einbeziehen wuerde. Das Einzige, was mich sehr geaergert hat, ist, dass es mir nicht gelungen ist, die 
Testcoverage in SonarQube darzustellen. Darin habe ich so viele Stunden gesteckt, weil die Testcoverage der Teil des Projekts
ist, auf den ich sehr stolz bin und den ich auch sehr priorisiert habe. Nichtsdestotrotz ist SonarQube
ein grossartiges Tool und hat mich stark dabei unterstuetzt zu einem Ergebnis zu kommen, mit dem ich zufrieden bin. <br>
Die schlechte Sicherheitsbewertung meines Projekts ist rein durch die Verwendung des random-Pakets in meinem Fluent Interface
bedingt, da fuer SonarCube dies keine sicheren Zufallsgeneratoren stellt. Da die Anwendung jedoch nur sehr klein ist und
das random-Paket ein gelaeufiges Beginner-Paket fuer Zufallsgeneratoren ist, wurde dieses trotzdem beibehalten. Die Prioritaet
wurde vor allem auf ein ascii-freundliches Benennungsschema gesetzt, das auch den herkoemmlichen Coding-Konventionen folgt.
<br>[zurueck zum Wegweiser](#wegweiser)
### Clean Code Development
Da ich nur eine voherige Coding-Erfahrung hatte, die mittlerweile 7 Jahre her ist, hatte ich vor der Umsetzung dieses Aspekts
den meisten Respekt. Die Lesbarkeit, Struktur und Einhaltung von Coding-Konventionen war ueber den Grossteil des Projekts einfach
grottig. Gleichzeitig ist das genau deswegen auch der Aspekt, bei dem ich am meisten dazugelernt und verbessert habe. Es
hat sehr viele Stunden und viel Lernarbeit auch ausserhalb des Projekts gebraucht, um Grundlagen der CCD-Prinzipien umzusetzen.
Zu wissen, dass das Projekt nun in vielerlei Hinsicht diesen Prinzipien entspricht, ist fuer mich ein grosser Erfolg.
<br>[zurueck zum Wegweiser](#wegweiser)
### Build
Es war auch meine erste Erfahrung mit Maven, dementsprechend ist die Demo bescheiden, aber tut, was sie soll. Um einmal kurz auf den
Abschnitt Functional Programming vorzugreifen - einige der dort geforderten Konzepte wie finale Datenstrukturen und private
Klassenattribute lassen sich in Python nicht umsetzen. Demzufolge habe ich diese in Java geschrieben, einen
Test dafuer verfasst und mit in die Maven-Demo gepackt. Das Aufsetzen eines Builds war fuer mich neu und ein wenig frustrierend,
weil es schwierig fuer mich war, Fehler zu finden und zu beheben, bis es funktioniert hat. Eine weitere Herausforderung,
deren Bewaelitgung ich als Erfolg verbuchen kann.
<br>[zurueck zum Wegweiser](#wegweiser)
### Continuous Delivery
Auch hier war es mein erstes Mal, eine Pipeline aufzusetzen. Erneute Frustration, wenn etwas nicht so lief wie es sollte.
Die entstandene Pipeline ist ein minimum value product, aber das war noetig, um so priorisieren zu koennen,
dass das Projekt eine gute Qualitaet erreicht.
<br>[zurueck zum Wegweiser](#wegweiser)
### Unit Tests
Nach den voherigen Punkten bin ich dankbar, dass ich mit Unit-Tests bekannten Boden betreten konnte. Ich bin ein grosser Fan
von Tests, da sie dabei helfen, Auswirkungen von funktionalen Aenderungen bei einer Klasse direkt pruefen zu koennen und zu
schauen, ob bei abhaengigen Klassen Fehler entstanden sind. Der Ansatz dabei war: jede Funktion, die eine nicht triviale Aufgabe
(z.B. Getter-Funktionen) erfuellt und eine Variable zurueckgibt wird geprueft. Dies konnte so auch umgesetzt werden. Ich habe
in einem Forum in Bezug auf side-effect free programming eine hitzige Diskussion zu der Verwendung von Exceptions gelesen - ich persoenlich positioniere
mich eher dazu, Funktionen moeglichst unabhaengig zu betrachten und lieber etwas mehr abzufangen als zu wenig. Dies begruende
ich so, dass es bei einer hypothetischen Weiterentwicklung des Projekts dabei hilft, moegliche Aenderungen zu pruefen und Integritaet
zu von Geschaeftsprozessen zu wahren. Dabei ist mir jedoch auch wichtig, dass nicht nur die Exceptions an sich fliegen, sondern
dass diese auch wiedergeben, was denn genau das Problem ist.
<br>[zurueck zum Wegweiser](#wegweiser)
### IDE
#### Lieblings-Tastenkombinationen
Alt Enter: <br>
Kontextmenue - immer dann nuetzlich, um Variablen oder Funktionen wiederzufinden, z.B. wenn man sich verschrieben hat oder Probleme mit der Sichtbarkeit bestehen. <br>
<br>
Alt F7: <br>
Nach dem Ueberarbeiten einer Funktion kann man so schnell suchen, wo sie ueberall vorkommt, um zu ueberpruefen, ob etwas kaputt gegangen ist. <br>
<br>
Shift F6: <br>
Dieser Shortcut hilft dabei, alle Variablen- / Funktionsnamen auf einmal umzubenennen. Wurde viel benutzt, um ein einheitliches Benennungsschema innerhalb einer Datei umzusetzen. <br>
<br>
Strg Shift R: <br>
Fuer das Refactoring wurde diese Tastenkombination genutzt, um ueber das gesamte Projekt hinweg Funktions- und Variablennamen so anzupassen, dass
ein uniformes Benennungsschema entsteht. Als Hilfe wurde Sonarqube genutzt, um problematische Bezeichnungen zu finden
und im Anschluss zu korrigieren. <br>
<br>
#### weitere Erlaeuterungen zur IDE
Da ich mit PyCharm die meisten Vorerfahrungen habe, wollte ich auch das Projekt darin gestalten. Im CS for Big Data Modul hatte ich ueber das 
Semester ersten Kontakt mit VSCode, ich hatte aber staendig Probleme und das Gefuehl, nicht wirklich damit warm zu werden.
Dementsprechend war PyCharm in gewisser Weise auch eine zwingende Wahl.
<br>[zurueck zum Wegweiser](#wegweiser)
### DSL Demo
Aehnlich wie bereits zu den UML-Diagrammen erwaehnt, hat mir auch die Erstellung des Sequenzdiagramms Spass gemacht. Es gibt
auch sehr schoen die Struktur wieder, die ein Geschaeftsprozess hat. Der erste Versuch eines Sequenzdiagramms hat mir deutlich
aufgezeigt, dass meine Funktionsstrukturen sehr wirr sind. Es liefert eine Anschaulichkeit, die das einfache Schreiben von Code
nicht liefern kann - vor allem dann, wenn Prozesse ueber mehrere Klassen verlaufen. Vor dem Aufsetzen von SonarQube war
dies meine erste Moeglichkeit, grundlegend die Ablaeufe meiner Funktionen zu ueberblicken und ueberdenken.
Auch dies wuerde ich fuer kuenftige Projekte wieder nutzen, auch wenn ich nun viel mehr Erfahrung habe und dementsprechend
mehr fuer strukturelle Konventionen sensibilisiert bin. Die Anschaulichkeit eines Geschaeftsprozesses auf diese Weise finde
ich zur Kommunikation in einem Team persoenlich sinnvoll.
<br>[zurueck zum Wegweiser](#wegweiser)
### Functional Programming
Diese Aufgabe hat mir persoenlich klargemacht, wie viel es noch zu lernen gibt. Die im Projekt verwendeten Funktionalitaeten
sind viel primitiver als die hier geforderten Aspekte. Ich habe diese Aspekte in mathematischen Kontexten umgesetzt, einfach
weil ich finde, dass mathematische Methoden sehr gut in Code umzusetzen sind. Vor allem bei der closure-Funktion hatte ich
das Gefuehl, wie wenn man zum ersten Mal eine Rekursion schreibt. Das ist einfach etwas ganz anderes fuer mich, was ich erstmal
verstehen muss. Auch hier habe ich ausserhalb des Projekts noch etwas weitergelesen und recherchiert, um mir zu helfen,
diese Art der Implementierung zu verstehen. Auch wenn die implementierten Funktionen letztendlich funktionieren und auch ihre
entsprechenden Tests bestehen, ist das funktionale Programmieren etwas, dass ich in Zukunft gerne noch mehr ueben wuerde,
um eine bessere Programmiererin zu werden. <br>
Im Maven-Projekt habe ich die Angestellten- und Chef-Klasse aus dem Projekt noch einmal auf Java umgesetzt und getestet.
Ich habe nicht viel Erfahrung mit Java, aber es war einfach noetig, um die geforderten Konzepte umzusetzen.
<br>[zurueck zum Wegweiser](#wegweiser)