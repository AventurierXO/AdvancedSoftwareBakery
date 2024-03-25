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
Weiterhin existiert eine Klasse BestellungBuilder, mithilfe dessen die Backbestellungen des Kunden generiert werden.

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
Dieser Absatz schliesst sich an die Ausfuehrungen zum Build an. Auch hier war es mein erstes Mal, eine Pipeline aufzusetzen. Erneute Frustration, wenn etwas nicht so lief wie es sollte.
Die entstandene Pipeline ist meines Erachtens ein minimum value product, aber das war noetig, um so priorisieren zu koennen,
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
### Code Dokumentation
Code Dokumentation fuehlt sich fuer mich manchmal schwierig an, weil man sich in die Perspektive von jemandem versetzen muss,
der die Funktionalitaeten nicht kennt, die man selbst implementiert hat. Die Code Dokumentation wurde einfach durch einen
Doc-String an Klassen und nicht-trivialen Funktionen erfuellt. Fuer die Klasse enthalten die DocStrings Informationen, was
die Klasse repraesentiert und welche Attribute sie hat. Fuer Funktionen wird kurz deren Zweck beschrieben. <br>
Dies ist nach meiner eigenen Einschaetzung gut gelungen. Aus meinem Werkstudentenjob kenne ich bereits Markdown-Dokumentationen,
allerdings fuer R in Form von Quarto-Dokumenten. Im Vergleich zu den Notizen, die noetig sind, um Gedankengaenge fuer z.B. eine Datenanalyse
festzuhalten und Entscheidungen zu begruenden, ist die Dokumentation hier sehr verschieden, da es bei der Code Dokumentation
nur um funktionale Aspekte geht. Bis zuletzt gab es DocStrings und ein README-Kapitel, das Geschaeftsprozesse 
mit Code-Snippets darlegte. Dies ist allerdings nicht Konvention und wurde dementsprechend angepasst.
#### Beispiel
[Beispiel Baecker](https://github.com/AventurierXO/AdvancedSoftwareBakery/blob/main/src/main/Backstube/Baecker.py) <br>
Zu Beginn wird dargelegt, was die Klasse Baecker ist und welche Attribute sie annimmt. Vor allem wir spezifiziert,
dass z.B. lagerbestand ein Objekt der Klasse Lagerbestand sein muss. Dies ist wichtig, um zu kommunizieren, was die Klasse
erwartet und vor allem braucht, um ihren Zweck erfuellen zu koennen. Uebergibt man z.B. einfach ein Dictionary mit Waren
und Anzahlen, so funktionieren die Funktionalitaeten, die in der Klasse Lagerbestand definiert sind, nicht fuer ein Dictionary.
Weiterhin wird fuer die Funktion liefere_backstuecke() dargelegt, was fuer einen Prozess diese umfasst. Die Funktionsnamen
fuer sich koennen zwar fuer sich sprechen, aber so hat man in einer Zeile eine konkrete Beschreibung, wie die folgenden Teilfunktionen
zusammenspielen.
<br>[zurueck zum Wegweiser](#wegweiser)