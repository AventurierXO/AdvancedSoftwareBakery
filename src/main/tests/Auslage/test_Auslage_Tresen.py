import pytest
from Auslage.Auslage_Tresen import Auslage_Tresen

auslage1_basis = {
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

auslage2_basis = {
    "Weizensemmel": 50,
    "Kuerbiskernbroetchen": 50,
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
    test_backwaren = test_auslage2.erfasse_fehlende_backwaren()
    assert test_backwaren == ["Roggenmischbrot", "Vollkornbrot"]

def test_entnehme_backwerk_korrekt():
    assert test_auslage1.entnehme_backwerk([("Roggenmischbrot", 2), ("Kuerbiskernbroetchen", 2)]) == [
        ("Roggenmischbrot", 2), ("Kuerbiskernbroetchen", 2)]
    test_auslage1_save = test_auslage1.pruefe_bestand()
    assert test_auslage1_save["Roggenmischbrot"] == 48
    assert test_auslage1_save["Kuerbiskernbroetchen"] == 48

def test_entnehme_backwerk_leere_bestellung():
    with pytest.raises(ValueError) as valueerror:
        test_auslage1.entnehme_backwerk([])
    assert str(valueerror.value) == "Die Liste der zu entnehmenden Waren kann nicht leer sein!"

def test_entnehme_backwerk_nicht_vorhandenes_gebaeck():
    with pytest.raises(KeyError) as keyerror:
        test_auslage1.entnehme_backwerk([("Kartoffelbrot", 3)])
    assert str(keyerror.value) == "'Die Backware gibt es in der Auslage nicht.'"

def test_entnehme_backwerk_anzahl_0():
    with pytest.raises(ValueError) as valueerror:
        test_auslage1.entnehme_backwerk([("Roggenmischbrot", 0)])
    assert str(valueerror.value) == "Es koennen nicht 0 Backwerke entnommen werden!"

def test_entnehme_backwerk_anzahl_groesser_50():
    with pytest.raises(ValueError) as valueerror:
        test_auslage1.entnehme_backwerk([("Roggenmischbrot", 51)])
    assert str(valueerror.value) == "Es sind nicht genug Teile Roggenmischbrot vorhanden."

def test_fuelle_bestand_nach_korrekt():
    test_lieferung = ["Roggenmischbrot", "Vollkornbrot"]

    check_auslage = test_auslage2.pruefe_bestand()
    test_auslage2.fuelle_bestand_nach(test_lieferung)
    assert check_auslage["Roggenmischbrot"] == 50
    assert check_auslage["Vollkornbrot"] == 50

def test_fuelle_bestand_nach_falsche_backware():
    test_lieferung = ["Fakekuchen"]
    with pytest.raises(KeyError) as keyerror:
        test_auslage2.fuelle_bestand_nach(test_lieferung)
    assert str(keyerror.value) == "'Die Backware gibt es in der Auslage nicht.'"

def test_fuelle_bestand_nach_leere_lieferung():
    test_lieferung = []
    with pytest.raises(ValueError) as valueerror:
        test_auslage1.fuelle_bestand_nach(test_lieferung)
    assert str(valueerror.value) == "Um die Auslage befuellen zu koennen, muss die Lieferung Backwerke enthalten!"

