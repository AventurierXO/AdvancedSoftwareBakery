class Angestellte:
    def __init__(self, name, lohn):
        self.__name = name
        self.__lohn = lohn

    def gebe_Namen_an(self):
        return self.__name

    def gebe_Lohn_an(self):
        return self.__lohn

    def ändere_Lohn(self, lohn):
        self.__lohn = lohn
