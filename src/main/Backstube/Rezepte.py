class Rezepte:
    def __init__(self, rezepte):
        self.__rezepte = rezepte

    def hole_Rezept(self, backstück):
        return self.__rezepte[backstück]
