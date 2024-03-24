import pytest
from Lieferant.Lagerarbeiter import Lagerarbeiter
from Lieferant.Lieferbestand import Lieferbestand

testbestand_dummy = ["Mehl", "Zucker", "Milch", "Eier", "Hefe", "Wasser", "Butter", "Kuerbiskerne"]
testbestand = Lieferbestand(testbestand_dummy)

testlagerarbeiter = Lagerarbeiter(testbestand)

def test_stellt_lieferung_zusammen_korrekt():
    assert testlagerarbeiter.stelle_lieferung_zusammen(["Mehl", "Wasser", "Hefe"]) == ["Mehl", "Wasser", "Hefe"]

def test_stellt_lieferung_zusammen_leere_bestellung():
    with pytest.raises(ValueError) as valueerror:
        testlagerarbeiter.stelle_lieferung_zusammen([])
    assert str(valueerror.value) == "Eine zu erfuellende Bestellung kann nicht leer sein!"

def test_stellt_lieferung_zusammen_falsche_bestellung():
    with pytest.raises(KeyError) as keyerror:
        testlagerarbeiter.stelle_lieferung_zusammen(["Unsinnszutat"])
    assert str(keyerror.value) == "'In der Bestellung darf sich keine Ware befinden, die der Lieferant nicht verkauft!'"