# Imprimir Factorial de cualquier numero (A)
"""n = int(input("Numero:"))
factorial = 1
if n != 0:
    for i in range(1, n+1):
        factorial = factorial * i
print(f"Factorial:", factorial)

# Mostrar los N primeros numeros de la serie Fibonacci (B)


def fibonacci(n):
    a = 1
    b = 1
    if n == 1:
        print('0')
    elif n == 2:
        print('0', '1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n-3):
            total = a + b
            b = a
            a = total
            print(total)


fibonacci(2)

# PUNTO (C)
vp = float(input("Ingrese el valor del prestamo: "))
n = float(input("Ingrese numero de meses: "))
tasa = float(input("Ingrese Tasa Mensual: "))

cuota = (vp *(tasa*(1+tasa)**n)/((1 + tasa)**n)-1)

print(f"El valor de la cuota de un prestamo es:", cuota)"""


#Mostrar los datos de cualquier array (D)

listado = ['2', '4','6','8' ,'10']

for value in listado:
    print(f"Numeros elegidos:", value)


#Mostrar los datos de cualquier diccionario (E)

dataperson = {}
dataperson  ["Id"] = [2424]
dataperson  ["Nombres"] = ["Oswaldo"]
dataperson  ["Edad"] = [20]
dataperson  ["Ciudad"] = ["Montreal"]
dataperson  ["Nacionalidad"] = ["Colombiano"]

"""for data in dataperson :
    print (data)"""

for values in dataperson.values():
    print(values)

#Retornar el total de pagos (PUNTO 2)

dpagos = {"placa":"tis123","Marca":"Aveo","Pagos": [100,200,300,400]}

print(dpagos.get("Pagos", None))

# for pago, valor in dpagos.items:
#     print (f"El valor del pago es:", (pago,valor))


#Crear diccionario con varibles (PUNTO 3)

calificaciones = {"Artes": '4.2', "Ingles": '3.4', "Historia": '4.2'}


 #Punto 7
lst = list(calificaciones.values())
print(lst)
#Crea una lista con los numeros del 1 al 50 (PUNTO 4)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

#Buscar impares de la list (PUNTO 5)

def extraer_impares(imp):
    impares = []
    for n in imp:
        if n % 2 !=0:
            impares.append(n)
    return impares
print()

result = extraer_impares(lista)
print(result)#Punto 5

#Crear un diccionario con los datos de un vehiculo (PUNTO 6)

vehiculo = {"placa":"tis123","Marca":"Aveo","Modelo":"2012","valor":"7.000000"}


#Crear uan lista con las ciduades (PUNTO 8)

ciudades = ['Bogota', 'Cartagena','Medellin','Santa Marta','Cali']

#Listar ciudades en orden(Punto 9)
for city in ciudades:
    print(city)

#Agregar una ciudad(Puntpo 10)
ciudades.append('San andres de islas')

print(ciudades)

#Borrar ciudad (PUNTO 11)
del ciudades[5]
print(ciudades)

#clases de phyton
class vehiculo:
    #atributos __:private o privado
    __placa = ""
    __marca = ""
    __modelo = ""
    __precio = ""

    #constructor
    def __init__(self,placa,marca,modelo,precio) :
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio 
    
    def getPlaca(self):
        return self.__placa

    def setPlaca(self,placa):
        self.__placa = placa

    def getMarca(self):
        return self.__marca
    
    def setMarca(self,marca):
        self.__marca=marca

    def getModelo(self):
        return self.__modelo
    
    def setModelo(self,modelo):
        self.__modelo=modelo

    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self,precio):
        self.__precio= precio


