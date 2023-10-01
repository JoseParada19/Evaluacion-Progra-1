from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, voltaje, precio, eficiencia, marca, nombreConsola, version):
        super().__init__(voltaje, precio, eficiencia, marca)

        self.__nombreConsola = nombreConsola
        self.__version = version


#getter Setter----
    def get_nombreConsola(self):
        return self.__nombreConsola
    def set_nombreConsola(self, nombreConsola):
        self.__nombreConsola = nombreConsola

    def get_version(self):
        return self.__version
    def set_version(self, version):
        self.__version = version
#-----------------

