# Realizar un programa que solicite al usuario un número entero positivo, y luego en
# pantalla muestre solamente los números pares desde el 1 hasta el número
# ingresado.
# Ej: usuario ingresa 10, en pantalla se mostrará 2 4 6 8 10

numero = int(input("Ingrese un número entero positivo: "))
for i in range(1, numero + 1):
    if i % 2 == 0:
        print(i, end=" ")
