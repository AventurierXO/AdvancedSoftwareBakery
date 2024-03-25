import pytest

from Verkaufsraum.Kunde import Kunde
from Auslage.Verkaeufer import Verkaeufer
from Auslage.Preisliste import Preisliste
from Auslage.Kasse import Kasse
from Auslage.AuslageTresen import AuslageTresen
from Auslage.Kaffeemaschine import Kaffeemaschine
from Lager.Lagerbestand import Lagerbestand
from Backstube.Baecker import Baecker
from Backstube.Rezepte import Rezepte

getraenke_optionen = ["Pot Kaffee", "Tasse Kaffee", "Latte Macchiato", "Cappucino", "Espresso", "Heisse Schokolade"]

testkaffeemaschine = Kaffeemaschine(getraenke_optionen)

preisliste = {
    "Weizensemmel": 0.30,
    "Kuerbiskernbroetchen": 0.40,
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
    "Heisse Schokolade": 2.50
}

testpreisliste = Preisliste(preisliste)

auslage_dummy = {
    "Weizensemmel": 50,
    "Kuerbiskernbroetchen": 50,
    "Roggenmischbrot": 50,
    "Vollkornbrot": 50,
    "Dinkelbrot": 50,
    "Croissant": 50,
    "Streuselkuchen": 0,
    "Bienenstich": 0,
    "Pfannkuchen": 50
}

testauslage = AuslageTresen(auslage_dummy)

dummy_lagerbestand = {
    "Weizensemmel": 50,
    "Kuerbiskernbroetchen": 50,
    "Roggenmischbrot": 0,
    "Vollkornbrot": 0,
    "Dinkelbrot": 0,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 50,
    "Pfannkuchen": 50,
    "Kuerbiskerne": 50,
    "Mehl": 50,
    "Wasser": 50,
    "Hefe": 50
}

testlagerbestand = Lagerbestand(dummy_lagerbestand)

rezeptbuch = {
    "Weizensemmel": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1)],
    "Kuerbiskernbroetchen": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1), ("Kuerbiskerne", 1)],
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
testbaecker = Baecker("Johanna", 2500, testlagerbestand, testrezepte)
testkasse = Kasse(10000, testpreisliste)
testverkaeufer = Verkaeufer("Alex", 2000, testauslage, testkasse, testkaffeemaschine)

def test_kassiere_geld_ein_korrekt():
    assert testverkaeufer.kassiere_geld_ein(5.7*100, testkunde) == 570

def test_kassiere_geld_ein_0_betrag():
    with pytest.raises(ValueError) as valueerror:
        testverkaeufer.kassiere_geld_ein(0, testkunde)
    assert str(valueerror.value) == "Der zu bezahlende Betrag kann nicht kleiner oder gleich 0 sein!"

def test_kassiere_geld_ein_negativer_betrag():
    with pytest.raises(ValueError) as valueerror:
        testverkaeufer.kassiere_geld_ein(-1, testkunde)
    assert str(valueerror.value) == "Der zu bezahlende Betrag kann nicht kleiner oder gleich 0 sein!"

def test_verkaufe_backwaren_korrekt():
    testbestellung = [("Weizensemmel", 3), ("Kuerbiskernbroetchen", 2)]
    rechnung = testverkaeufer.kasse.erstelle_rechnung(testbestellung)
    check_auslage = testverkaeufer.auslage.pruefe_bestand()
    check_kasse_vor_einzahlung = testverkaeufer.kasse.geld_in_kasse()
    testverkaeufer.verkaufe_backwaren(testbestellung, testkunde)

    assert check_auslage["Weizensemmel"] == 47
    assert check_auslage["Kuerbiskernbroetchen"] == 48
    check_kasse_nach_einzahlung = testverkaeufer.kasse.geld_in_kasse()
    assert check_kasse_nach_einzahlung == check_kasse_vor_einzahlung + rechnung

def test_verkaufe_backwaren_leere_bestellung():
    with pytest.raises(ValueError) as valueerror:
        testverkaeufer.verkaufe_backwaren([], testkunde)
    assert str(valueerror.value) == "Eine leere Bestellung kann nicht verarbeitet werden!"

def test_verkaufe_backwaren_falsche_backware():
    with pytest.raises(KeyError) as keyerror:
        testverkaeufer.verkaufe_backwaren([("Unsinnsbrot", 3)], testkunde)
    assert str(keyerror.value) == "'Die Backware gibt es in der Auslage nicht.'"

def test_verkaufe_getraenke_korrekt():
    test_bestellung = [("Latte Macchiato", 2), ("Pot Kaffee", 1)]
    rechnung = testverkaeufer.kasse.erstelle_rechnung(test_bestellung)
    check_kasse_vor_einzahlung = testverkaeufer.kasse.geld_in_kasse()
    testverkaeufer.verkaufe_getraenke(test_bestellung, testkunde)
    check_kasse_nach_einzahlung = testverkaeufer.kasse.geld_in_kasse()
    assert check_kasse_nach_einzahlung == check_kasse_vor_einzahlung + rechnung

def test_verkaufe_getaenke_leere_bestellung():
    with pytest.raises(ValueError) as valueerror:
        testverkaeufer.verkaufe_getraenke([], testkunde)
    assert str(valueerror.value) == "Eine leere Bestellung kann nicht verarbeitet werden!"

def test_verkaufe_getraenke_falsches_getraenk():
    with pytest.raises(ValueError) as valueerror:
        testverkaeufer.verkaufe_getraenke([("Unsinnsgetraenk", 2)], testkunde)
    assert str(valueerror.value) == "Diese Bestellung kann die Kaffeemaschine nicht zubereiten (falsches Getränk oder Anzahl)!"

def test_backwaren_nachbestellen_korrekt():
    testverkaeufer.bestelle_backwaren_nach(testbaecker)
    check_auslage = testverkaeufer.auslage.pruefe_bestand()
    assert check_auslage["Bienenstich"] == 50
    assert check_auslage["Streuselkuchen"] == 50