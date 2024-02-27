import pytest
from Auslage.Verkäufer_in import Verkäufer_in
from Büro.Chef import Chef
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

testbestand_dummy = ["Mehl", "Zucker", "Milch", "Eier", "Hefe", "Wasser", "Butter", "Kürbiskerne"]
testbestand = Lieferbestand(testbestand_dummy)

dummy_lagerbestand1 = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
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
    "Kürbiskerne": 50
}

dummy_lagerbestand2 = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
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
    "Kürbiskerne": 50
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
    "Kürbiskerne": 0.20
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
testverkäufer = Verkäufer_in("Anna", 2000, testauslage, testkasse, testkaffeemaschine)
test_name1 = "Johanna"
test_name2 = "Ruben"
test_lohn = 2000
test_position1 = "Verkäufer_in"
test_position2 = "Bäcker_in"

angestellte_bib = {
    "Anna": (2000, Verkäufer_in)
}

testchef1 = Chef("Joachim", 4000, testlagerbestand1, testlieferant, angestellte_bib)
testchef2 = Chef("Ole", 4000, testlagerbestand2, testlieferant, angestellte_bib)

def test_ändert_Lohn():
    test_lohn1 = 2500
    test_lohn2 = 0
    test_lohn3 = -100

    testchef1.ändere_Lohn_Mitarbeiter(testverkäufer, test_lohn1)
    assert testverkäufer.gebe_Lohn_an() == 2500
    with pytest.raises(ValueError):
        assert testchef1.ändere_Lohn_Mitarbeiter(testverkäufer, test_lohn2)
    with pytest.raises(ValueError):
        assert testchef1.ändere_Lohn_Mitarbeiter(testverkäufer, test_lohn3)

def test_Bestellung_erstellen():
    assert testchef1.Bestellung_erstellen() == ["Mehl", "Eier"]
def test_bestellt_Zutaten():
    check_bestand = testlagerbestand1.prüfe_Bestand()
    testchef1.bestelle_Zutaten()
    assert check_bestand["Mehl"] == 50
    assert check_bestand["Eier"] == 50
    with pytest.raises(ValueError):
        assert testchef2.bestelle_Zutaten()

def test_bezahlt_Rechnung():
    testrechnung1 = 0
    testrechnung2 = 100
    testrechnung3 = -100

    check_kasse_vor_einzahlung = testlieferant.kasse.Geld_in_Kasse()
    with pytest.raises(ValueError):
        assert testchef1.bezahlt_Rechnung(testrechnung1)
    testchef1.bezahlt_Rechnung(testrechnung2)
    check_kasse_nach_einzahlung = testlieferant.kasse.Geld_in_Kasse()
    assert check_kasse_nach_einzahlung == check_kasse_vor_einzahlung + testrechnung2
    with pytest.raises(ValueError):
        assert testchef1.bezahlt_Rechnung(testrechnung3)

def test_stellt_an():
    testchef1.stelle_an(test_name1, test_lohn, test_position1, testauslage, testkasse, testkaffeemaschine, testlagerbestand1, testrezepte)
    assert angestellte_bib[test_name1] == (test_lohn, test_position1)

    testchef1.stelle_an(test_name2, test_lohn, test_position2, testauslage, testkasse, testkaffeemaschine, testlagerbestand1, testrezepte)
    assert angestellte_bib[test_name2] == (test_lohn, test_position2)

    with pytest.raises(KeyError):
        assert testchef1.stelle_an(test_name1, test_lohn, test_position1, testauslage, testkasse, testkaffeemaschine, testlagerbestand1, testrezepte)

def test_kündigt():
    testchef1.kündige(testverkäufer)
    assert angestellte_bib == {'Johanna': (2000, 'Verkäufer_in'), 'Ruben': (2000, 'Bäcker_in')}
