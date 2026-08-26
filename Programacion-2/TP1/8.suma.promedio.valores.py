# Desarrollar un programa que permita al usuario indicar cuantos valores quiere
# ingresar, luego que permita la carga de los valores por teclado y nos muestre
# posteriormente la suma de los valores ingresados y su promedio.

cantidad = int(input("Ingrese la cantidad de valores que desea ingresar: "))
suma = 0
for i in range(cantidad):
    valor = float(input(f"Ingrese el valor {i + 1}: "))
    suma += valor

if cantidad > 0:
    promedio = suma / cantidad
else:
    promedio = 0
print(f"La suma de los valores ingresados es: {suma}")
print(f"El promedio de los valores ingresados es: {promedio}")
