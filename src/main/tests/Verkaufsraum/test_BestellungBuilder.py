import pytest
from Verkaufsraum.BestellungBuilder import BestellungBuilder
from Auslage.Auslage_Tresen import Auslage_Tresen
from Auslage.Kaffeemaschine import Kaffeemaschine

auslage = {
    "Weizensemmel": 50,
    "Kuerbiskernbroetchen": 50,
    "Roggenmischbrot": 50,
    "Vollkornbrot": 50,
    "Dinkelbrot": 50,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 50,
    "Pfannkuchen": 50
}

getraenkeoptionen = ["Pot Kaffee", "Tasse Kaffee", "Latte Macchiato", "Cappucino", "Espresso", "Heisse Schokolade"]

testauslage = Auslage_Tresen(auslage)
testkaffeemaschine = Kaffeemaschine(getraenkeoptionen)
def test_gebaeckbestellung_erzeugen():
    bestellung = BestellungBuilder().gebaeckoptionen(testauslage.schaue_waren_an()).backbestellung_erzeugen()
    assert bestellung != []

def test_getraenkebestellung_erzeugen():
    bestellung = BestellungBuilder().getraenkeoptionen(testkaffeemaschine.schaue_optionen_an()).getraenkebestellung_erzeugen()
    assert bestellung != []