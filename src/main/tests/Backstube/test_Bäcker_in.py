import pytest

from Backstube.Bäcker_in import Bäcker_in
from Lager.Lagerbestand import Lagerbestand
from Backstube.Rezepte import Rezepte

dummy_lagerbestand1 = {
        "Roggenmischbrot": 0,
        "Pfannkuchen": 0,
        "Kürbiskernbrötchen": 0,
        "Bienenstich": 0
    }
dummy_lagerbestand2 = {
    "Roggenmischbrot": 50,
    "Pfannkuchen": 50,
    "Kürbiskernbrötchen": 50,
    "Bienenstich": 50
}

dummy_lagerbestand3 = {
    "Weizensemmel": 50,
    "Kürbiskernbrötchen": 50,
    "Roggenmischbrot": 0,
    "Vollkornbrot": -50,
    "Dinkelbrot": 0,
    "Croissant": 50,
    "Streuselkuchen": 50,
    "Bienenstich": 0,
    "Pfannkuchen": 50,
    "Kürbiskerne": 50,
    "Mehl": 50,
    "Wasser": 50,
    "Hefe": 50
}

test_lagerbestand1 = Lagerbestand(dummy_lagerbestand1)
test_lagerbestand2 = Lagerbestand(dummy_lagerbestand2)
test_lagerbestand3 = Lagerbestand(dummy_lagerbestand3)

rezeptbuch = {
    "Weizensemmel": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1)],
    "Kürbiskernbrötchen": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1), ("Kürbiskerne", 1)],
    "Roggenmischbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Vollkornbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Dinkelbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Croissant": [("Mehl", 1), ("Butter", 1), ("Hefe", 1), ("Milch", 1), ("Zucker", 1)],
    "Streuselkuchen": [("Mehl", 4), ("Hefe", 1), ("Zucker", 3), ("Milch", 2), ("Butter", 3)],
    "Bienenstich": [("Mehl", 4), ("Milch", 4), ("Zucker", 1), ("Butter", 2), ("Hefe", 1)],
    "Pfannkuchen": [("Eier", 2), ("Mehl", 2), ("Milch", 1), ("Zucker", 1)]
}

testrezepte = Rezepte(rezeptbuch)
testbäcker1 = Bäcker_in("Gustav", 2500, test_lagerbestand1, testrezepte)
testbäcker2 = Bäcker_in("Hannah", 2500, test_lagerbestand2, testrezepte)
testbäcker3 = Bäcker_in("Johann", 2500, test_lagerbestand3, testrezepte)

def test_liefere_Backstücke():
    test_anforderung1 = []
    test_anforderung2 = ["Roggenmischbrot", "Pfannkuchen"]
    test_anforderung3 = ["Kürbiskernbrötchen", "Fakekuchen"]
    test_anforderung4 = ["Bienenstich", "Roggenmischbrot"]

    with pytest.raises(ValueError):
        assert testbäcker1.liefere_Backstücke(test_anforderung1)
    with pytest.raises(ValueError):
        assert testbäcker2.liefere_Backstücke(test_anforderung1)
    assert testbäcker2.liefere_Backstücke(test_anforderung2) == ["Roggenmischbrot", "Pfannkuchen"]
    with pytest.raises(KeyError):
        assert testbäcker3.liefere_Backstücke(test_anforderung3) == ["Kürbiskernbrötchen"]
    with pytest.raises(ValueError):
        assert testbäcker2.liefere_Backstücke(test_anforderung4) == ["Bienenstich"]

def test_ermittelt_nachzufüllende_Backstücke():
    with pytest.raises(ValueError):
        assert testbäcker3.ermittle_nachzufüllende_Backstücke() == ["Roggenmischbrot", "Dinkelbrot", "Bienenstich"]

def test_backt():
    bestellung_dummy1 = ["Roggenmischbrot"]
    bestellung_dummy2 = ["Fakekuchen"]

    check_lager = test_lagerbestand3.prüfe_Bestand()

    testbäcker3.backe(bestellung_dummy1)
    assert check_lager["Mehl"] == 46
    assert check_lager["Hefe"] == 48
    assert check_lager["Wasser"] == 48
    assert check_lager["Roggenmischbrot"] == 50

    with pytest.raises(KeyError):
        assert testbäcker3.backe(bestellung_dummy2)
def test_produziere_Backstück():
    test_backstücke1 = []
    test_backstücke2 = ["Kürbiskernbrötchen", "Dinkelbrot"]
    test_backstücke3 = ["Fakekuchen"]

    with pytest.raises(ValueError):
        assert testbäcker3.produziere_Backstück(test_backstücke1)
    assert testbäcker3.produziere_Backstück(test_backstücke2) == ["Kürbiskernbrötchen", "Dinkelbrot"]
    with pytest.raises(KeyError):
        assert testbäcker3.produziere_Backstück(test_backstücke3)

def test_holt_Zutaten():
    test_zutatenliste1 = []
    test_zutatenliste2 = [("Mehl", 2), ("Wasser", 3)]
    test_zutatenliste3 = [("Unsinnszutat", 2)]
    test_zutatenliste4 = [("Mehl", 0)]
    check_bestand = test_lagerbestand3.prüfe_Bestand()
    check_bestand_mehl = check_bestand["Mehl"]
    check_bestand_wasser = check_bestand["Wasser"]
    with pytest.raises(ValueError):
        assert testbäcker3.hole_Zutaten(test_zutatenliste1)
    testbäcker3.hole_Zutaten(test_zutatenliste2)
    assert check_bestand["Mehl"] == check_bestand_mehl - 2
    assert check_bestand["Wasser"] == check_bestand_wasser - 3
    with pytest.raises(KeyError):
        testbäcker3.hole_Zutaten(test_zutatenliste3)
    with pytest.raises(ValueError):
        testbäcker3.hole_Zutaten(test_zutatenliste4)