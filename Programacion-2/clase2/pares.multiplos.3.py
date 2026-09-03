# generar una lista con los elementos pares multiplos de 3,
# menores a un numero ingresado por el usuario.
# dividir el problema en subproblemas


def leer_entero(mensaje: str) -> int:
    repetir = True
    while repetir:
        try:
            ingreso = input(mensaje)
            numero = int(ingreso)
            repetir = False
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            print("Intente nuevamente.")
    return numero


lista_pares = []
limite = -1
while limite < 0:
    limite = leer_entero("Ingrese un número entero positivo: ")

    for i in range(1, limite):
        if i % 2 == 0 and i % 3 == 0:
            lista_pares.append(i)

print(lista_pares)
