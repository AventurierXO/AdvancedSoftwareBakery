import pytest
from Auslage.Kaffeemaschine import Kaffeemaschine

getraenke_optionen = ["Pot Kaffee", "Tasse Kaffee", "Latte Macchiato", "Cappucino", "Espresso", "Heisse Schokolade"]

test_kaffeemaschine = Kaffeemaschine(getraenke_optionen)
def test_mache_getraenk_gibt_korrektes_getraenk():
    assert test_kaffeemaschine.mache_getraenk([("Latte Macchiato", 2)]) == [("Latte Macchiato", 2)]

def test_mache_getraenk_falsches_getraenk():
    with pytest.raises(ValueError) as valueerror:
        test_kaffeemaschine.mache_getraenk([("Unsinnsbruehe", 2)])
    assert str(valueerror.value) == "Diese Bestellung kann die Kaffeemaschine nicht zubereiten (falsches Getränk oder Anzahl)!"

def test_mache_getraenk_leere_Bestellung():
    with pytest.raises(ValueError) as valueerror:
        test_kaffeemaschine.mache_getraenk([])
    assert str(valueerror.value) == "Die Kaffeemaschine kann keine leere Bestellung annehmen!"

def test_mache_getraenk_anzahl_0():
    with pytest.raises(ValueError) as valueerror:
        test_kaffeemaschine.mache_getraenk([("Latte Macchiato", 0)])
    assert str(valueerror.value) == "Diese Bestellung kann die Kaffeemaschine nicht zubereiten (falsches Getränk oder Anzahl)!"

