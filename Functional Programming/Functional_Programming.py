"""
Funktionen ohne Seiteneffekte: alle
Higher-Order functions: closure_fibonacci()
Funktionen als Parameter und return values:
    closure_fibonacci() - gibt Funktion berechne_fib_zahl() zurueck
    anonyme_differentiation() - Parameter f ist eine Funktion (siehe Test-Datei)
Nutzung closure Funktion: closure_fibonacci()
Nutzung anonymer Funktion: anonyme_differentiation()
"""

def closure_fibonacci():
    """Diese Funktion generiert mit jedem wiederholten Call die naechste Fibonacci-Zahl."""
    num1 = 0
    num2 = 0
    def berechne_fib_zahl():
        """Diese Helferfunktion berechnet Fibonacci-Zahlen."""
        nonlocal num1, num2
        if num1 ==0 and num2 ==0:
            num2 = 1
            return num1
        else:
            n = num1 + num2
            num2 = num1
            num1 = n
            return n
    return berechne_fib_zahl

def berechne_fib_summe(n):
    """Diese Funktion gibt die Summe der generierten Fibonacci-Zahlen bis zur n-ten Fibonacci-Zahl zurueck."""
    if n < 0:
        raise ValueError("Es gibt nur n-te Fibonacci-Zahlen >= 0! n darf nicht negativ sein!")
    fib = closure_fibonacci()
    fib_list = []
    for i in range(n):
        fib_list.append(fib())
    return(sum(fib_list))

def anonyme_differentiation(f, a, h = 0.00001):
    """Diese Funktion berechnet die lokale Ableitung einer Funktion f fuer die Stelle a."""
    diff = lambda h: (f(a + h) - f(a)) / h
    return diff(h)