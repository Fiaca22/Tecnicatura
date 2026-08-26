# Escriba un programa que permita el ingreso de números enteros positivos,
# finalizando el ingreso con 0, y luego indique si la secuencia estaba ordenada de
# menor a mayor.

print(
    "Ingrese números enteros positivos para verificar si la secuencia está ordenada de menor a mayor. Ingrese 0 para finalizar."
)

numero = int(input("Ingrese un número: "))
anterior = 0
ordenado = True

while numero != 0:
    if numero < anterior:
        ordenado = False
    anterior = numero
    numero = int(input("Ingrese un número: "))

if ordenado:
    print("La secuencia está ordenada de menor a mayor.")
else:
    print("La secuencia no está ordenada de menor a mayor.")
