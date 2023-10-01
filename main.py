#--------------------------------#
#--------------------------------#
from Tecnologia import Tecnologia
from Transporte import Transporte
from Consola import Consola
from Tv import Tv
from Scooter import Scooter
from Bicicleta import Bicicleta
#----------------------------------------------------------------------
#Registros de Datos----
def registrar_tv(mostrartv):
    marca = input("Ingrese la marca del la Tv: ")
    voltaje = input("Ingrese el voltaje del Televisor: ")
    eficiencia = input("Ingrese el nivel de eficiencia (A, B, C, D, E o F) de la tv: ")
    precio = float(input("Ingrese el valor de la tv: "))
    tamano = input("Ingrese el tamaño en pulgadas del Televisor: ")
    tv = Tv(voltaje, precio, eficiencia, marca, tamano)
    mostrartv.append(tv)
    print("Registrado!!")
#----------------------------------------------------------------------
def registrar_consola(mostrarconsola):
    marca = input("Ingrese la marca de la Consola: ")
    voltaje = input("Ingrese un voltaje de la Consola: ")
    eficiencia = input("Ingrese el nivel de eficiencia (A, B, C, D, E o F) de la Consola: ")
    precio = float(input("Ingrese un valor de la Consola: "))
    nombreConsola = input("Ingrese un nombre de la Consola: ")
    version = input("Ingrese la versión de la Consola (Lite o otro): ")
    consola = Consola(voltaje, precio, eficiencia, marca, nombreConsola, version)
    mostrarconsola.append(consola)
    print("Registrado!!!!")
#----------------------------------------------------------------------
def registrar_scooter(mostrarscooter):
    marca = input("Ingrese la marca del Scooter: ")
    voltaje = input("Ingrese el voltaje del Scooter: ")
    eficiencia = input("Ingrese el nivel de eficiencia (A, B, C, D, E o F) del Scooter: ")
    precio = float(input("Ingrese el valor del Scooter: "))  
    aro = input("Ingrese el aro del Scooter: ")
    velocidad = input("Ingrese la velocidad máxima del Scooter: ")
    peso = float(input("Ingrese el peso en kilos del Scooter: "))  
    scooter = Scooter(voltaje, precio, eficiencia, marca, aro, velocidad, peso)
    mostrarscooter.append(scooter)
    print("Registrado!")
#----------------------------------------------------------------------
def registrar_bicicleta(mostrarbici):
    marca = input("Ingrese la marca de la Bici: ")
    aro = input("Ingrese el aro de la Bicii: ")
    peso = float(input("Ingrese el peso en kg de la Bici: ")) 
    precio = float(input("Ingrese el valor de la Bici: "))  
    costodespachobase = float(input("Ingrese el costo de despacho base de la Bici: "))  
    bicicleta = Bicicleta(aro, peso, precio, marca, costodespachobase)
    mostrarbici.append(bicicleta)
    print("Bici Registrada!")
#----------------------------
def cotizar_tv(mostrartv):
    print("---------------TV---------------")
    for tv in mostrartv:
        descuento_eficiencia = tv.calcular_descuento()  
        descuentotv = tv.precio * (1 - descuento_eficiencia)  
        print(f"Marca: {tv.marca}")
        print(f"Voltaje: {tv.voltaje}")
        print(f"Eficiencia: {tv.eficiencia}")
        print(f"Precio sin descuento: ${tv.precio:.2f}")
        print(f"Descuento de eficiencia: {descuento_eficiencia * 100:.2f}%")
        print(f"Precio con descuento: ${descuentotv:.2f}")
        print(f"Tamaño en pulgadas: {tv.get_tamano()} pulgadas ")
#--------------------------------------------------------------------        
def cotizar_consola(mostrarconsola):
    print("---------------Consola---------------")
    for consola in mostrarconsola:
        descuento_eficiencia = consola.calcular_descuento()
        descuentoconsola = consola.precio * (1 - descuento_eficiencia)
        print(f"Marca: {consola.marca}")
        print(f"Voltaje: {consola.voltaje}")
        print(f"Eficiencia : {consola.eficiencia}")
        print(f"Precio sin descuento: ${consola.precio:.2f}")
        print(f"Precio con descuento: ${descuentoconsola:.2f}")
        print(f"Nombre: {consola.get_nombreConsola()}")
        print(f"Versión: {consola.get_version()}")

#----------------------------------------------------------------------
def cotizar_scooter(mostrarscooter):
    print("---------------Scooter---------------")
    for scooter in mostrarscooter:
        descuento_eficiencia = scooter.calcular_descuento()  
        descuentoscooter = scooter.precio * (1 - descuento_eficiencia)  
        print(f"Marca: {scooter.marca}")
        print(f"Voltaje: {scooter.voltaje}")
        print(f"Eficiencia: {scooter.eficiencia}")
        print(f"Precio sin descuento: ${scooter.precio:.2f}")
        print(f"Precio con descuento: ${descuentoscooter:.2f}")
        print(f"Tamaño del aro: {scooter.get_aro()} pulgadas")
        print(f"Velocidad máxima: {scooter.get_velocidad()} km/h")
        print(f"Peso en kg: {scooter.get_peso()}")
#----------------------------------------------------------------------
def cotizar_bicicletas(mostrarbici):
    print("---------------Bicicleta---------------")
    for bicicleta in mostrarbici:
        print(f"Marca: {bicicleta.get_marca()}")
        print(f"Tamaño del aro: {bicicleta.get_aro()} pulgadas")
        print(f"Peso en kilos: {bicicleta.get_peso()}")
        print(f"Precio: ${bicicleta.get_precio()}")
#----------------------------------------------------------------------


#----------------
mostrartv=[]
mostrarconsola=[]
mostrarbici=[]
mostrarscooter=[]
#----------------

def menu():
    print("Elije una opcion")
    print("1. Registrar Televisores")
    print("2. Registrar Consolas")
    print("3. Registrar Bicicletas")
    print("4. Registrar Scooters")
    print("5. Cotizar televisores")
    print("6. Cotizar Consolas")
    print("7. Cotizar Bicicletas")
    print("8. Cotizar Scooters")
    print("9. Salir")

while True:
    menu()
    opcion = int(input("Elija una opcion: "))
    if opcion == 1:
        registrar_tv(mostrartv)
    elif opcion == 2:
        registrar_consola(mostrarconsola)
    elif opcion == 3:
        registrar_bicicleta(mostrarbici)
    elif opcion == 4:
        registrar_scooter(mostrarscooter)
    elif opcion == 5:
        cotizar_tv(mostrartv)
    elif opcion == 6:
        cotizar_consola(mostrarconsola)
    elif opcion == 7:
        cotizar_bicicletas(mostrarbici)
    elif opcion == 8:
        cotizar_scooter(mostrarscooter)
    elif opcion == 9:
            print("Hasta Pronto Crack")
            break
    else:
        print("Opcion Incorrecta")    
#----------------------------------------------------------------------          


#----Llamado de Funciones----
#registrar_tv()
#registrar_consola()
#registrar_scooter()
#registrar_bicicleta()
#mostrar_productos()
#-----------------------------


#def registrar_bicicleta():
#
#    marca=input("marca de la Bici: ")
#    aro=input("aro de la Bicii: ")
#    peso=float(input("kg de la Bici: ") 
#    precio=float(input("Ingrese el valor de la Bici: ")


#def mostrar_productos():
#   if len(productos) == 0:
#       print("No Registraste Nada")
#   else
#       print("PProductos registrados:")
#       for producto in productos:
#   