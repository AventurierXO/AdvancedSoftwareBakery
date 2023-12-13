#Domain Backstube

import Lager

class Ofen:

    pass

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

backwerkzeuge = Backwerkerkzeuge(werkzeuge)