# Unit Tests
import random

import Auslage, Backstube, Büro, Lager, Lieferant, Verkaufsraum, main
import pytest

import Auslage.Auslage_Tresen
import Lager.Lagerbestand
import Verkaufsraum.Kunde

"""Verkauf von Waren"""

## Kunde bestellt Backware
def test_Backwarenbestellung_Kunde():
    kunde = Verkaufsraum.Kunde.Kunde("Polli")
    backwaren = Auslage.auslage.schaue_Waren_an()
    test_bestellung = kunde.kauft_Backwaren(Auslage.auslage)
    teilbestellung = test_bestellung[0]

    assert len(test_bestellung) > 0
    assert teilbestellung[0] in backwaren
    assert teilbestellung[1] >= 1 and teilbestellung[1] <= 4

## Verkäufer entnimmt Backwerke der Auslage
def test_Backwerke_aus_Auslage_nehmen():
    assert Auslage.auslage.entnehme_Backwerk([("Roggenmischbrot", 2), ("Kürbiskernbrötchen", 2)]) == [("Roggenmischbrot", 2), ("Kürbiskernbrötchen", 2)]
    with pytest.raises(ValueError):
        assert Auslage.auslage.entnehme_Backwerk([])
    with pytest.raises(KeyError):
        assert Auslage.auslage.entnehme_Backwerk([("Kartoffelbrot", 3)])
    with pytest.raises(ValueError):
        assert Auslage.auslage.entnehme_Backwerk([("Roggenmischbrot", 0)])
    with pytest.raises(ValueError):
        assert Auslage.auslage.entnehme_Backwerk([("Roggenmischbrot", 51)])

## Kunde bestellt Heißgetränk
def test_Kaffeebestellung_Kunde():
    kunde = Verkaufsraum.Kunde.Kunde("Polli")
    optionen = Auslage.kaffeemaschine.schaut_Optionen_an()
    test_bestellung = kunde.kauft_Heißgetränk(Auslage.kaffeemaschine)
    teilbestellung = test_bestellung[0]

    assert len(test_bestellung) > 0
    assert teilbestellung[0] in optionen
    assert teilbestellung[1] > 0

## Kaffeemaschine tut, was sie soll
def test_Kaffeemaschine():
    optionen = Auslage.kaffeemaschine.schaut_Optionen_an()
    test_getränk = random.choice(optionen)
    test_anzahl = random.randint(1, 2)
    fertiges_getränk1 = Auslage.kaffeemaschine.macht_Getränk([(test_getränk, test_anzahl)])
    teilbestellung = fertiges_getränk1[0]

    assert len(fertiges_getränk1) > 0
    assert teilbestellung[0] == test_getränk
    assert teilbestellung[1] == test_anzahl

    with pytest.raises(ValueError):
        Auslage.kaffeemaschine.macht_Getränk([("White Russian", test_anzahl)])
    with pytest.raises(ValueError):
        Auslage.kaffeemaschine.macht_Getränk([(test_getränk, 0)])
    with pytest.raises(ValueError):
        Auslage.kaffeemaschine.macht_Getränk([("White Russian", 0)])

## Verkäufer erstellt Rechnung
def test_Rechnung():
    verkäufer = Büro.testverkäufer
    test_einkauf1 = [("Pfannkuchen", 3), ("Roggenmischbrot", 2)]
    test_einkauf2 = []
    test_einkauf3 = [("Huggelmupf", 1)]
    rechnung = verkäufer.erstelle_Rechnung(test_einkauf1)
    with pytest.raises(ValueError):
        verkäufer.erstelle_Rechnung(test_einkauf2)
    with pytest.raises(KeyError):
        verkäufer.erstelle_Rechnung(test_einkauf3)

    assert rechnung == 7.6

