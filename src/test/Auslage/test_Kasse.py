import pytest
from Auslage.Kasse import Kasse

test_kasse = Kasse(10000)
def test_geld_einzahlen():
    test_kasse.geld_einzahlen(200)
    assert test_kasse.geld_in_kasse() == 10200
    with pytest.raises(ValueError):
        test_kasse.geld_einzahlen(-200)
    with pytest.raises(ValueError):
        test_kasse.geld_einzahlen(0)
