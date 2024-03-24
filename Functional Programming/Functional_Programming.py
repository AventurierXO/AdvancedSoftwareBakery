"""
Funktionen ohne Seiteneffekte: alle
Higher-Order functions: closure_Fibonacci()
Funktionen als Parameter und return values:
    closure_Fibonacci() - gibt Funktion berechne_Fib_Zahl() zurück
    anonyme_Differentiation() - Parameter f ist eine Funktion (siehe Test-Datei)
Nutzung closure Funktion: closure_Fibonacci()
Nutzung anonymer Funktion: anonyme_Differentiation()
"""

def closure_Fibonacci():
    """Diese Funktion generiert mit jedem wiederholten Call die nächste Fibonacci-Zahl."""
    num1 = 0
    num2 = 0
    def berechne_Fib_Zahl():
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
    return berechne_Fib_Zahl

def berechne_Fib_Summe(n):
    """Diese Funktion gibt die Summe der generierten Fibonacci-Zahlen bis zur n-ten Fibonacci-Zahl zurück."""
    if n < 0:
        raise ValueError("Es gibt nur n-te Fibonacci-Zahlen >= 0! n darf nicht negativ sein!")
    fib = closure_Fibonacci()
    fib_list = []
    for i in range(n):
        fib_list.append(fib())
    return(sum(fib_list))

def anonyme_Differentiation(f, a, h = 0.00001):
    """Diese Funktion berechnet die lokale Ableitung einer Funktion f für die Stelle a."""
    diff = lambda h: (f(a + h) - f(a)) / h
    return diff(h)