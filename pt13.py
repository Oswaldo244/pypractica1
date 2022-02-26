#Importar funciones

from pfunciones.funciones import vehiculo

#intanciar la clase persona (PUNTO 12)
car = vehiculo("1534","Yamaha","2022","2000000")
print(f"Placa del Vehiculo:{car.getPlaca()}")
print(f"Marca del Vehiculo:{car.getMarca()}")
print(f"Modelo del Vehiculo:{car.getModelo()}")
print(f"Precio del Vehiculo:{car.getPrecio()}")

car.setMarca("Toyota")
print(f"Nueva Marca: {car.getMarca()}")
#Set es para cambiar y Get para obtener
car.setPlaca("690")
print(car.getPlaca())