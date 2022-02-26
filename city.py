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