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

Der Kunde startet einen Verkaufsprozess. Es gibt zwei verschiedene Verkaufsprozesse: einen für Getränke und einen für Backwaren.

Die Klasse Kunde wird folgendermaßen intialisiert:

```
class Kunde:
    def __init__(self, name):
        self.__name = name
```

Bei der Klasse Kunde handelt es sich um eine sehr generische Klasse, die lediglich einen Namen besitzt. Da Kunden mit einem beliebigen Akteur der Klasse Verkäufer_in interagieren können, wird dem Kunden kein bestimmter Verkäufer bei der Initialisierung zugeordnet. Weiterhin besitzt der Kunde keine Werkzeuge, mit denen er interagieren muss, um seine Rolle zu erfüllen.

Im Folgenden wird zunächst der Bestellprozess für eine Backwarenbestellung vorgestellt:

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
Beim Aufruf der Funktion wird ein Akteur von der Klasser Verkäufer_in und ein Objekt der Klasse Auslage_Tresen zugeordnet. Per Zufall wird eine Bestellung generiert, die alle möglichen Backwaren der Auslage enthalten kann. Dazu wird zunächst zufällig bestimmt, wie viele verschiedene Waren bestellt werden. Danach werden die Bestelloptionen bzw. eine Liste der zum Verkauf stehenden Backwaren generiert, aus der dann viermal zufällig ein Item gezogen wird, das bestellt wird. Im nächsten Schritt wird dann noch die Anzahl, die von dem Backwerk bestellt wird, zufällig gezogen. Sowohl das gewählte Backwerk als auch die Anzahl werden gemeinsam in einem Tupel gespeichert und an die Liste Bestellung angehängt.
Nachdem die Liste bestellter Waren fertig generiert ist, wird sie dem zugeordneten Verkäufer übergeben und sein Verkaufsprozess wird gestartet.
Die Größe der Bestellungen und die Menge, in der Backwaren bestellt werden können, wurde auf maximal 4 begrenzt. Diese Begrenzung wurde willkürlich getroffen, um einen realistischen Kauf zu simulieren. Eine leere Bestellung und sehr große Bestellungen, die die Bestände "sprengen", wurden beide als nicht sinnvoll empfunden und deswegen ausgeschlossen.