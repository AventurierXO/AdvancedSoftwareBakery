import pytest
from Verkaufsraum.BestellungBuilder import BestellungBuilder
from Auslage.Auslage_Tresen import Auslage_Tresen
from Auslage.Kaffeemaschine import Kaffeemaschine

auslage = {
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

getränkeoptionen = ["Pot Kaffee", "Tasse Kaffee", "Latte Macchiato", "Cappucino", "Espresso", "Heiße Schokolade"]

testauslage = Auslage_Tresen(auslage)
testkaffeemaschine = Kaffeemaschine(getränkeoptionen)
def test_Gebäckbestellung_erzeugen():
    bestellung = BestellungBuilder().Gebäckoptionen(testauslage.schaue_Waren_an()).Backbestellung_erzeugen()
    assert bestellung != []

def test_Getränkebestellung_erzeugen():
    bestellung = BestellungBuilder().Getränkeoptionen(testkaffeemaschine.schaue_Optionen_an()).Getränkebestellung_erzeugen()
    assert bestellung != []