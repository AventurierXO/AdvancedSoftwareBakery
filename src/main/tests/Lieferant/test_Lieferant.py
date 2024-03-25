import pytest
from Lieferant.Lieferant import Lieferant
from Lieferant.PreislisteLieferant import PreislisteLieferant
from Lieferant.Lagerarbeiter import Lagerarbeiter
from Lieferant.Lieferbestand import Lieferbestand
from Lieferant.KasseLieferant import KasseLieferant
from Lager.Lagerbestand import Lagerbestand

testbestand_dummy = ["Mehl", "Zucker", "Milch", "Eier", "Hefe", "Wasser", "Butter", "Kuerbiskerne"]
testbestand = Lieferbestand(testbestand_dummy)

preisliste = {
    "Mehl": 1.00,
    "Zucker": 1.00,
    "Milch": 1.10,
    "Eier": 2.50,
    "Hefe": 1.80,
    "Butter": 1.50,
    "Wasser": 0.50,
    "Kuerbiskerne": 0.20
}

testpreisliste = PreislisteLieferant(preisliste)

dummy_lagerbestand = {
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

testlagerbestand = Lagerbestand(dummy_lagerbestand)
testlagerarbeiter = Lagerarbeiter(testbestand)
testkasse = KasseLieferant(10000, testpreisliste)
testlieferant = Lieferant("Testlieferant", testlagerarbeiter, testbestand, testkasse)

def test_erfuelle_lieferung_korrekt():
    rechnung = testlieferant.erfuelle_lieferung(["Mehl"], testlagerbestand)
    assert rechnung == 50

def test_erfuelle_lieferung_leere_bestellung():
    with pytest.raises(ValueError) as valueerror:
        testlieferant.erfuelle_lieferung([], testlagerbestand)
    assert str(valueerror.value) == "Eine leere Bestellung kann nicht erfuellt werden."

def test_erfuelle_lieferung_falsche_ware():
    with pytest.raises(KeyError) as keyerror:
        testlieferant.erfuelle_lieferung(["Unsinnszutat"], testlagerbestand)
    assert str(keyerror.value) == "'In der Bestellung darf sich keine Ware befinden, die der Lieferant nicht verkauft!'"

def test_kassiere_geld_ein_korrekt():
    check_kasse_vor_einzahlung = testkasse.geld_in_kasse()
    testlieferant.kassiere_geld_ein(100)
    check_kasse_nach_einzahlung = testkasse.geld_in_kasse()
    assert check_kasse_nach_einzahlung == check_kasse_vor_einzahlung + 100

def test_kassiere_geld_ein_0():
    with pytest.raises(ValueError) as valueerror:
        testlieferant.kassiere_geld_ein(0)
    assert str(valueerror.value) == "Der eingenommene Geldbetrag kann nicht kleiner gleich 0 sein!"

def test_kassiere_geld_ein_negativer_betrag():
    with pytest.raises(ValueError) as valueerror:
        testlieferant.kassiere_geld_ein(-100)
    assert str(valueerror.value) == "Der eingenommene Geldbetrag kann nicht kleiner gleich 0 sein!"