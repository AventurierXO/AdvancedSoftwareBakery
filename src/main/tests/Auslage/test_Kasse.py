import pytest
import math
from Auslage.Kasse import Kasse
from Auslage.Preisliste import Preisliste
from Auslage.Verkaeufer import Verkaeufer
from Auslage.AuslageTresen import AuslageTresen
from Auslage.Kaffeemaschine import Kaffeemaschine

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
testkasse = Kasse(10000, testpreisliste)
testauslage = AuslageTresen({})
testkaffeemaschine = Kaffeemaschine([])
testverkaeufer = Verkaeufer("Alex", 2000, testauslage, testkasse, testkaffeemaschine)

def test_zahle_geld_ein():
    testkasse.zahle_geld_ein(200)
    assert testkasse.geld_in_kasse() == 10200
    with pytest.raises(ValueError):
        testkasse.zahle_geld_ein(-200)
    with pytest.raises(ValueError):
        testkasse.zahle_geld_ein(0)

def test_erstelle_rechnung_korrekt():
    test_einkauf = [("Pfannkuchen", 3), ("Roggenmischbrot", 2)]
    rechnung = testkasse.erstelle_rechnung(test_einkauf)
    assert rechnung*100 == 760


def test_erstelle_rechnung_leerer_einkauf():
    with pytest.raises(ValueError) as valueerror:
        testkasse.erstelle_rechnung([])
    assert str(valueerror.value) == "Der zu bezahlende Einkauf kann nicht leer sein!"

def test_erstelle_rechnung_falsche_ware():
    with pytest.raises(KeyError) as keyerror:
        testkasse.erstelle_rechnung([("Huggelmupf", 1)])
    assert str(keyerror.value) == "'Die bestellte Ware Huggelmupf ist nicht in der Preisliste!'"
