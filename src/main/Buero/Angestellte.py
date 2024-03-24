class Angestellte:
    def __init__(self, name, lohn):
        self.__name = name
        self.__lohn = lohn

    def gebe_namen_an(self):
        return self.__name

    def gebe_lohn_an(self):
        return self.__lohn

    def aendere_lohn(self, lohn):
        self.__lohn = lohn
