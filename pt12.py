#phyton Punto 12
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