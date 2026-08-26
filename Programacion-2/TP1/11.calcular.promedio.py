# Escriba un programa que permita el ingreso de números enteros positivos para
# calcular su promedio, el ingreso finaliza cuando el usuario ingresa un número
# negativo. Luego mostrar el promedio y la cantidad de valores que se ingresaron. Ej:
# “El promedio es ….. con un total de …. ingresos.” sin el uso de break.
# NO SE PUEDE USAR BREAK, SE DEBE USAR UN WHILE PARA CONTROLAR EL INGRESO DE DATOS.

print(
    "Ingrese números enteros positivos para calcular su promedio. Ingrese un número negativo para finalizar."
)

suma = 0
cantidad = 0

numero = int(input("Ingrese un número: "))
while numero >= 0:
    suma += numero
    cantidad += 1
    numero = int(input("Ingrese un número: "))

if cantidad > 0:
    promedio = suma / cantidad
    print(f"El promedio es {promedio} con un total de {cantidad} ingresos.")
else:
    print("No se ingresaron números positivos.")