## Geld einkassieren
def test_Geld_kassieren():
    with pytest.raises(ValueError):
        assert Büro.testverkäufer.kassiere_Geld_ein(rechnung = 0, kunde = Verkaufsraum.testkunde)
    with pytest.raises(ValueError):
        assert Büro.testverkäufer.kassiere_Geld_ein(rechnung = -1, kunde = Verkaufsraum.testkunde)
    assert Büro.testverkäufer.kassiere_Geld_ein(rechnung = 5.7, kunde = Verkaufsraum.testkunde) == 5.7

## Kunde bezahlt
def test_Rechnung_bezahlen():
    with pytest.raises(ValueError):
        assert Verkaufsraum.testkunde.bezahlen(rechnung = 0)
    with pytest.raises(ValueError):
        assert Verkaufsraum.testkunde.bezahlen(rechnung = -1)
    assert Verkaufsraum.testkunde.bezahlen(rechnung = 5.7) == 5.7

## Geld wird in Kasse eingezahlt
def test_in_Kasse_einzahlen():
    Auslage.kasse.geld_einzahlen(200)
    assert Auslage.kasse.geld_in_kasse() == 10200
    with pytest.raises(ValueError):
        Auslage.kasse.geld_einzahlen(-200)
    with pytest.raises(ValueError):
        Auslage.kasse.geld_einzahlen(0)

## Aufnahme von Bestellung
#def test_Bestellung_aufnehmen():
#    assert Büro.testverkäufer.verkaufe_Waren(Auslage.auslage, Auslage.kaffeemaschine, Auslage.kasse, Verkaufsraum.testkunde)

"""Nachfüllen der Auslage"""

## fehlende Backwaren checken
def test_Auslage_nach_fehlenden_Backwaren_checken():
    auslage_dummy1 = {
        "A": 50,
        "B": 0,
        "C": 50,
    }

    auslage_dummy2 = {
        "A": 50,
        "B": 50,
        "C": 50
    }

    auslage_dummy3 = {
        "A": 0,
        "B": 0,
        "C": -10
    }
    test_auslage1 = Auslage.Auslage_Tresen.Auslage_Tresen(auslage_dummy1)
    assert test_auslage1.erfasst_fehlende_Backwaren() == ["B"]
    test_auslage2 = Auslage.Auslage_Tresen.Auslage_Tresen(auslage_dummy2)
    assert test_auslage2.erfasst_fehlende_Backwaren() == []
    test_auslage3 = Auslage.Auslage_Tresen.Auslage_Tresen(auslage_dummy3)
    with pytest.raises(ValueError):
        assert test_auslage3.erfasst_fehlende_Backwaren()

## Lieferung von Backwerken testen
def test_Bäcker_liefert_Backstücke():
    test_anforderung1 = []
    test_anforderung2 = ["Roggenmischbrot", "Pfannkuchen"]
    test_anforderung3 = ["Kürbiskernbrötchen", "Fakekuchen"]
    test_anforderung4 = ["Bienenstich", "Roggenmischbrot"]

    dummy_lagerbestand1 = {
        "Roggenmischbrot": 0,
        "Pfannkuchen": 0,
        "Kürbiskernbrötchen": 0,
        "Bienenstich": 0
    }
    dummy_lagerbestand2 = {
        "Roggenmischbrot": 50,
        "Pfannkuchen": 50,
        "Kürbiskernbrötchen": 50,
        "Bienenstich": 50
    }
    test_lagerbestand1 = Lager.Lagerbestand.Lagerbestand(dummy_lagerbestand1)
    test_lagerbestand2 = Lager.Lagerbestand.Lagerbestand(dummy_lagerbestand2)

    with pytest.raises(ValueError):
        assert Büro.testbäcker.liefert_Backstücke(test_anforderung1, test_lagerbestand1)
    with pytest.raises(ValueError):
        assert Büro.testbäcker.liefert_Backstücke(test_anforderung1, test_lagerbestand2)
    with pytest.raises(ValueError):
        assert Büro.testbäcker.liefert_Backstücke(test_anforderung2, test_lagerbestand1)
    with pytest.raises(KeyError):
        assert Büro.testbäcker.liefert_Backstücke(test_anforderung3, test_lagerbestand2) == ["Kürbiskernbrötchen"]
    assert Büro.testbäcker.liefert_Backstücke(test_anforderung2, test_lagerbestand2) == test_anforderung2
    assert Büro.testbäcker.liefert_Backstücke(test_anforderung4, test_lagerbestand2) == ["Bienenstich"]

