import pytest
from Auslage.Auslage_Tresen import Auslage_Tresen

auslage1_basis = {
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

test_auslage1 = Auslage_Tresen(auslage1_basis)
test_auslage2 = Auslage_Tresen(auslage2_basis)

def test_erfasse_fehlende_backwaren():
    backwaren = test_auslage2.erfasse_fehlende_Backwaren()
    assert backwaren == ["Roggenmischbrot", "Vollkornbrot"]

def test_entnehme_backwerk():
    assert test_auslage1.entnehme_Backwerk([("Roggenmischbrot", 2), ("Kürbiskernbrötchen", 2)]) == [
        ("Roggenmischbrot", 2), ("Kürbiskernbrötchen", 2)]
    test_auslage1_save = test_auslage1.prüfe_Bestand()
    assert test_auslage1_save["Roggenmischbrot"] == 48
    assert test_auslage1_save["Kürbiskernbrötchen"] == 48
    with pytest.raises(ValueError):
        assert test_auslage1.entnehme_Backwerk([])
    with pytest.raises(KeyError):
        assert test_auslage1.entnehme_Backwerk([("Kartoffelbrot", 3)])
    with pytest.raises(ValueError):
        assert test_auslage1.entnehme_Backwerk([("Roggenmischbrot", 0)])
    with pytest.raises(ValueError):
        assert test_auslage1.entnehme_Backwerk([("Roggenmischbrot", 51)])

def test_fülle_bestand_nach():
    lieferung1 = []
    lieferung2 = ["Roggenmischbrot", "Vollkornbrot"]
    lieferung3 = ["Fakekuchen"]

    check_auslage = test_auslage2.prüfe_Bestand()
    with pytest.raises(ValueError):
        assert test_auslage2.fülle_Bestand_nach(lieferung1)
    test_auslage2.fülle_Bestand_nach(lieferung2)
    assert check_auslage["Roggenmischbrot"] == 50
    assert check_auslage["Vollkornbrot"] == 50
    with pytest.raises(KeyError):
        assert test_auslage2.fülle_Bestand_nach(lieferung3)

