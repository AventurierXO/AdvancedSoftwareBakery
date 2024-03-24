import pytest

from Backstube.Baecker import Baecker
from Lager.Lagerbestand import Lagerbestand
from Backstube.Rezepte import Rezepte

dummy_lagerbestand1 = {
        "Roggenmischbrot": 0,
        "Pfannkuchen": 0,
        "Kuerbiskernbroetchen": 0,
        "Bienenstich": 0
    }
dummy_lagerbestand2 = {
    "Roggenmischbrot": 50,
    "Pfannkuchen": 50,
    "Kuerbiskernbroetchen": 50,
    "Bienenstich": 50
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
    "Kuerbiskerne": 50,
    "Mehl": 50,
    "Wasser": 50,
    "Hefe": 50
}

test_lagerbestand1 = Lagerbestand(dummy_lagerbestand1)
test_lagerbestand2 = Lagerbestand(dummy_lagerbestand2)
test_lagerbestand3 = Lagerbestand(dummy_lagerbestand3)

rezeptbuch = {
    "Weizensemmel": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1)],
    "Kuerbiskernbroetchen": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1), ("Kuerbiskerne", 1)],
    "Roggenmischbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Vollkornbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Dinkelbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Croissant": [("Mehl", 1), ("Butter", 1), ("Hefe", 1), ("Milch", 1), ("Zucker", 1)],
    "Streuselkuchen": [("Mehl", 4), ("Hefe", 1), ("Zucker", 3), ("Milch", 2), ("Butter", 3)],
    "Bienenstich": [("Mehl", 4), ("Milch", 4), ("Zucker", 1), ("Butter", 2), ("Hefe", 1)],
    "Pfannkuchen": [("Eier", 2), ("Mehl", 2), ("Milch", 1), ("Zucker", 1)]
}

testrezepte = Rezepte(rezeptbuch)
testbaecker1 = Baecker("Gustav", 2500, test_lagerbestand1, testrezepte)
testbaecker2 = Baecker("Hannah", 2500, test_lagerbestand2, testrezepte)
testbaecker3 = Baecker("Johann", 2500, test_lagerbestand3, testrezepte)

def test_liefere_backstuecke_korrekt():
    test_anforderung = ["Roggenmischbrot", "Pfannkuchen"]
    assert testbaecker2.liefere_backstuecke(test_anforderung) == ["Roggenmischbrot", "Pfannkuchen"]

def test_liefere_backstuecke_leere_bestellung():
    with pytest.raises(ValueError) as valueerror:
        testbaecker1.liefere_backstuecke([])
    assert str(valueerror.value) == "Es sollten keine Backstuecke geliefert werden, wenn keine Anforderung besteht!"

def test_liefere_backstuecke_falsche_backware():
    with pytest.raises(KeyError) as keyeerror:
        testbaecker3.liefere_backstuecke(["Fakekuchen"])
    assert str(keyeerror.value) == "'Die Ware gibt es im Lager nicht.'"

def test_liefere_backstuecke_zeug():
    with pytest.raises(ValueError) as valueerror:
        testbaecker3.liefere_backstuecke(["Roggenmischbrot"])
    assert str(valueerror.value) == "Es sind nicht mehr genug Stueck von Roggenmischbrot eingelagert."


def test_ermittelt_nachzufuellende_backstuecke_korrekt():
    assert testbaecker3.ermittle_nachzufuellende_backstuecke() == ["Roggenmischbrot", "Dinkelbrot", "Bienenstich"]

def test_backt_korrekt():
    bestellung_dummy1 = ["Roggenmischbrot"]
    check_lager = test_lagerbestand3.pruefe_bestand()
    testbaecker3.backe(bestellung_dummy1)
    assert check_lager["Mehl"] == 46
    assert check_lager["Hefe"] == 48
    assert check_lager["Wasser"] == 48
    assert check_lager["Roggenmischbrot"] == 50

def test_backt_falsches_gebaeck():
    with pytest.raises(KeyError) as keyerror:
        testbaecker3.backe(["Fakekuchen"])
    assert str(keyerror.value) == "'Für das Backstueck gibt es kein Rezept!'"

def test_produziere_backstueck_korrekt():
    test_backstuecke = ["Kuerbiskernbroetchen", "Dinkelbrot"]
    assert testbaecker3.produziere_backstueck(test_backstuecke) == ["Kuerbiskernbroetchen", "Dinkelbrot"]

def test_produziere_backstueck_leere_anforderung():
    with pytest.raises(ValueError) as valueerror:
        testbaecker3.produziere_backstueck([])
    assert str(valueerror.value) == "Die Liste zu produzierender Backstuecke sollte nicht leer sein!"

def test_produziere_backstueck_falsches_gebaeck():
    with pytest.raises(KeyError) as keyerror:
        testbaecker3.produziere_backstueck(["Fakekuchen"])
    assert str(keyerror.value) == "'Für das Backstueck gibt es kein Rezept!'"

def test_holt_zutaten_korrekt():
    test_zutatenliste = [("Mehl", 2), ("Wasser", 3)]
    check_bestand = test_lagerbestand3.pruefe_bestand()
    check_bestand_mehl = check_bestand["Mehl"]
    check_bestand_wasser = check_bestand["Wasser"]
    testbaecker3.hole_zutaten(test_zutatenliste)
    assert check_bestand["Mehl"] == check_bestand_mehl - 2
    assert check_bestand["Wasser"] == check_bestand_wasser - 3

def test_holt_zutaten_leere_zutatenliste():
    with pytest.raises(ValueError) as valueerror:
        testbaecker3.hole_zutaten([])
    assert str(valueerror.value) == "Die Zutatenliste kann nicht leer sein!"

def test_holt_zutaten_falsche_zutat():
    with pytest.raises(KeyError) as keyerror:
        testbaecker3.hole_zutaten([("Unsinnszutat", 2)])
    assert str(keyerror.value) == "'Die Ware gibt es im Lager nicht.'"

def test_holt_zutaten_anzahl_0():
    with pytest.raises(ValueError) as valueerror:
        testbaecker3.hole_zutaten([("Mehl", 0)])
    assert str(valueerror.value) == "Es muss mindestens ein Stueck der Ware aus dem Lager geholt werden bzw. nicht mehr als 50!"
