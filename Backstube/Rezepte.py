class Rezepte:
    def __init__(self, rezepte):
        self.__rezepte = rezepte

    def holt_Rezept(self, backstück):
        return self.__rezepte[backstück]
