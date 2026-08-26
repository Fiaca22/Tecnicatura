# Se desea realizar una aplicación que solicite al usuario un caracter y un número
# natural N, y que la aplicación muestre en pantalla dicho carácter repetido N veces
# consecutivas.
# Ej: Ingrese un caracter: +
# Ingrese la cantidad de repeticiones: 15
# +++++++++++++++

print(
    "Ingrese un caracter y un número natural N, para mostrar en pantalla dicho carácter repetido N veces consecutivas."
)
caracter = input("Ingrese un caracter: ")
numero = int(input("Ingrese la cantidad de repeticiones: "))
for i in range(numero):
    print(caracter, end="")
