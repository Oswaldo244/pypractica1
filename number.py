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