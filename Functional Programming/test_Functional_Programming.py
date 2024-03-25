import pytest
from Functional_Programming import berechne_fib_summe
from Functional_Programming import closure_fibonacci
from Functional_Programming import anonyme_differentiation

def test_closure_fibonacci():
    f = closure_fibonacci()
    assert f() == 0
    assert f() == 1
    assert f() == 1
    assert f() == 2
    assert f() == 3

def test_berechne_fib_summe_korrekt():
    assert berechne_fib_summe(0) == 0
    assert berechne_fib_summe(5) == 7

def test_berechne_fib_summe_negative_zahl():
    with pytest.raises(ValueError) as valueerror:
        berechne_fib_summe(-1)
    assert str(valueerror.value) == "Es gibt nur n-te Fibonacci-Zahlen >= 0! n darf nicht negativ sein!"

def test_anonyme_differentiation():
    f1 = lambda x: x + 1
    assert round(anonyme_differentiation(f1, 2), 2) == 1

    f2 = lambda x: x**2
    assert round(anonyme_differentiation(f2, 2), 2) == 4

    f3 = lambda x: x**2 + x + 1
    assert round(anonyme_differentiation(f3, 2), 2) == 5