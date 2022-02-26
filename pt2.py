# Imprimir Factorial de cualquier numero (A)
n = int(input("Numero:"))
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

print(f"El valor de la cuota de un prestamo es:", cuota)


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