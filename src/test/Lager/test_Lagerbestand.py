import pytest

from Lager.Lagerbestand import Lagerbestand

dummy_lagerbestand1 = {
        "Roggenmischbrot": 50,
        "Pfannkuchen": 50,
        "Kürbiskernbrötchen": 0
    }
dummy_lagerbestand2 = {
        "Roggenmischbrot": 50,
        "Pfannkuchen": 50,
        "Kürbiskernbrötchen": 50
    }

dummy_lagerbestand3 = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
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
    "Kürbiskerne": 50
}

test_bestand1 = Lagerbestand(dummy_lagerbestand1)
test_bestand2 = Lagerbestand(dummy_lagerbestand2)
test_bestand3 = Lagerbestand(dummy_lagerbestand3)

def test_prüft_fehlende_Waren():
    assert test_bestand3.prüft_fehlende_Waren() == ["Roggenmischbrot", "Dinkelbrot", "Bienenstich"]
    assert test_bestand3.prüft_fehlende_Waren(back = False) == ["Mehl", "Eier"]

def test_wird_gelagert():
    einzulagern1 = []
    einzulagern2 = ["Kürbiskernbrötchen"]
    einzulagern3 = ["Unsinnskuchen"]

    check_bestand = test_bestand1.prüft_Bestand()

    with pytest.raises(ValueError):
        assert test_bestand1.wird_gelagert(einzulagern1)
    test_bestand1.wird_gelagert(einzulagern2)
    assert check_bestand["Kürbiskernbrötchen"] == 50
    with pytest.raises(KeyError):
        assert test_bestand1.wird_gelagert(einzulagern3)

def test_wird_aus_dem_Lager_genommen():
    test_waren1 = []
    test_waren2 = ["Roggenmischbrot", "Pfannkuchen"]
    test_waren3 = ["Kürbiskernbrötchen", "Fakekuchen"]

    anzahl1 = 0
    anzahl2 = 51

    with pytest.raises(ValueError):
        assert test_bestand1.wird_aus_dem_Lager_genommen(test_waren1)
    assert test_bestand1.wird_aus_dem_Lager_genommen(test_waren2) == ["Roggenmischbrot", "Pfannkuchen"]
    with pytest.raises(KeyError):
        assert test_bestand1.wird_aus_dem_Lager_genommen(test_waren3) == ["Kürbiskernbrötchen"]
    with pytest.raises(ValueError):
        assert test_bestand1.wird_aus_dem_Lager_genommen(test_waren2, anzahl1)
    with pytest.raises(ValueError):
        assert test_bestand1.wird_aus_dem_Lager_genommen(test_waren2, anzahl2)