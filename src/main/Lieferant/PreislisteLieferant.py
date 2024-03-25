from Auslage.Preisliste import Preisliste

class PreislisteLieferant(Preisliste):
    """
    Diese Klasse repräsentiert die Preisliste des Lieferanten

    Attribute:
    ----------
    preisliste: Dictionary
        eine Übersicht von Waren und ihren zugehörigen Preisen
    """
    def __init__(self, preisliste):
        super().__init__(preisliste)
