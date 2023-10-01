from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, voltaje, precio, eficiencia, marca, tamano):
        super().__init__(voltaje, precio, eficiencia, marca)

        self.__tamano = tamano
#getter yt Setter
    def get_tamano(self):
        return self.__tamano
    def set_tamano(self, tamano):
        self.__tamano = tamano
#-----





