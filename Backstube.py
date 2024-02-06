#Domain Backstube

import Lager
class Ofen:

    def backt_teig(self, backwerk):
        print(f"Der Ofen backt nun {backwerk}.")
        print(f"{backwerk} wurde fertig gebacken.")
        return backwerk

class Backwerkerkzeuge:

    def __init__(self, backwerkzeuge):
        self.__backwerkzeuge = backwerkzeuge

    def verwendendet_Backwerkzeug(self, backwerkzeug):
        # backwerkzeug ist eine Liste von genutzten Geräten
        for gerät in backwerkzeug:
            if backwerkzeug[gerät] == 0:
                return f"Es ist gerade kein {gerät} verfügbar."
            else:
                backwerkzeug[gerät] -= 1


werkzeuge = {
        "Mixer": 3,
        "Nudelholz": 3,
        "Tortenform": 3,
        "Schüssel": 10,
        "Rührlöffel": 4
    }

rezepte = {
    "Weizensemmel": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1)],
    "Kürbiskernbrötchen": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1), ("Kürbiskerne", 1)],
    "Roggenmischbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Vollkornbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Dinkelbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
    "Croissant": [("Mehl", 1), ("Butter", 1), ("Hefe", 1), ("Milch", 1), ("Zucker", 1)],
    "Streuselkuchen",
    "Bienenstich",
    "Pfannkuchen"
}

backwerkzeuge = Backwerkerkzeuge(werkzeuge)