import pytest
from Auslage.Kasse import Kasse
from Auslage.Preisliste import Preisliste
from Auslage.Verkäufer_in import Verkäufer_in
from Auslage.Auslage_Tresen import Auslage_Tresen
from Auslage.Kaffeemaschine import Kaffeemaschine

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
testkasse = Kasse(10000, testpreisliste)
testauslage = Auslage_Tresen({})
testkaffeemaschine = Kaffeemaschine([])
testverkäufer = Verkäufer_in("Alex", 2000, testauslage, testkasse, testkaffeemaschine)

def test_zahle_Geld_ein():
    testkasse.zahle_Geld_ein(200)
    assert testkasse.Geld_in_Kasse() == 10200
    with pytest.raises(ValueError):
        testkasse.zahle_Geld_ein(-200)
    with pytest.raises(ValueError):
        testkasse.zahle_Geld_ein(0)

def test_erstelle_Rechnung():
    test_einkauf1 = [("Pfannkuchen", 3), ("Roggenmischbrot", 2)]
    test_einkauf2 = []
    test_einkauf3 = [("Huggelmupf", 1)]

    rechnung = testkasse.erstelle_Rechnung(test_einkauf1,)
    with pytest.raises(ValueError):
        testkasse.erstelle_Rechnung(test_einkauf2)
    with pytest.raises(KeyError):
        testkasse.erstelle_Rechnung(test_einkauf3)
    assert rechnung == 7.6