## Nehmen von Backwaren aus dem Lager testen
def test_Waren_aus_dem_Lager_nehmen():
    test_waren1 = []
    test_waren2 = ["Roggenmischbrot", "Pfannkuchen"]
    test_waren3 = ["Kürbiskernbrötchen", "Fakekuchen"]
    test_waren4 = ["Roggenmischbrot", "Bienenstich"]

    anzahl1 = 0
    anzahl2 = 51

    with pytest.raises(ValueError):
        assert Lager.testbestand.wird_aus_dem_Lager_genommen(test_waren1)
    assert Lager.testbestand.wird_aus_dem_Lager_genommen(test_waren2)
    with pytest.raises(KeyError):
        assert Lager.testbestand.wird_aus_dem_Lager_genommen(test_waren3) == ["Kürbiskernbrötchen"]
    assert Lager.testbestand.wird_aus_dem_Lager_genommen(test_waren4) == ["Bienenstich"]
    with pytest.raises(ValueError):
        assert Lager.testbestand.wird_aus_dem_Lager_genommen(test_waren2, anzahl1)
    with pytest.raises(ValueError):
        assert Lager.testbestand.wird_aus_dem_Lager_genommen(test_waren2, anzahl2)

## Auffüllen der Auslage testen
def test_auffüllen_der_Auslage():
    lieferung1 = []
    lieferung2 = ["Roggenmischbrot", "Pfannkuchen"]
    lieferung3 = ["Kürbiskernbrötchen", "Fakekuchen"]

    check_auslage = Auslage.auslage.prüf_Bestand()
    check_roggenmischbrot = check_auslage["Roggenmischbrot"]
    check_pfannkuchen = check_auslage["Pfannkuchen"]
    check_kürbiskernbrötchen = check_auslage["Kürbiskernbrötchen"]
    with pytest.raises(ValueError):
        assert Auslage.auslage.fülle_Bestand_nach(lieferung1)
    Auslage.auslage.fülle_Bestand_nach(lieferung2)
    with pytest.raises(KeyError):
        assert Auslage.auslage.fülle_Bestand_nach(lieferung3)

    assert (check_auslage["Roggenmischbrot"] - check_roggenmischbrot)== 50
    assert (check_auslage["Pfannkuchen"] - check_pfannkuchen)== 50
    assert (check_auslage["Kürbiskernbrötchen"] - check_kürbiskernbrötchen)== 50

"""Tests zum Backprozess"""

## Checken des Lagers testen
def test_Lagerbestand_checken():
    test_bestand_basis = {
        "Weizensemmel": 50,
        "Kürbiskernbrötchen": 50,
        "Roggenmischbrot": 0,
        "Vollkornbrot": -50,
        "Dinkelbrot": 0,
        "Croissant": 50,
        "Streuselkuchen": 50,
        "Bienenstich": 0,
        "Pfannkuchen": 50
    }

    test_bestand = Lager.Lagerbestand.Lagerbestand(test_bestand_basis)

    with pytest.raises(ValueError):
        assert Büro.testbäcker.ermittelt_nachzufüllende_backstücke(test_bestand) == ["Roggenmischbrot", "Dinkelbrot", "Bienenstich"]

## Backzutaten aus dem Lager holen
def test_Backzutaten_holen():
    test_zutatenliste1 = [("Mehl", 2)]
    test_zutatenliste2 = []
    test_zutatenliste3 = [("Fakezutat", 3)]

    assert Lager.testbestand.wird_aus_dem_Lager_genommen([test_zutatenliste1[0][0]], test_zutatenliste1[0][1]) == ["Mehl"]
    with pytest.raises(ValueError):
        assert Lager.testbestand.wird_aus_dem_Lager_genommen(test_zutatenliste2)
    with pytest.raises(KeyError):
        assert Lager.testbestand.wird_aus_dem_Lager_genommen([test_zutatenliste3[0][0]], test_zutatenliste3[0][1])

