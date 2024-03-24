import pytest
from Auslage.Verkaeufer import Verkaeufer
from Buero.Chef import Chef
from Lager.Lagerbestand import Lagerbestand
from Lieferant.Lieferant import Lieferant
from Lieferant.Preisliste_Lieferant import Preisliste_Lieferant
from Lieferant.Lagerarbeiter import Lagerarbeiter
from Lieferant.Lieferbestand import Lieferbestand
from Lieferant.Kasse_Lieferant import Kasse_Lieferant
from Auslage.Auslage_Tresen import Auslage_Tresen
from Auslage.Kasse import Kasse
from Auslage.Preisliste import Preisliste
from Auslage.Kaffeemaschine import Kaffeemaschine
from Backstube.Rezepte import Rezepte

testbestand_dummy = ["Mehl", "Zucker", "Milch", "Eier", "Hefe", "Wasser", "Butter", "Kuerbiskerne"]
testbestand = Lieferbestand(testbestand_dummy)

dummy_lagerbestand1 = {
    "Weizensemmel": 50,
    "Kuerbiskernbroetchen": 50,
    "Roggenmischbrot": 0,
    "Vollkornbrot": 50,
    "Dinkelbrot": 0,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 0,
    "Pfannkuchen": 50,
    "Mehl": 0,
    "Zucker": 50,
    "Milch": 50,
    "Eier": 0,
    "Hefe": 50,
    "Butter": 50,
    "Wasser": 50,
    "Kuerbiskerne": 50
}

dummy_lagerbestand2 = {
    "Weizensemmel": 50,
    "Kuerbiskernbroetchen": 50,
    "Roggenmischbrot": 0,
    "Vollkornbrot": 50,
    "Dinkelbrot": 0,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 0,
    "Pfannkuchen": 50,
    "Mehl": 50,
    "Zucker": 50,
    "Milch": 50,
    "Eier": 50,
    "Hefe": 50,
    "Butter": 50,
    "Wasser": 50,
    "Kuerbiskerne": 50
}

testlagerbestand1 = Lagerbestand(dummy_lagerbestand1)
testlagerbestand2 = Lagerbestand(dummy_lagerbestand2)

preisliste = {
    "Mehl": 1.00,
    "Zucker": 1.00,
    "Milch": 1.10,
    "Eier": 2.50,
    "Hefe": 1.80,
    "Butter": 1.50,
    "Wasser": 0.50,
    "Kuerbiskerne": 0.20
}

testpreisliste1 = Preisliste_Lieferant(preisliste)
testpreisliste2 = Preisliste({})
testkasse = Kasse(100, testpreisliste2)
testkasse_lieferant = Kasse_Lieferant(1000, testpreisliste1)
testauslage = Auslage_Tresen({})
testkaffeemaschine = Kaffeemaschine([])
testrezepte = Rezepte({})
testlagerarbeiter = Lagerarbeiter(testbestand)
testlieferant = Lieferant("Testo", testlagerarbeiter, testbestand, testkasse_lieferant)
testverkaeufer = Verkaeufer("Anna", 2000, testauslage, testkasse, testkaffeemaschine)
test_name1 = "Anna"
test_name2 = "Ruben"
test_lohn = 2000
test_position1 = "Verkaeufer"
test_position2 = "Baecker"

angestellte_bib = {
    "Anna": (2000, Verkaeufer)
}

testchef1 = Chef("Joachim", 4000, testlagerbestand1, testlieferant, angestellte_bib)
testchef2 = Chef("Ole", 4000, testlagerbestand2, testlieferant, angestellte_bib)

def test_aendert_lohn_korrekt():
    testchef1.aendere_lohn_mitarbeiter(testverkaeufer, 2500)
    assert testverkaeufer.gebe_lohn_an() == 2500

def test_aendert_lohn_0():
    with pytest.raises(ValueError) as valueerror:
        testchef1.aendere_lohn_mitarbeiter(testverkaeufer, 0)
    assert str(valueerror.value) == "Der Lohn kann nicht kleiner oder gleich 0 sein."

def test_aendert_lohn_negativer_lohn():
    with pytest.raises(ValueError) as valueerror:
        testchef1.aendere_lohn_mitarbeiter(testverkaeufer, -100)
    assert str(valueerror.value) == "Der Lohn kann nicht kleiner oder gleich 0 sein."

def test_erstelle_bestellung_korrekt():
    assert testchef1.erstelle_bestellung() == ["Mehl", "Eier"]

def test_bestellt_zutaten_korrekt():
    check_bestand = testlagerbestand1.pruefe_bestand()
    testchef1.bestelle_zutaten()
    assert check_bestand["Mehl"] == 50
    assert check_bestand["Eier"] == 50

def test_bestellt_zutaten_unnoetig():
    with pytest.raises(ValueError) as valueerror:
        testchef2.bestelle_zutaten()
    assert str(valueerror.value) == "Im Moment muessen keine Zutaten nachbestellt werden."

def test_bezahle_rechnung_korrekt():
    testrechnung2 = 100
    check_kasse_vor_einzahlung = testlieferant.kasse.geld_in_kasse()
    testchef1.bezahle_rechnung(testrechnung2)
    check_kasse_nach_einzahlung = testlieferant.kasse.geld_in_kasse()
    assert check_kasse_nach_einzahlung == check_kasse_vor_einzahlung + testrechnung2

def test_bezahle_rechnung_0():
    with pytest.raises(ValueError) as valueerror:
        testchef1.bezahle_rechnung(0)
    assert str(valueerror.value) == "Die Rechnung muss groesser gleich 0 sein!"

def test_bezahle_rechnung_negative_zahl():
    with pytest.raises(ValueError) as valueerror:
        testchef1.bezahle_rechnung(-100)
    assert str(valueerror.value) == "Die Rechnung muss groesser gleich 0 sein!"

def test_stellt_an_korrekt():
    testchef1.stelle_an(test_name2, test_lohn, test_position2, testauslage, testkasse, testkaffeemaschine, testlagerbestand1, testrezepte)
    assert angestellte_bib[test_name2] == (test_lohn, test_position2)

def test_stellt_an_doppelter_mitarbeiter():
    with pytest.raises(KeyError) as keyerror:
        testchef1.stelle_an(test_name1, test_lohn, test_position1, testauslage, testkasse, testkaffeemaschine,
                                   testlagerbestand1, testrezepte)
    assert str(keyerror.value) == "'Es koennen keine zwei Angestellte denselben Namen haben! Bitte pruefen, ob der/die Angestellte bereits angelegt ist oder Namen durch Zahl ergaenzen!'"

def test_kuendigt_korrekt():
    testchef1.kuendige(testverkaeufer)
    assert angestellte_bib == {'Ruben': (2000, 'Baecker')}
