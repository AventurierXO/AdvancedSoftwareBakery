import pytest

from Verkaufsraum.Kunde import Kunde
from Auslage.Verkäufer_in import Verkäufer_in
from Auslage.Preisliste import Preisliste
from Auslage.Kasse import Kasse
from Auslage.Auslage_Tresen import Auslage_Tresen
from Auslage.Kaffeemaschine import Kaffeemaschine
from Lager.Lagerbestand import Lagerbestand
from Backstube.Bäcker_in import Bäcker_in
from Backstube.Rezepte import Rezepte

getränke_optionen = ["Pot Kaffee", "Tasse Kaffee", "Latte Macchiato", "Cappucino", "Espresso", "Heiße Schokolade"]

testkaffeemaschine = Kaffeemaschine(getränke_optionen)

preisliste = {
    "Weizensemmel": 0.30,
    "Kürbiskernbrötchen": 0.40,
    "Roggenmischbrot": 2.00,
    "Vollkornbrot": 2.30,
    "Dinkelbrot": 2.10,
    "Croissant": 1.20,
    "Streuselkuchen": 1.40,
    "Bienenstich": 1.40,
    "Pfannkuchen": 1.20,
    "Pot Kaffee": 4.00,
    "Tasse Kaffee": 1.70,
    "Latte Macchiato": 2.50,
    "Cappuccino": 2.00,
    "Espresso": 1.80,
    "Heiße Schokolade": 2.50
}

testpreisliste = Preisliste(preisliste)

auslage_dummy = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
    "Roggenmischbrot": 50,
    "Vollkornbrot": 50,
    "Dinkelbrot": 50,
    "Croissant": 50,
    "Streuselkuchen": 0,
    "Bienenstich": 0,
    "Pfannkuchen": 50
}

testauslage = Auslage_Tresen(auslage_dummy)

dummy_lagerbestand = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
    "Roggenmischbrot": 0,
    "Vollkornbrot": 0,
    "Dinkelbrot": 0,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 50,
    "Pfannkuchen": 50,
    "Kürbiskerne": 50,
    "Mehl": 50,
    "Wasser": 50,
    "Hefe": 50
}

testlagerbestand = Lagerbestand(dummy_lagerbestand)

rezeptbuch = {
    "Weizensemmel": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1)],
    "Kürbiskernbrötchen": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1), ("Kürbiskerne", 1)],
    "Roggenmischbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Vollkornbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Dinkelbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Croissant": [("Mehl", 1), ("Butter", 1), ("Hefe", 1), ("Milch", 1), ("Zucker", 1)],
    "Streuselkuchen": [("Mehl", 4), ("Hefe", 1), ("Zucker", 3), ("Milch", 2), ("Butter", 3)],
    "Bienenstich": [("Mehl", 4), ("Milch", 4), ("Zucker", 1), ("Butter", 2), ("Hefe", 1)],
    "Pfannkuchen": [("Eier", 2), ("Mehl", 2), ("Milch", 1), ("Zucker", 1)]
}

testrezepte = Rezepte(rezeptbuch)

testkunde = Kunde("Julia")
testbäcker = Bäcker_in("Johanna", 2500, testlagerbestand, testrezepte)
testkasse = Kasse(10000, testpreisliste)
testverkäufer = Verkäufer_in("Alex", 2000, testauslage, testkasse, testkaffeemaschine)

def test_kassiere_Geld_ein():
    with pytest.raises(ValueError):
        assert testverkäufer.kassiere_Geld_ein(0, testkunde)
    with pytest.raises(ValueError):
        assert testverkäufer.kassiere_Geld_ein(-1, testkunde)
    assert testverkäufer.kassiere_Geld_ein(5.7, testkunde) == 5.7

def test_verkaufe_Backwaren():
    testbestellung1 = []
    testbestellung2 = [("Weizensemmel", 3), ("Kürbiskernbrötchen", 2)]
    testbestellung3 = [("Unsinnsbrot", 3)]

    rechnung = testverkäufer.kasse.erstelle_Rechnung(testbestellung2)
    check_auslage = testverkäufer.auslage.prüf_Bestand()
    check_kasse_vor_einzahlung = testverkäufer.kasse.geld_in_kasse()

    with pytest.raises(ValueError):
        testverkäufer.verkaufe_Backwaren(testbestellung1, testkunde)
    testverkäufer.verkaufe_Backwaren(testbestellung2, testkunde)
    assert check_auslage["Weizensemmel"] == 47
    assert check_auslage["Kürbiskernbrötchen"] == 48
    check_kasse_nach_einzahlung = testverkäufer.kasse.geld_in_kasse()
    assert check_kasse_nach_einzahlung == check_kasse_vor_einzahlung + rechnung
    with pytest.raises(KeyError):
        testverkäufer.verkaufe_Backwaren(testbestellung3, testkunde)

def test_verkaufe_Getränke():
    testbestellung1 = []
    testbestellung2 = [("Latte Macchiato", 2), ("Pot Kaffee", 1)]
    testbestellung3 = [("Unsinnsgetränk", 2)]
    rechnung = testverkäufer.kasse.erstelle_Rechnung(testbestellung2)
    check_kasse_vor_einzahlung = testverkäufer.kasse.geld_in_kasse()
    with pytest.raises(ValueError):
        testverkäufer.verkaufe_Getränke(testbestellung1, testkunde)
    testverkäufer.verkaufe_Getränke(testbestellung2, testkunde)
    check_kasse_nach_einzahlung = testverkäufer.kasse.geld_in_kasse()
    assert check_kasse_nach_einzahlung == check_kasse_vor_einzahlung + rechnung
    with pytest.raises(ValueError):
        testverkäufer.verkaufe_Getränke(testbestellung3, testkunde)

def test_Backwaren_nachbestellen():
    testverkäufer.Backwaren_nachbestellen(testbäcker)
    check_auslage = testverkäufer.auslage.prüf_Bestand()
    assert check_auslage["Bienenstich"] == 50
    assert check_auslage["Streuselkuchen"] == 50