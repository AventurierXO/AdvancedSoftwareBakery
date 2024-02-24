import pytest
from Auslage.Kaffeemaschine import Kaffeemaschine

getränke_optionen = ["Pot Kaffee", "Tasse Kaffee", "Latte Macchiato", "Cappucino", "Espresso", "Heiße Schokolade"]

test_kaffeemaschine = Kaffeemaschine(getränke_optionen)
def test_macht_getränk_gibt_korrektes_getränk():
    test_getränke1 = [("Latte Macchiato", 2)]
    test_getränke2 = []
    test_getränke3 = [("Unsinnsbrühe", 2)]
    test_getränke4 = [("Latte Macchiato", 0)]

    assert test_kaffeemaschine.macht_Getränk(test_getränke1) == [("Latte Macchiato", 2)]
    with pytest.raises(ValueError):
        test_kaffeemaschine.macht_Getränk(test_getränke3)
    with pytest.raises(ValueError):
        test_kaffeemaschine.macht_Getränk(test_getränke2)
    with pytest.raises(ValueError):
        test_kaffeemaschine.macht_Getränk(test_getränke4)
