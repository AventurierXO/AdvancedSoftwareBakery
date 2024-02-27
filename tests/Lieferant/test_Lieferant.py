import pytest
from Lieferant.Lieferant import Lieferant
from Lieferant.Preisliste_Lieferant import Preisliste_Lieferant
from Lieferant.Lagerarbeiter import Lagerarbeiter
from Lieferant.Lieferbestand import Lieferbestand
from Lieferant.Kasse_Lieferant import Kasse_Lieferant
from Lager.Lagerbestand import Lagerbestand

testbestand_dummy = ["Mehl", "Zucker", "Milch", "Eier", "Hefe", "Wasser", "Butter", "Kürbiskerne"]
testbestand = Lieferbestand(testbestand_dummy)

preisliste = {
    "Mehl": 1.00,
    "Zucker": 1.00,
    "Milch": 1.10,
    "Eier": 2.50,
    "Hefe": 1.80,
    "Butter": 1.50,
    "Wasser": 0.50,
    "Kürbiskerne": 0.20
}

testpreisliste = Preisliste_Lieferant(preisliste)

dummy_lagerbestand = {
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

testlagerbestand = Lagerbestand(dummy_lagerbestand)
testlagerarbeiter = Lagerarbeiter(testbestand)
testkasse = Kasse_Lieferant(10000, testpreisliste)
testlieferant = Lieferant("Testlieferant", testlagerarbeiter, testbestand, testkasse)

def test_erstelle_Rechnung():
    test_einkauf1 = ["Mehl"]
    test_einkauf2 = []
    test_einkauf3 = ["Unsinnszutat"]

    rechnung = testlieferant.kasse.erstelle_Rechnung_Lieferung(test_einkauf1)
    assert rechnung == 50
    with pytest.raises(ValueError):
        testlieferant.kasse.erstelle_Rechnung_Lieferung(test_einkauf2)
    with pytest.raises(KeyError):
        testlieferant.kasse.erstelle_Rechnung_Lieferung(test_einkauf3)

def test_erfülle_Lieferung():
    test_einkauf1 = ["Mehl"]
    test_einkauf2 = []
    test_einkauf3 = ["Unsinnszutat"]

    rechnung = testlieferant.erfülle_Lieferung(test_einkauf1, testlagerbestand)
    assert rechnung == 50
    with pytest.raises(ValueError):
        assert testlieferant.erfülle_Lieferung(test_einkauf2, testlagerbestand)
    with pytest.raises(ValueError):
        assert testlieferant.erfülle_Lieferung(test_einkauf3, testlagerbestand)

def test_kassiere_Geld_ein():
    testgeld1 = 0
    testgeld2 = 100
    testgeld3 = -100

    with pytest.raises(ValueError):
        testlieferant.kassiere_Geld_ein(testgeld1)
    check_kasse_vor_einzahlung = testkasse.Geld_in_Kasse()
    testlieferant.kassiere_Geld_ein(testgeld2)
    check_kasse_nach_einzahlung = testkasse.Geld_in_Kasse()
    assert check_kasse_nach_einzahlung == check_kasse_vor_einzahlung + testgeld2
    with pytest.raises(ValueError):
        testlieferant.kassiere_Geld_ein(testgeld3)