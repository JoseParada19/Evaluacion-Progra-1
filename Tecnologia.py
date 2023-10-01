class Tecnologia:
    def __init__(self, voltaje, precio, eficiencia, marca):
        
        self.voltaje = voltaje
        self.precio = precio
        self.eficiencia = eficiencia
        self.marca = marca

#Getter y Setters----
    def get_voltaje(self):
        return self.voltaje
    def set_voltaje(self, voltaje):
        self.voltaje = voltaje

    def get_precio(self):
        return self.precio
    def set_precio(self, precio):
        self.precio = precio

    def get_eficiencia(self):
        return self.eficiencia
    def set_eficiencia(self, eficiencia):
        self.eficiencia = eficiencia

    def get_marca(self):
        return self.marca
    def set_marca(self, marca):
        self.marca = marca
#------------------
    def calcular_descuento(self):
        if self.eficiencia in ('A', 'B'):
            return 0.5
        elif self.eficiencia in ('C', 'D'):
            return 0.3
        elif self.eficiencia in ('E', 'F'):
            return 0.1
        else:
            return 0.0
#-------------------