def test_produziere_Backstücke():
    test_backstücke1 = []
    test_backstücke2 = ["Roggenmischbrot", "Bienenstich"]
    test_backstücke3 = ["Fakekuchen"]

    with pytest.raises(ValueError):
        assert Büro.testbäcker.produziere_Backstück(test_backstücke1, Lager.testbestand)
    assert Büro.testbäcker.produziere_Backstück(test_backstücke2, Lager.testbestand) == ["Roggenmischbrot", "Bienenstich"]
    with pytest.raises(KeyError):
        assert Büro.testbäcker.produziere_Backstück(test_backstücke3, Lager.testbestand)

def test_backen():
    lagerbestand_dummy1 = {
        "Mehl": 50,
        "Hefe": 50,
        "Wasser": 50,
        "Roggenmischbrot": 50
    }

    lagerbestand_dummy2 = {
        "Mehl": 0,
        "Hefe": 0,
        "Wasser": 0
    }

    test_lagerbestand1 = Lager.Lagerbestand.Lagerbestand(lagerbestand_dummy1)
    test_lagerbestand2 = Lager.Lagerbestand.Lagerbestand(lagerbestand_dummy2)
    bestellung_dummy1 = ["Roggenmischbrot"]
    bestellung_dummy2 = ["Fakekuchen"]

    check_lager1 = test_lagerbestand1.prüft_Bestand()

    Büro.testbäcker.backt(test_lagerbestand1, bestellung_dummy1)

    assert check_lager1["Mehl"] == 46
    assert check_lager1["Hefe"] == 48
    assert check_lager1["Wasser"] == 48
    assert check_lager1["Roggenmischbrot"] == 100

    with pytest.raises(ValueError):
        assert Büro.testbäcker.backt(test_lagerbestand2, bestellung_dummy1)
    with pytest.raises(KeyError):
        assert Büro.testbäcker.backt(test_lagerbestand1, bestellung_dummy2)

"""Test der Lohnänderung"""

def test_lohnänderung():
    test_lohn1 = 2500
    test_lohn2 = 0
    test_lohn3 = -100

    Büro.testchef.ändert_lohn(Büro.testverkäufer, test_lohn1)
    assert Büro.testverkäufer.gibt_Lohn_an() == 2500
    with pytest.raises(ValueError):
        assert Büro.testchef.ändert_lohn(Büro.testverkäufer, test_lohn2)
    with pytest.raises(ValueError):
        assert Büro.testchef.ändert_lohn(Büro.testverkäufer, test_lohn3)

"""Test für die Nachbestellung von Zutaten durch den Chef"""

def test_Bestellung_erstellen():
    lagerbestand_dummy1 = {
        "Mehl": 50,
        "Zucker": 50,
        "Milch": 50,
        "Eier": 50,
        "Hefe": 50,
        "Butter": 50,
        "Wasser": 50,
        "Kürbiskerne": 50
    }

    lagerbestand_dummy2 = {
        "Mehl": 0,
        "Zucker": 50,
        "Milch": 50,
        "Eier": 50,
        "Hefe": 50,
        "Butter": 50,
        "Wasser": 50,
        "Kürbiskerne": 50
    }

    test_bestand1 = Lager.Lagerbestand.Lagerbestand(lagerbestand_dummy1)
    test_bestand2 = Lager.Lagerbestand.Lagerbestand(lagerbestand_dummy2)
    check_bestand1 = test_bestand1.prüft_Bestand()

    Büro.testchef.Bestellung_erstellen(test_bestand1)
    assert check_bestand1["Mehl"] == 50
    assert check_bestand1["Wasser"] == 50
    assert check_bestand1["Hefe"] == 50

    assert Büro.testchef.Bestellung_erstellen(test_bestand2) == ["Mehl"]

