from Tecnologia import Tecnologia

class Scooter(Tecnologia):
    def __init__(self, voltaje, precio, eficiencia, marca, aro, velocidad, peso):
        super().__init__(voltaje, precio, eficiencia, marca)

        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso

#getter y Setter-------
    def get_aro(self):
        return self.__aro
    def set_aro(self, aro):
        self.__aro = aro

    def get_velocidad(self):
        return self.__velocidad
    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def get_peso(self):
        return self.__peso
    def set_peso(self, peso):
        self.__peso = peso
#-----------------------