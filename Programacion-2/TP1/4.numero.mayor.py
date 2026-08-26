# Pedir 3 números enteros e implementar un algoritmo para determinar cuál es el
# mayor de los 3 y mostrar un mensaje por pantalla.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print(f"El número mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El número mayor es: {num2}")
else:
    print(f"El número mayor es: {num3}")