def test_Bestellung_zusammenstellen_Lieferant():
    test_bestellung1 = []
    test_bestellung2 = ["Unsinnszutat"]
    test_bestellung3 = ["Mehl", "Wasser", "Hefe"]

    with pytest.raises(ValueError):
        assert Lieferant.testlagerarbeiter.stellt_Lieferung_zusammen(test_bestellung1)
    with pytest.raises(ValueError):
        assert Lieferant.testlagerarbeiter.stellt_Lieferung_zusammen(test_bestellung2)
    assert Lieferant.testlagerarbeiter.stellt_Lieferung_zusammen(test_bestellung3) == ["Mehl", "Wasser", "Hefe"]

def test_Rechnung_für_Lieferung():
    test_lieferung1 = []
    test_lieferung2 = ["Mehl", "Wasser", "Hefe"]
    test_anzahl = 0

    with pytest.raises(ValueError):
        assert Lieferant.testlieferant.erstellt_Rechnung(test_lieferung1)
    with pytest.raises(ValueError):
        assert Lieferant.testlieferant.erstellt_Rechnung(test_lieferung2, test_anzahl)
    assert Lieferant.testlieferant.erstellt_Rechnung(test_lieferung2) == 50 * (1.00 + 0.50 + 1.80)

def test_erfüllt_Lieferung():
    test_bestellung1 = []
    test_bestellung2 = ["Unsinnszutat"]
    test_bestellung3 = ["Mehl", "Wasser", "Hefe"]

    with pytest.raises(ValueError):
        Lieferant.testlieferant.erfüllt_Lieferung(test_bestellung1)
    with pytest.raises(ValueError):
        Lieferant.testlieferant.erfüllt_Lieferung(test_bestellung2)
    assert Lieferant.testlieferant.erfüllt_Lieferung(test_bestellung3) == 50 * (1.00 + 0.50 + 1.80)

# Objekte für Verkaufsraum
testkunde = Kunde("Alexandra")

# Objekte für Lieferant
bestand = ["Mehl", "Zucker", "Milch", "Eier", "Hefe", "Wasser", "Butter", "Kürbiskerne"]

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

testlieferbestand = Lieferbestand(bestand)
testlieferant = Lieferant("Speedy Food")
testlagerarbeiter = Lagerarbeiter()
testpreisliste = Preisliste(preisliste)

# Objekte für Lager
lagerbestand = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
    "Roggenmischbrot": 50,
    "Vollkornbrot": 50,
    "Dinkelbrot": 50,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 50,
    "Pfannkuchen": 50,
    "Mehl": 50,
    "Zucker": 50,
    "Milch": 30,
    "Eier": 30,
    "Hefe": 50,
    "Butter": 50,
    "Wasser": 50,
    "Kürbiskerne": 50
}

testbestand = Lagerbestand(lagerbestand)

# Objekte für Büro
testchef = Chef("Jana", 4000)
testverkäufer = Verkäufer_in("Alexander", 2000)
testbäcker = Bäcker_in("Linda", 3000)

# Objekte für Backstube
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

rezepte = Rezepte(rezeptbuch)

# Objekte für Auslage
auslage_basis = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
    "Roggenmischbrot": 50,
    "Vollkornbrot": 50,
    "Dinkelbrot": 50,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 50,
    "Pfannkuchen": 50
}

# zum Testen fürs Nachfüllen
auslage2_basis = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
    "Roggenmischbrot": 0,
    "Vollkornbrot": 0,
    "Dinkelbrot": 50,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 50,
    "Pfannkuchen": 50
}

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

getränke_optionen = ["Pot Kaffee", "Tasse Kaffee", "Latte Macchiato", "Cappucino", "Espresso", "Heiße Schokolade"]

kasse = Kasse(10000)
auslage = Auslage_Tresen(auslage_basis)
preisliste = Preisliste(preisliste)
auslage2 = Auslage_Tresen(auslage2_basis)
kaffeemaschine = Kaffeemaschine(getränke_optionen)