import pytest

from Lager.Lagerbestand import Lagerbestand

dummy_lagerbestand1 = {
        "Roggenmischbrot": 50,
        "Pfannkuchen": 50,
        "Kuerbiskernbroetchen": 0
    }
dummy_lagerbestand2 = {
        "Roggenmischbrot": 50,
        "Pfannkuchen": 50,
        "Kuerbiskernbroetchen": 50
    }

dummy_lagerbestand3 = {
    "Weizensemmel": 50,
    "Kuerbiskernbroetchen": 50,
    "Roggenmischbrot": 0,
    "Vollkornbrot": 50,
    "Dinkelbrot": 0,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 0,
    "Pfannkuchen": 50,
    "Mehl": 0,
    "Zucker": 50,
    "Milch": 50,
    "Eier": 0,
    "Hefe": 50,
    "Butter": 50,
    "Wasser": 50,
    "Kuerbiskerne": 50
}

test_bestand1 = Lagerbestand(dummy_lagerbestand1)
test_bestand2 = Lagerbestand(dummy_lagerbestand2)
test_bestand3 = Lagerbestand(dummy_lagerbestand3)

def test_prueft_fehlende_waren_korrekt():
    assert test_bestand3.pruefe_fehlende_waren() == ["Roggenmischbrot", "Dinkelbrot", "Bienenstich"]
    assert test_bestand3.pruefe_fehlende_waren(back = True) == ["Roggenmischbrot", "Dinkelbrot", "Bienenstich"]
    assert test_bestand3.pruefe_fehlende_waren(back = False) == ["Mehl", "Eier"]

def test_lagere_ein_korrekt():
    check_bestand = test_bestand1.pruefe_bestand()
    test_bestand1.lagere_ein(["Kuerbiskernbroetchen"])
    assert check_bestand["Kuerbiskernbroetchen"] == 50

def test_lagere_ein_leere_lieferung():
    with pytest.raises(ValueError) as valueerror:
        test_bestand1.lagere_ein([])
    assert str(valueerror.value) == "Eine Liste einzulagernder Waren darf nicht leer sein!"

def test_lagere_ein_falsche_ware():
    with pytest.raises(KeyError) as keyerror:
        test_bestand1.lagere_ein(["Unsinnskuchen"])
    assert str(keyerror.value) == "'Die Ware gibt es im Lager nicht.'"

def test_wird_aus_dem_lager_genommen_korrekt():
    assert test_bestand1.nimm_aus_dem_lager(["Roggenmischbrot", "Pfannkuchen"]) == ["Roggenmischbrot", "Pfannkuchen"]

def test_wird_aus_dem_lager_genommen_falsche_ware():
    with pytest.raises(KeyError) as keyerror:
        test_bestand1.nimm_aus_dem_lager(["Fakekuchen"])
    assert str(keyerror.value) == "'Die Ware gibt es im Lager nicht.'"

def test_nimm_aus_dem_lager_anzahl_0():
    with pytest.raises(ValueError) as valueerror:
        test_bestand1.nimm_aus_dem_lager(["Roggenmischbrot"], 0)
    assert str(valueerror.value) == "Es muss mindestens ein Stueck der Ware aus dem Lager geholt werden bzw. nicht mehr als 50!"

def test_nimm_aus_dem_lager_anzahl_51():
    with pytest.raises(ValueError) as valueerror:
        test_bestand1.nimm_aus_dem_lager(["Roggenmischbrot"], 51)
    assert str(valueerror.value) == "Es muss mindestens ein Stueck der Ware aus dem Lager geholt werden bzw. nicht mehr als 50!"