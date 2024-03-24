import pytest
from Functional_Programming import berechne_Fib_Summe
from Functional_Programming import closure_Fibonacci
from Functional_Programming import anonyme_Differentiation

def test_closure_Fibonacci():
    f = closure_Fibonacci()
    assert f() == 0
    assert f() == 1
    assert f() == 1
    assert f() == 2
    assert f() == 3

def test_berechne_Fib_Summe():
    assert berechne_Fib_Summe(0) == 0
    assert berechne_Fib_Summe(5) == 7
    with pytest.raises(ValueError):
        assert berechne_Fib_Summe(-1)

def test_anonyme_Differentiation():
    f1 = lambda x: x + 1
    assert round(anonyme_Differentiation(f1, 2), 2) == 1

    f2 = lambda x: x**2
    assert round(anonyme_Differentiation(f2, 2), 2) == 4

    f3 = lambda x: x**2 + x + 1
    assert round(anonyme_Differentiation(f3, 2), 2) == 5