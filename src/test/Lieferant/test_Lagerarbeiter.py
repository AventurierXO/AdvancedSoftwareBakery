import pytest
from Lieferant.Lagerarbeiter import Lagerarbeiter
from Lieferant.Lieferbestand import Lieferbestand

testbestand_dummy = ["Mehl", "Zucker", "Milch", "Eier", "Hefe", "Wasser", "Butter", "Kürbiskerne"]
testbestand = Lieferbestand(testbestand_dummy)

testlagerarbeiter = Lagerarbeiter(testbestand)

def test_stellt_Lieferung_zusammen():
    test_bestellung1 = []
    test_bestellung2 = ["Unsinnszutat"]
    test_bestellung3 = ["Mehl", "Wasser", "Hefe"]

    with pytest.raises(ValueError):
        assert testlagerarbeiter.stellt_Lieferung_zusammen(test_bestellung1)
    with pytest.raises(ValueError):
        assert testlagerarbeiter.stellt_Lieferung_zusammen(test_bestellung2)
    assert testlagerarbeiter.stellt_Lieferung_zusammen(test_bestellung3) == ["Mehl", "Wasser", "Hefe"]