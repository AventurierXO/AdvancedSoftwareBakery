class Rezepte:
    def __init__(self, rezepte):
        self.__rezepte = rezepte

    def hole_rezept(self, backstueck):
        if backstueck not in list(self.zeige_rezepte().keys()):
            raise KeyError("Für das Backstueck gibt es kein Rezept!")
        return self.__rezepte[backstueck]

    def zeige_rezepte(self):
        return self.__rezepte
