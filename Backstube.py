#Domain Backstube

import Lager
class Rezepte:
    def __init__(self, rezeptbuch):
        self.__rezeptbuch = rezeptbuch

    def schaut_Rezepte_an(self):
        return rezeptbuch

rezeptbuch = {
"Weizensemmel": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1)],
"Kürbiskernbrötchen": [("Mehl", 2), ("Wasser", 1), ("Hefe", 1), ("Kürbiskerne", 1)],
"Roggenmischbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
"Vollkornbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
"Dinkelbrot": [("Mehl", 4), ("Wasser", 2), ("Hefe", 2)],
"Croissant": [("Mehl", 1), ("Butter", 1), ("Hefe", 1), ("Milch", 1), ("Zucker", 1)],
"Streuselkuchen": [("Mehl", 4), ("Hefe", 1), ("Zucker", 3), ("Milch", 2), ("Butter", 3)],
"Bienenstich": [("Mehl", 4), ("Milch", 4), ("Zucker", 1), ("Butter", 2), ("Hefe", 1)],
"Pfannkuchen": [("Eier", 2), ("Mehl", 2), ("Milch", 1), ("Zucker", 1)]
}

rezepte = Rezepte(rezeptbuch)